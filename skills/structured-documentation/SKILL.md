---
name: structured-documentation
description: >
  Generate a verified, modular handbook from a large source-code or document tree, then keep it
  cheap to refresh as the inputs change. Use when the documents are numerous, relate to each other
  in intricate ways, or their total size exceeds the context window — and you need a navigable
  TOC/Index with verified cross-references rather than an ad-hoc summary.
license: MIT
---

# Principles

Apply these throughout the pipeline below; they decide what to read, what to cache, and what to skip.

## Optimize for token efficiency

- Process documents (code, configuration, data, prose) with sub-agents, not in one long context.
- Prefer programmatic extraction and classification over reading full document contents.
- Store SHA256 hashes to detect changes programmatically, enabling caching of prior results.
  Hash text and source files by their LF-normalized content (see step 2) so the cache key is platform-independent.
- Generate and reuse utility scripts to avoid duplicate AI inference.
- Split work into sub-tasks that fit comfortably under the model's context limit (≈200k tokens). Exceptions allowed.

## Don't reinvent the wheel

The domain may already have established tools to map system state, index code, or generate a documentation
tree. Evaluate whether they fit before rolling your own — building on an existing, well-tested solution is
usually better unless it needs significant changes or has unacceptable limitations.

## Incremental by default

The hash recorded for every input is the cache key. On any re-run, skip documents whose hash is unchanged and
reuse their existing descriptions; only re-process the differences and propagate the effects. Keep every data
file the pipeline produces so later runs are cheap.

## Resumability

Use task management and progress files so an interruption costs minimal rework. Parallelize with sub-agents
while avoiding collisions that lose work.

# Pipeline

1. Set up task management. Parallelize with sub-agents. Ensure resumability after interruption.
   Create a single dedicated subdirectory to hold **everything** this process generates — write nothing to the
   project root. Within it, keep all working data files (index, hashes, reference graph, module list, tier data,
   path mapping, progress files, generated scripts) in a clearly named `data/` subdirectory, separate from the
   documentation tree (descriptions, module descriptions, `TOC.md`, `Index.md`), which lives in the output root
   alongside it. Containing all generated files this way lets the user exclude the whole directory from version
   control (e.g. via `.gitignore`) or delete just the `data/` subdirectory in one step. Ask the user for the
   location and name if a sensible default isn't obvious.

2. Build a manifest/index of all input documents as JSON or JSONL in the `data/` subdirectory. For each document record: name, location,
   file type, size, **SHA256 hash**, tier (assigned in step 4), and optionally a timestamp (prefer the hash).
   - The hash enables change detection so all downstream analysis can be cached and reused across runs.
   - **Normalize line endings before hashing text files.** For text and source files, strip carriage returns
     (convert CRLF and lone CR to LF) on the raw bytes, then hash the LF-only content. This keeps the hash
     stable across operating systems and Git checkouts — Git with `core.autocrlf=true` rewrites newlines on
     clone/checkout, which would otherwise change the hash and invalidate the cache for unchanged content.
     Detect text vs. binary programmatically (e.g. by extension or a null-byte/encoding check) and hash binary
     files by their exact bytes (no normalization). Apply the same normalization on every run.
   - Identify programmatically generated documents (from code, configuration, or data) and prefer referring to
     the source they are generated from instead of analyzing the generated output.
   - On a re-run, load the prior index and mark documents whose hash matches as cache hits; process only the rest.

3. Convert non-text files to readable text with minimal content loss. Prefer existing tools (e.g. `pandoc`) over
   AI models, which cost more tokens. Use a cheap or local multimodal model for image descriptions. Mark empty
   or unconvertible files as skipped.

4. Categorize documents into tiers by content type, size, and complexity. Store tiers in the index/data file.
   Ask the user to clarify size thresholds (bytes, characters, tokens, or lines) or expected modules if ambiguous.
   Use heuristics (location, file type) and static analysis to classify tiers **before** spending tokens on reads,
   so lengthy, repetitive, or generated files don't get expensive treatment.
   - Tier 1: High-complexity, usually important, small-to-medium, must be understood in full. Strong reasoning
     model (e.g. Opus 4.8, GPT 5.5, or better).
   - Tier 2: Medium-complexity, occasionally long, simple/repetitive or low-priority. Cheaper, faster model
     (e.g. Sonnet 4.6, GPT 5.4-Mini).
   - Tier 3: Large or highly repetitive/low-priority. Cheapest model or programmatic summarization
     (e.g. Haiku 4.5, GPT 5.3-Nano).

