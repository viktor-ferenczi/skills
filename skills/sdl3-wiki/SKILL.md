---
name: sdl3-wiki
description: Complete offline copy of the SDL3 (Simple DirectMedia Layer 3) wiki in CommonMark format. Use this skill whenever the user is working with SDL3 — writing or porting code that calls SDL_*, asking about SDL subsystems (audio, video, GPU, input, events, render, surface, gamepad, joystick, haptic, threads, file I/O, etc.), looking up an SDL function/struct/enum/macro signature, migrating from SDL2 to SDL3, or referencing SDL3 hints/properties/keycodes/scancodes. Prefer this skill over guessing API shapes from memory — SDL3 changed many SDL2 names and signatures.
license: CC BY 4.0 (wiki content); see references/FAQLicensing.md and https://creativecommons.org/licenses/by/4.0/
---

# SDL3 Wiki — Offline Reference

This skill is an offline mirror of the official SDL3 wiki at
<https://wiki.libsdl.org/SDL3/>, sourced from the upstream
[`libsdl-org/sdlwiki`](https://github.com/libsdl-org/sdlwiki) repository
(`SDL3/` subtree). The original pages were already authored in CommonMark
Markdown, so no format conversion was required — every page in
[`references/`](references/) is the exact source published on the wiki,
except that pure redirect pages have been eliminated and references to them
rewritten to point at the destination page (see [UPDATING.md](UPDATING.md)).

- **License of the wiki content:** Creative Commons Attribution 4.0
  International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).
  Stated by the wiki itself in [references/FAQLicensing.md](references/FAQLicensing.md):
  *"The wiki content is under the Creative Commons Attribution 4.0
  International license."* This is **not** the same as SDL's library
  license (which is the [zlib license](https://www.libsdl.org/license.php));
  the wiki and the library are licensed separately.
- **Attribution:** "SDL3 Wiki" by the SDL community
  (<https://github.com/libsdl-org/sdlwiki> contributors), used under
  CC BY 4.0. Individual page contents are unmodified except that links
  pointing at upstream redirect pages have been retargeted at the redirect
  destination. The only additions in this skill are this `SKILL.md`,
  `PAGE_INDEX.md`, `API_INDEX.md`, and `UPDATING.md`, which are derivative
  organizational material released under the same CC BY 4.0 terms.
- **Pages mirrored:** 2,371
- **API symbols indexed:** 4,119 (functions, structs, enums, enumerator
  values, macros, datatypes)

## How to use this skill

1. **Don't guess.** SDL3 renamed and reshaped a lot of SDL2 surface area
   (e.g. `SDL_RWops` → `SDL_IOStream`, `SDL_GetWindowSize` semantics, the
   whole new `SDL_gpu.h` / `SDL_camera.h` / `SDL_storage.h` subsystems).
   When in doubt, look the symbol up here before writing code.
2. **Pick the right entry point** from the TOC below:
   - Need a specific function/struct/enum? → [API Symbol Index](API_INDEX.md)
   - Browsing by subsystem (audio, video, GPU, input…)? →
     [API by Category](references/APIByCategory.md) (the wiki's own grouped TOC)
   - Migrating from SDL2? → [README-migration](references/README-migration.md)
     and [SDL12MigrationGuide](references/SDL12MigrationGuide.md)
   - Looking for any page by name? → [Full Page Index](PAGE_INDEX.md)
3. **Cross-link convention.** Inside the wiki, links like `[SDL_Foo](SDL_Foo)`
   are bare page names; in this skill they resolve to
   `references/SDL_Foo.md`. When you follow a link from a wiki page, prepend
   `references/` and append `.md` if the link doesn't already include them.
4. **Image links may be broken.** A few pages reference images that live on
   the rendered wiki only — focus on the text, which is complete.

## Top-Level Table of Contents

Each entry below points to a *sub-TOC* — typically one of the wiki's own
auto-generated `Category*` pages, which then links to every individual page
in that section. This mirrors the wiki's own navigation structure rather
than imposing a new one.

| Section | Sub-TOC | What's in it |
|---|---|---|
| **Front page** | [FrontPage](references/FrontPage.md) | Wiki landing page, top-level orientation. |
| **API by category** | [APIByCategory](references/APIByCategory.md) | Subsystem-grouped index of all SDL3 headers (Basics, Video, Input, Audio, GPU, Threads, Time, File I/O, Platform, etc.). The canonical browsing entry point. |
| **Full API listing** | [CategoryAPI](references/CategoryAPI.md) | Master index of every API symbol (alphabetic). |
| **API symbol indexes (by symbol kind)** | see [API_INDEX.md](API_INDEX.md) | Functions / Structs / Enums / Enumerator values / Macros / Datatypes — each listing every symbol of that kind, with links. |
| **Full page index** | [PAGE_INDEX.md](PAGE_INDEX.md) | Every actual wiki page (2,371 of them), grouped into Guide / Category / SDL\_\* / Integer types. |
| **Quick reference** | [QuickReference](references/QuickReference.md) | One-page cheat sheet of the entire SDL3 API. Also: [QuickReferenceNoUnicode](references/QuickReferenceNoUnicode.md). |
| **FAQs** | [FAQs](references/FAQs.md) | Hub for [FAQGeneral](references/FAQGeneral.md), [FAQDevelopment](references/FAQDevelopment.md), [FAQUsingSDL](references/FAQUsingSDL.md), [FAQLicensing](references/FAQLicensing.md), [FAQCommunities](references/FAQCommunities.md). |
| **Tutorials** | [Tutorials](references/Tutorials.md) | Curated tutorial list (most tutorials live off-wiki at examples.libsdl.org). |
| **Getting started** | [SourceCode](references/SourceCode.md) | Plus IDE/build introductions: [INTRO-cmake](references/INTRO-cmake.md), [INTRO-visualstudio](references/INTRO-visualstudio.md), [INTRO-xcode](references/INTRO-xcode.md), [INTRO-mingw](references/INTRO-mingw.md), [INTRO-androidstudio](references/INTRO-androidstudio.md), [INTRO-emscripten](references/INTRO-emscripten.md). |
| **What's new in SDL3** | [NewFeatures](references/NewFeatures.md) | High-level feature additions over SDL2. |
| **SDL2 → SDL3 migration** | [README-migration](references/README-migration.md) | Detailed migration guide. Also [SDL12MigrationGuide](references/SDL12MigrationGuide.md) for the older SDL1 → SDL2 transition (still useful context). |
| **Platform & topic READMEs** | [READMEs](references/READMEs.md) | Per-platform setup and notes (Windows, macOS, Linux, iOS, Android, Wayland, Haiku, BSD, KMS/BSD, Emscripten, GDK, RISC OS, SteamOS, PS2/PS4/PS5/PSP/Vita, N3DS, Switch, NGage, QNX, DOS, OpenXR) and topic READMEs: [main-functions](references/README-main-functions.md), [highdpi](references/README-highdpi.md), [touch](references/README-touch.md), [strings](references/README-strings.md), [versions](references/README-versions.md), [dynapi](references/README-dynapi.md), [porting](references/README-porting.md), [contributing](references/README-contributing.md), [documentation-rules](references/README-documentation-rules.md). |
| **Reference / further reading** | [Articles](references/Articles.md), [Books](references/Books.md), [LanguageBindings](references/LanguageBindings.md), [Libraries](references/Libraries.md), [SupportedPlatforms](references/README-platforms.md), [EnvironmentVariables](references/EnvironmentVariables.md), [HowToReportBugs](references/HowToReportBugs.md) | Misc reference material. |
| **Subsystem sub-TOCs** | see table below | Each SDL subsystem has its own `Category*` page that lists every function, struct, enum, and macro for that header. |

### Subsystem sub-TOCs

These are the wiki's own per-subsystem index pages. Each one is a
self-contained sub-TOC — open it to see every symbol in that subsystem
with links to the individual symbol pages.

#### Basics
- [CategoryMain](references/CategoryMain.md) — Application entry points (`SDL_main.h`)
- [CategoryInit](references/CategoryInit.md) — Initialization and shutdown (`SDL_init.h`)
- [CategoryHints](references/CategoryHints.md) — Configuration hints (`SDL_hints.h`)
- [CategoryProperties](references/CategoryProperties.md) — Object properties (`SDL_properties.h`)
- [CategoryError](references/CategoryError.md) — Error handling (`SDL_error.h`)
- [CategoryLog](references/CategoryLog.md) — Logging (`SDL_log.h`)
- [CategoryAssert](references/CategoryAssert.md) — Assertions (`SDL_assert.h`)
- [CategoryVersion](references/CategoryVersion.md) — Version querying (`SDL_version.h`)

#### Video
- [CategoryVideo](references/CategoryVideo.md) — Display and window management (`SDL_video.h`)
- [CategoryRender](references/CategoryRender.md) — 2D accelerated rendering (`SDL_render.h`)
- [CategoryPixels](references/CategoryPixels.md) — Pixel formats (`SDL_pixels.h`)
- [CategoryBlendmode](references/CategoryBlendmode.md) — Blend modes (`SDL_blendmode.h`)
- [CategoryRect](references/CategoryRect.md) — Rectangle math (`SDL_rect.h`)
- [CategorySurface](references/CategorySurface.md) — Software surfaces (`SDL_surface.h`)
- [CategoryClipboard](references/CategoryClipboard.md) — Clipboard (`SDL_clipboard.h`)
- [CategoryVulkan](references/CategoryVulkan.md) — Vulkan integration (`SDL_vulkan.h`)
- [CategoryMetal](references/CategoryMetal.md) — Metal integration (`SDL_metal.h`)
- [CategoryOpenXR](references/CategoryOpenXR.md) — OpenXR integration (`SDL_openxr.h`)
- [CategoryCamera](references/CategoryCamera.md) — Camera capture (`SDL_camera.h`)

#### Input
- [CategoryEvents](references/CategoryEvents.md) — Event handling (`SDL_events.h`)
- [CategoryKeyboard](references/CategoryKeyboard.md) — Keyboard (`SDL_keyboard.h`)
- [CategoryKeycode](references/CategoryKeycode.md) — Keycodes (`SDL_keycode.h`)
- [CategoryScancode](references/CategoryScancode.md) — Scancodes (`SDL_scancode.h`)
- [CategoryMouse](references/CategoryMouse.md) — Mouse (`SDL_mouse.h`)
- [CategoryJoystick](references/CategoryJoystick.md) — Joystick (`SDL_joystick.h`)
- [CategoryGamepad](references/CategoryGamepad.md) — Gamepad (`SDL_gamepad.h`)
- [CategoryTouch](references/CategoryTouch.md) — Touch (`SDL_touch.h`)
- [CategoryPen](references/CategoryPen.md) — Pen / stylus (`SDL_pen.h`)
- [CategorySensor](references/CategorySensor.md) — Sensors (`SDL_sensor.h`)
- [CategoryHIDAPI](references/CategoryHIDAPI.md) — Raw HID API (`SDL_hidapi.h`)
- [CategoryHaptic](references/CategoryHaptic.md) — Force feedback (`SDL_haptic.h`)
- [CategoryGameController](references/CategoryGameController.md) — Legacy game controller (kept for reference)

#### Audio
- [CategoryAudio](references/CategoryAudio.md) — Audio playback, recording, mixing (`SDL_audio.h`)

#### GPU
- [CategoryGPU](references/CategoryGPU.md) — 3D rendering and GPU compute (`SDL_gpu.h`)

#### Threads / Time
- [CategoryThread](references/CategoryThread.md) — Thread management (`SDL_thread.h`)
- [CategoryMutex](references/CategoryMutex.md) — Synchronization primitives (`SDL_mutex.h`)
- [CategoryAtomic](references/CategoryAtomic.md) — Atomic operations (`SDL_atomic.h`)
- [CategoryTimer](references/CategoryTimer.md) — Timers (`SDL_timer.h`)
- [CategoryTime](references/CategoryTime.md) — Date and time (`SDL_time.h`)

#### File and I/O
- [CategoryFilesystem](references/CategoryFilesystem.md) — Filesystem (`SDL_filesystem.h`)
- [CategoryStorage](references/CategoryStorage.md) — Storage abstraction (`SDL_storage.h`)
- [CategoryIOStream](references/CategoryIOStream.md) — I/O streams (`SDL_iostream.h`)
- [CategoryAsyncIO](references/CategoryAsyncIO.md) — Async I/O (`SDL_asyncio.h`)

#### Platform / CPU
- [CategoryPlatform](references/CategoryPlatform.md) — Platform detection (`SDL_platform.h`)
- [CategoryCPUInfo](references/CategoryCPUInfo.md) — CPU feature detection (`SDL_cpuinfo.h`)
- [CategoryIntrinsics](references/CategoryIntrinsics.md) — Compiler intrinsics (`SDL_intrin.h`)
- [CategoryEndian](references/CategoryEndian.md) — Byte order / swap (`SDL_endian.h`)
- [CategoryBits](references/CategoryBits.md) — Bit manipulation (`SDL_bits.h`)

#### Additional
- [CategorySharedObject](references/CategorySharedObject.md) — DLL / shared object loading (`SDL_loadso.h`)
- [CategoryProcess](references/CategoryProcess.md) — Process control (`SDL_process.h`)
- [CategoryPower](references/CategoryPower.md) — Power management (`SDL_power.h`)
- [CategoryMessagebox](references/CategoryMessagebox.md) — Message boxes (`SDL_messagebox.h`)
- [CategoryDialog](references/CategoryDialog.md) — File dialogs (`SDL_dialog.h`)
- [CategoryTray](references/CategoryTray.md) — System tray (`SDL_tray.h`)
- [CategoryLocale](references/CategoryLocale.md) — Locale info (`SDL_locale.h`)
- [CategorySystem](references/CategorySystem.md) — Platform-specific extras (`SDL_system.h`)
- [CategoryStdinc](references/CategoryStdinc.md) — Standard library replacements (`SDL_stdinc.h`)
- [CategoryGUID](references/CategoryGUID.md) — GUIDs (`SDL_guid.h`)
- [CategoryMisc](references/CategoryMisc.md) — Miscellaneous (`SDL_misc.h`)

#### Symbol-kind indexes (across all subsystems)
- [CategoryAPI](references/CategoryAPI.md) — Every API symbol, alphabetic.
- [CategoryAPIFunction](references/CategoryAPIFunction.md) — All functions (1,305).
- [CategoryAPIStruct](references/CategoryAPIStruct.md) — All structs (121).
- [CategoryAPIEnum](references/CategoryAPIEnum.md) — All enum types (95).
- [CategoryAPIEnumerators](references/CategoryAPIEnumerators.md) — All enumerator values (1,144).
- [CategoryAPIMacro](references/CategoryAPIMacro.md) — All preprocessor macros (1,317).
- [CategoryAPIDatatype](references/CategoryAPIDatatype.md) — All typedefs / datatypes (137).
- [CategoryAPICategory](references/CategoryAPICategory.md) — Index of category pages.

## Repository layout

```
sdl3-wiki/
├── SKILL.md          ← this file (top-level TOC)
├── PAGE_INDEX.md     ← every wiki page, grouped alphabetically
├── API_INDEX.md      ← every API symbol, grouped by kind
├── UPDATING.md       ← maintainer notes: snapshot, refresh procedure
└── references/       ← wiki's SDL3/ tree, with redirect pages removed
    ├── FrontPage.md
    ├── APIByCategory.md
    ├── Category*.md          ← per-subsystem and per-symbol-kind sub-TOCs (70 files)
    ├── SDL_*.md              ← one page per documented API symbol (2,222 files)
    ├── README-*.md           ← platform and topic READMEs (36 files)
    └── (FAQ, Tutorials, Articles, intro guides, …)
```

---

For maintainers: snapshot provenance, reduction stats, and the procedure for
refreshing `references/` from upstream live in [UPDATING.md](UPDATING.md).
