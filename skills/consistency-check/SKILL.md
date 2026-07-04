---
name: consistency-check
description: Finds and fixes internal inconsistencies in a software project — code vs configuration vs documentation drift, plus linter findings. Use after a larger change or refactoring, before a release, or when the user asks to check/clean up the consistency of the project.
license: MIT
---

Check the project for internal inconsistencies and fix what you find. Work through the passes below in order.
Cap each pass at **3 iterations**; if issues remain after that, stop fixing and list them in the final report instead.

1. **Code ↔ code.** Look for drift within the codebase:
   - References to renamed/removed symbols, files, endpoints, or CLI flags (grep for old names after renames).
   - The same constant, magic value, or default duplicated with different values in different places.
   - Inconsistent naming for the same concept across modules.
   - Dead exports/imports and commented-out code left behind by refactorings.
2. **Configuration ↔ code.** Compare configuration against what the code actually reads:
   - Config keys, environment variables, and feature flags that the code no longer reads, or reads but are missing from config templates/examples.
   - Mismatched defaults between code and config files.
   - Build/CI files referencing scripts, paths, or targets that no longer exist.
3. **Linters.** Discover the project's linters and formatters instead of assuming any:
   check config files (e.g. `pyproject.toml`, `.eslintrc*`, `.golangci.yml`, `.editorconfig`), `package.json` scripts,
   `Makefile`/`justfile` targets, and CI workflows. Run what you find and fix the findings.
   If the project defines no linters, skip this pass — do not introduce new tools.
4. **Documentation ↔ code and configuration.** Update docs to match reality:
   - README/setup instructions that no longer work (commands, paths, prerequisites, version numbers).
   - Documented APIs, options, or behavior that changed in code.
   - Doc comments/docstrings contradicting the code they describe.
5. **Final cross-check.** Re-scan anything you modified in passes 1–4 for new inconsistencies introduced by the fixes
   (one pass only, no loop).

Remarks:
- Fix inconsistencies; do not redesign. If the correct resolution is ambiguous (e.g. code and docs disagree and either could be intended), ask the user instead of guessing.
- Never delete or disable tests to make a pass "consistent".
- Prefer programmatic checks (grep, existing linters, link checkers) over reading whole files.

Once done, provide a concise report: fixes made per pass, issues left unresolved (with why), and anything that needs the user's decision.