5. Pre-process file types programmatically, without per-file AI calls where avoidable:
   - Generate initial source-code descriptions with language-appropriate documentation tools.
   - Extract structural metadata from each file (e.g. parent class, interfaces, abstract/concrete, fields,
     members, properties, events). Define a consistent header format with a fixed item order across all files.
   - Batch-describe images via a cheap or local multimodal model.
   - Produce one Markdown description file per non-skipped document.
   - Write resumable pre-processing scripts with a formal execution plan.
   - Mirror the original directory structure under the output root. Flatten or normalize long/incompatible paths
     and log the mapping to a data file in `data/`.
   - **Output paths must be unique on case-insensitive filesystems.** No two generated files or directories may
     differ only in letter casing (e.g. `Parser.md` vs. `parser.md`, or a `Net/` and `net/` directory). Source
     trees built on Linux routinely contain such siblings, but Windows and macOS treat them as the same path, so
     committing the docs from Linux and cloning on Windows/macOS causes file collisions (one file overwrites the
     other, or the checkout fails). Detect case-insensitive path collisions programmatically while building the
     path mapping and disambiguate them deterministically (e.g. append a short hash or numeric suffix to the
     colliding name). Record the chosen names in the path-mapping data file so they stay stable across runs.

6. Run pre-processing to completion. Verify every non-skipped document has a description file.

7. Post-process each description with the tier-appropriate AI model. Apply only to types that need it (e.g. source
   code, text). Skip data files and images already described. Track progress via task management.
   **Critical**: an index and descriptions alone are not enough — you must understand the important, typically
   small and complex parts in full. Spend the strong model where tiering says it matters.

8. Plan information propagation based on file structure and inter-document relationships:
   - Horizontal: across documents at the same abstraction level.
   - Vertical: between abstraction levels.
   - For source code: build a code index if none exists. Prefer existing indexing tools; fall back to TreeSitter.
     Keep the index simple but preserve cross-references.

9. Execute the propagation plan. Add cross-references to description files. Store the reference graph in a data file in `data/`.

10. Cluster documents by cross-references into modules (subsystems) with strong coupling and cohesion. Store the
    module list in a data file in `data/`. Decide whether multi-module membership is allowed based on project context and file type.

11. Build a top-level `TOC.md` from the module list.

12. In a separate subdirectory, write a description file per module listing its member documents.

13. For each module:
    - Collect summaries from all member descriptions.
    - Synthesize a module-level summary and enrich the module description with intra-module references.
    - Re-process each member description using the enriched module context.
    - For source code: ensure all fields, members, properties, and events have descriptions.

14. Collect all module contexts. Add a project-level description to `TOC.md` using the enriched module contexts,
    with cross-references between modules that interact.

15. Evaluate completeness at project and module levels. Verify a reader can locate any description within a few
    steps via progressive disclosure. If not, return to step 13. Repeat up to 6 times, numbering each run and
    tracking progress for resumability.

16. Verify structure: `TOC.md` links to module descriptions; module descriptions link to document descriptions;
    all links are cross-referenced.

17. Add `Index.md` referencing every document description regardless of module. Link it from `TOC.md`.

18. Programmatically verify all references. Fix any broken links.

19. Evaluate module boundaries against project context. If inadequate, ask the user for guidance and restructure.
    Reuse existing work by updating only the differences (using the hashes from step 2). After restructuring,
    re-verify all references.

20. If module boundaries are sound, present a final summary to the user.

# Storage and integration

- After the first generation, ask the user where to store the documentation permanently. An active project is a
  natural location, but size constraints or other requirements may dictate otherwise. Clarify if unclear.
- Suggest that the user reference both the generated documentation and this skill in the project's `AGENTS.md`,
  `CLAUDE.md`, or other agent-specific prompt file, so later tasks discover and reuse it.
- Keep all data files produced during the process in the `data/` subdirectory (index with hashes, reference graph,
  module list, tier data, path mapping, progress files, scripts). They make follow-up runs cheap — re-process only
  what changed — and let the user iterate further. Because they are contained in one subdirectory, the user can
  exclude them from version control or remove them without disturbing the documentation tree.
