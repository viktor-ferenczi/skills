---
name: recursive-language-model
description: Recursive Language Model workflow for processing documents that exceed context window limits. Uses a persistent Python REPL and subordinate agents to chunk, search, and analyze large context files.
license: MIT
---

# RLM (Recursive Language Model)

Process arbitrarily long documents by treating them as an external environment: keep the document in a
persistent Python REPL, search and chunk it there, and recursively delegate chunk-level analysis to
subordinate agents. Never paste large content into the main conversation.

All paths below are relative to this skill's directory. Requires Python 3.8+ and an agentic harness with
code execution and subordinate agents.

## Workflow

1. **Load the document** into the REPL:
   `python3 scripts/rlm_repl.py init <path/to/context.txt>` (verify with `... status`)
2. **Scout** the content: `python3 scripts/rlm_repl.py exec -c 'print(peek(0, 3000))'`
   and locate relevant sections with `grep(pattern)` before reading anything in bulk.
3. **Chunk** if needed: `python3 scripts/rlm_repl.py exec -c 'print("\n".join(write_chunks("./rlm_chunks", size=200000)))'`
4. **Delegate** each relevant chunk to a subordinate agent using the prompt profile in
   [rlm-subcall.md](rlm-subcall.md), passing the query and the chunk file path. Prefer JSON-structured replies.
5. **Synthesize** the sub-agent results in the main conversation and answer.
6. **Clean up**: `python3 scripts/rlm_repl.py reset`

## Reference

- [README.md](README.md) — full REPL command and helper-function reference, architecture, compatible harnesses.
- [EXAMPLE.md](EXAMPLE.md) — complete worked example on a large document.
- [rlm-subcall.md](rlm-subcall.md) — subordinate agent prompt profile.
- [scripts/rlm_repl.py](scripts/rlm_repl.py) — the persistent REPL (state stored locally via pickle; context size limited by memory).
