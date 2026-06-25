---
name: bizzfactory-document-downloader
description: Download all of a client's documents from the Bizz Factory portal (portal.bizzfactory.se) into a local folder tree that mirrors the page, without converting files or causing any side effects. Use when the user wants to back up, archive, or bulk-download documents from their BizzFactory / Bizz Factory portal account, or mentions a portal.bizzfactory.se/documents/<uuid> URL.
---

# BizzFactory Document Downloader

Downloads every document for a client from the Bizz Factory accounting portal into a
local directory tree that mirrors the folder structure shown on the page. Files (PDFs,
SIE `.se` exports, etc.) are saved **as-is — no conversion**.

## Read-only guarantee (no side effects)

The bundled script issues **only HTTP GET** requests against two endpoints:

- `GET /api/v1/documents/{clientUuid}` — the folder tree as JSON
- `GET /api/v1/documents/{clientUuid}/documents/{fileUuid}/download` — one file's bytes

It never touches any mutating endpoint (mark-as-read, mark-as-handled, upload, move,
delete, restore, empty-trash). **Downloading does not change a file's unread status** —
"read" is set by a separate directory-level endpoint the script deliberately avoids. The
only unavoidable server-side traces are the session keep-alive timestamp and any
download-audit entry inherent to fetching a file.

## Step 1 — Get the portal URL

Navigate to the client's documents page in your browser. The URL looks like:

```
https://portal.bizzfactory.se/documents/<clientUuid>
```

`<clientUuid>` is a UUID identifying the client (company). The script extracts it from
the URL automatically; you can also pass the bare UUID.

## Step 2 — Copy the two session cookies

You need two cookies for the `portal.bizzfactory.se` domain:

| Cookie | What it is |
| --- | --- |
| `Agency` | Agency/tenant id (a UUID) |
| `PLAY_SESSION` | The signed Play Framework session (a long JWT-like string) |

These expire and the session is rolling, so copy them from a **freshly loaded** portal
page just before running.

### Chrome / Edge / Brave (Chromium)
1. Open the portal page, press **F12** → **Application** tab.
2. Left sidebar → **Storage** → **Cookies** → `https://portal.bizzfactory.se`.
3. Copy the **Value** column for the `Agency` and `PLAY_SESSION` rows.

### Firefox
1. Open the portal page, press **F12** → **Storage** tab (enable it in the `»` overflow
   menu if hidden).
2. **Cookies** → `https://portal.bizzfactory.se`.
3. Copy the **Value** of `Agency` and `PLAY_SESSION`.

### Safari
1. Enable the Develop menu: **Safari → Settings → Advanced → "Show features for web
   developers"**.
2. On the portal page: **Develop → Show Web Inspector** (or ⌥⌘I) → **Storage** tab.
3. **Cookies** → `portal.bizzfactory.se` → copy `Agency` and `PLAY_SESSION` values.

### Shortcut (any browser): Copy as cURL
In **DevTools → Network**, reload the page, right-click any request to
`portal.bizzfactory.se` → **Copy → Copy as cURL**. The `Cookie:` header in the result
contains both `Agency=...` and `PLAY_SESSION=...`.

## Step 3 — Run the downloader

The script writes into a subdirectory of the **current working directory** (your project
folder). Default subdir name: **`BizzFactoryDocs`**.

```bash
python3 scripts/download.py \
  --url "https://portal.bizzfactory.se/documents/<clientUuid>" \
  --agency "<Agency cookie value>" \
  --session "<PLAY_SESSION cookie value>" \
  --outdir BizzFactoryDocs
```

Credentials can also come from the environment instead of flags (safer — keeps secrets
out of shell history):

```bash
export BIZZ_AGENCY="<Agency cookie value>"
export BIZZ_SESSION="<PLAY_SESSION cookie value>"
python3 scripts/download.py --url "https://portal.bizzfactory.se/documents/<clientUuid>"
```

Requires Python 3.11+ (standard library only — no `pip install`).

## Output

```
BizzFactoryDocs/
├─ _manifest.json          # path, uuid, byte size, mimeType for every file
└─ <Root folder>/...       # full tree, including empty folders, mirroring the page
```

The run prints each downloaded file and a final summary
(`Directories created`, `Files downloaded`, total bytes). Existing files are
overwritten; the run is idempotent and safe to re-run.

## Verifying the result

```bash
cd BizzFactoryDocs
find . -type f ! -name _manifest.json -size 0           # should print nothing
grep -rlI '<!DOCTYPE html' . 2>/dev/null                # no HTML error pages
find . -type f ! -name _manifest.json | wc -l           # file count
```

## Troubleshooting

- **HTTP 401/403** — the session expired or the cookies are wrong. Reload the portal
  page and re-copy `Agency` and `PLAY_SESSION`.
- **Empty / partial tree** — confirm the client UUID in the URL matches the client whose
  documents you intend to download (the portal can hold several clients).
- **Garbled filenames** — names are taken verbatim from the portal and only `/` and `\`
  are replaced with `_`; Swedish characters (å ä ö) are preserved.

## Script

The downloader lives at [`scripts/download.py`](scripts/download.py) and is fully
self-contained (stdlib only, Python 3.11 compatible).
