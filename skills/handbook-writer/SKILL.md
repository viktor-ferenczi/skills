---
name: handbook-writer
description: >
  Generate a structured handbook from source documents.
  Use to document legacy code or build a table of contents from any document collection.
license: MIT
---

1. Set up task management. Parallelize with sub-agents. Ensure resumability after interruption.
2. Build a manifest of all input documents listing file type and size.
3. Convert non-text files to readable text with minimal content loss.
   Prefer existing tools (e.g. `pandoc`) over AI models, which cost more tokens.
   Use a cheap or local multimodal model for image descriptions.
   Mark empty or unconvertible files as skipped.
4. Categorize documents into tiers by content type, size, and complexity. Store tiers in a data file.
   Ask the user to clarify size thresholds (bytes, characters, tokens, or lines) or expected modules if ambiguous.
   - Tier 1: Complex, small-to-medium, or high-priority documents. Use the most capable AI model.
   - Tier 2: Medium documents with simple, repetitive, or low-priority content. Use a cheaper, faster model.
   - Tier 3: Large or highly repetitive/low-priority documents. Use the cheapest model or programmatic summarization.
5. Pre-process file types programmatically without per-file AI calls:
   - Generate initial source code descriptions with language-appropriate documentation tools.
   - Extract structural metadata from each file
     (e.g. parent class, interfaces, abstract/concrete, fields, members, properties).
     Define a consistent header format with a fixed item order across all description files.
   - Batch-describe images via a cheap or local multimodal model.
   - Produce one Markdown description file per non-skipped document.
   - Write resumable pre-processing scripts with a formal execution plan.
   - Mirror the original directory structure.
     Flatten or normalize long/incompatible paths and log the mapping.
6. Run pre-processing to completion. Verify every non-skipped document has a description file.
7. Post-process each description with the tier-appropriate AI model.
   Apply only to types that need it (e.g. source code, text). Skip data files and images already described.
   Track progress via task management.
8. Plan information propagation based on file structure and inter-document relationships:
   - Horizontal: across documents at the same abstraction level.
   - Vertical: between abstraction levels.
   - For source code: build a code index if none exists. Prefer existing indexing tools; fall back to TreeSitter.
     Keep the index simple but preserve cross-references.
9. Execute the propagation plan. Add cross-references to description files.
   Store the reference graph in a data file.
10. Cluster documents by cross-references into modules (subsystems). Store the module list in a data file.
    Decide whether multi-module membership is allowed based on project context and file type.
11. Build a top-level `TOC.md` from the module list.
12. In a separate subdirectory, write a description file per module listing its member documents.
13. For each module:
    - Collect summaries from all member descriptions.
    - Synthesize a module-level summary and enrich the module description.
    - Re-process each member description using the enriched module context.
    - For source code: ensure all fields, members, properties, and events have descriptions.
14. Collect all module contexts.
    Add a project-level description to `TOC.md` using the enriched module contexts.
15. Evaluate completeness at project and module levels.
    Verify a reader can locate any description within a few steps via progressive disclosure.
    If not, return to step 13. Repeat up to 6 times, numbering each run. Track progress for resumability.
16. Verify structure: `TOC.md` links to module descriptions;
    module descriptions link to document descriptions; all links are cross-referenced.
17. Add `Index.md` referencing every document description regardless of module. Link it from `TOC.md`.
18. Programmatically verify all references. Fix any broken links.
19. Evaluate module boundaries against project context.
    If inadequate, ask the user for guidance and restructure.
    Reuse existing work by updating only the differences.
    After restructuring, re-verify all references.
20. If module boundaries are sound, present a final summary to the user. 

Keep all the data files produced during the writing process, so the user can use them to iterate on the book further.
