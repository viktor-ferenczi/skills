---
name: domain-specific-documentation
description: Systematic plan for generating domain-specific documentation from any documents, including but not limited to source code. Use this skill if the task at hand involves working with a significant number of documents or resources, especially if they relate to each other in intricate ways and their total size exceeds the maximum context size.
license: MIT
---

# General rules

## Optimize for token efficiency

- Use sub-agents to process documents (code, configuration, or other content) required for the task.
- Prefer programmatic extraction and classification over reading full document contents.
- Store hashes to detect changes programmatically, enabling caching of prior results.
  Hash text and source files by their LF-normalized content (see "Document index") so the cache key is platform-independent.
- Generate and reuse utility scripts to avoid duplicate AI inference.

## Don't reinvent the wheel

The domain may already have established programmatic ways to map system state or generate a documentation index.
If such solutions exist, evaluate whether they fit your situation. Building on an existing, well-tested
domain-specific solution is usually better than rolling your own, unless it requires significant changes or has
unacceptable limitations.

# Preparation

Establish detailed domain-specific documentation before working on actual tasks to improve token efficiency down the line.

If the documentation already exists, check for modifications programmatically (via hashes) and update as needed.
Otherwise, plan to produce it from the ground up.

## Write a plan

- Plan producing the domain-specific documentation for the environment related to your task.
- Track progress in files; optimize for resuming with minimal loss if interrupted.
- Parallelize with multiple sub-agents, while avoiding collisions that cause loss of work.
- Avoid long-context inference. Ideally, split into sub-tasks that fit under 200000 tokens. Exceptions are allowed.

## Establish document tiers

- Tier 1: High-complexity, usually important and short
- Tier 2: Medium-complexity, occasionally long, must be understood in full
- Tier 3: Low-complexity, repetitive (high redundancy) and/or less important, potentially very long

## Generate documentation

### Document index

Find and index all documents required for the task. Ensure the scope is clear.

Use a common format such as JSON or JSONL. The index must include each document's name, location, tier, and SHA256 hash.
Determine tier from heuristics (location, file type) or programmatic semantic analysis; avoid reading whole documents when possible.
Identify programmatically generated documents (code, configuration or data) and prefer referring to the source they are generated from instead.
The hash enables change detection so further analysis can be cached. Store a timestamp if applicable, but prefer the hash.

**Normalize line endings before hashing text files.** For text and source files, strip carriage returns (convert
CRLF and lone CR to LF) on the raw bytes, then hash the LF-only content. This keeps the hash stable across operating
systems and Git checkouts — Git with `core.autocrlf=true` rewrites newlines on clone/checkout, which would otherwise
change the hash and invalidate the cache for unchanged content. Detect text vs. binary programmatically (e.g. by
extension or a null-byte/encoding check) and hash binary files by their exact bytes (no normalization). Apply the
same normalization on every run.

Keep index files for reuse and up to date during follow-up tasks.

### Summarize individual documents

Write one summary file per document. Standardize the directory structure around the documents' layout;
otherwise, assign identifiers (e.g., GUIDs) in the index and use those as names.

Choose AI models and analysis methods by tier and content type. For code, parse with TreeSitter or another suitable parser.

When programmatic analysis can't extract the meaning (e.g., complex source code), pick a model by tier:
- Tier 1: Strong reasoning model (e.g., Opus 4.6, GPT 5.4, or better)
- Tier 2: Generic model (e.g., Sonnet 4.6, GPT 5.4-Mini); modest price with sufficient reasoning
- Tier 3: Cheap model (e.g., Haiku 4.5, GPT 5.3-Nano); low price, high throughput and quota

**CRITICAL**: An index and documentation alone are usually not enough. You must understand the important,
typically small and complex parts of the code and configuration. Use heuristics and static analysis to classify
tiers correctly before spending tokens on detailed reads. This avoids lengthy, repetitive, or generated files.

### Build modular documentation

- Analyze references between source documents.
- Group documents with strong coupling and cohesion into modules.
- For each module, build one documentation file from its documents' summaries, using intra-module references to clarify relationships.
- Enrich each document summary with intra-module context; ensure each document is referenced from its module.
- Build a top-level Table of Contents (TOC) summarizing and referencing each module.
- Enrich each module's documentation with cross-references to modules it interacts with.
- Verify consistency across the index, document summaries, module docs, and TOC.
- Run an information-propagation step to add transitive references where important.

### Storing the domain-specific documentation

After first generation, ask the user where to store the documentation permanently. An active project is a natural
location, but size constraints or other requirements may dictate otherwise. Clarify with the user if unclear.

Suggest that the user add references to the generated documentation and this skill in the project's AGENTS.md,
CLAUDE.md, or other relevant project-specific prompt file for the agentic coding tool(s) used in the project.