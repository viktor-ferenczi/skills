# Updating the SDL3 wiki snapshot

This file tracks where the mirrored content under [`references/`](references/)
came from and how to refresh it from upstream. End users of the skill don't
need any of this — see [SKILL.md](SKILL.md) for the user-facing TOC.

## Snapshot provenance

- **Upstream source:** <https://github.com/libsdl-org/sdlwiki> (path: `SDL3/`)
- **Snapshot commit:** `3f54699ba6a0fa292b57c7a3eeacf3bd060c389a` (2026-05-05)

## What was changed relative to upstream

The upstream wiki contains a large number of *redirect* pages — pages whose
body is just a "moved to" or "please refer to" pointer at another page. They
exist because every API constant (`SDLK_*`, enumerators, hint/property names,
…) gets its own page that simply forwards to its parent enum/hint/keycode
page. They add no information and bloat the corpus.

This skill eliminates those pages and rewrites every link that pointed at one
to point at the destination instead.

| | Upstream | This skill |
|---|---:|---:|
| Pages under `references/` | 4,293 | 2,371 |
| Redirect pages              | 1,922 | 0 |
| Indexed API symbols         | 4,119 | 4,119 |

The two redirect-page patterns recognised:

- `# Moved\n\nThis page has moved to [X](X).` — 35 pages (everything under
  `references/README/`, plus `references/SupportedPlatforms.md`).
- `# X\n\nPlease refer to [Y](Y) for details.` — 1,887 pages
  (`SDLK_*` keycodes, enumerator constants, hint/property names, …).

The `references/README/` subdirectory was removed (it contained only
redirects). Top-level `references/README-*.md` pages — the actual content
those redirects pointed at — are kept.

### Case-insensitive filename collisions

A handful of upstream pages are *distinct* symbols whose names differ only
in letter case (e.g. `SDL_Log` the logging function vs `SDL_log` the natural
logarithm). The upstream wiki stores each as its own file and relies on a
case-*sensitive* filesystem to tell them apart. That breaks the moment the
repo is checked out on a case-*insensitive* filesystem (Windows, default
macOS): only one file of each pair can exist on disk, so git reports the
other as permanently "modified" — a phantom diff.

To make the skill check out cleanly on every platform, the more-prominent /
more-linked symbol of each colliding set keeps its natural name, and the
other is renamed with a `__uppercase` / `__lowercase` suffix describing its
own casing. Every link in the corpus that pointed at the renamed page is
retargeted to the new filename (the visible link text — the true symbol
name — is left unchanged). The six renames:

| Kept (canonical) | Renamed page → new filename |
|---|---|
| `SDL_Log.md` (logging function) | `SDL_log.md` → `SDL_log__lowercase.md` (natural-log math fn) |
| `SDL_malloc.md` (allocation function) | `SDL_MALLOC.md` → `SDL_MALLOC__uppercase.md` (allocator-tag macro) |
| `SDL_PixelType.md` (enum) | `SDL_PIXELTYPE.md` → `SDL_PIXELTYPE__uppercase.md` (pixel-type macro) |
| `SDL_PRILLx.md` (lower-case-hex macro) | `SDL_PRILLX.md` → `SDL_PRILLX__uppercase.md` (upper-case-hex macro) |
| `SDL_PRIx32.md` (lower-case-hex macro) | `SDL_PRIX32.md` → `SDL_PRIX32__uppercase.md` (upper-case-hex macro) |
| `SDL_PRIx64.md` (lower-case-hex macro) | `SDL_PRIX64.md` → `SDL_PRIX64__uppercase.md` (upper-case-hex macro) |

To find any *new* collisions after a refresh:
`git ls-files | sort -f | uniq -Di`.

## Refresh procedure

1. Pull the latest upstream snapshot:

   ```sh
   git clone --depth 1 https://github.com/libsdl-org/sdlwiki /tmp/sdlwiki
   rm -rf references
   cp -r /tmp/sdlwiki/SDL3 references
   ```

2. Re-run the trampoline-elimination pass: walk every `.md` under
   `references/`, identify pages whose body matches one of the two redirect
   patterns above, retarget every link in the corpus that pointed at one of
   those pages, then delete them. Also remove the now-empty
   `references/README/` directory if present.

3. Re-apply the case-collision disambiguation pass (see *Case-insensitive
   filename collisions* above): run `git ls-files | sort -f | uniq -Di` to
   list any names that collide case-insensitively, rename the non-canonical
   member of each pair with a `__uppercase`/`__lowercase` suffix, and
   retarget every link that pointed at it.

4. Regenerate `PAGE_INDEX.md` and `API_INDEX.md` from the updated
   `references/Category*` files (the indexes are derived purely from the
   wiki's own auto-maintained category lists). Apply the same link
   retargeting from step 3 to the regenerated indexes.

5. Update the **Snapshot commit** hash and date above, and any totals in
   [SKILL.md](SKILL.md) that have shifted.

## License

The wiki content under `references/` is © its respective authors and
licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Attribution and the disclosure of modifications (trampoline elimination
and link retargeting) are stated in [SKILL.md](SKILL.md).
