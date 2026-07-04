# Core Principles

- **YAGNI** (You Aren't Gonna Need It) — Don't build functionality until it is actually needed; speculative generality is waste.
- **KISS** (Keep It Simple, Stupid) — Prefer the simplest design that works; complexity must earn its place.
- **DRY** (Don't Repeat Yourself) — Every piece of knowledge should have a single authoritative representation; extract duplication, but don't unify code that merely looks similar.
- **SSOT** (Single Source of Truth) — Each fact/configuration/state lives in exactly one place; everything else derives from it.
- **Fail Fast** — Detect and report errors as early and loudly as possible instead of limping on with corrupt state.
- **Throw Early, Catch Late** — Catch an exception only where you can actually recover; otherwise let it propagate to a top-level boundary that logs it with full context. Never swallow errors silently; blanket catch-alls belong only at the top level (main loop, request handler), and even there they must log.
- **PoLA** (Principle of Least Astonishment) — Code, APIs, and UIs should behave the way their users most likely expect.
