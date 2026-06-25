#!/usr/bin/env python3
"""
BizzFactory portal document downloader.

Downloads every document for a client from the Bizz Factory portal
(https://portal.bizzfactory.se) into a local directory tree that mirrors the
folder structure shown on the page. PDFs and other files are saved as-is
(no conversion).

READ-ONLY / NO SIDE EFFECTS:
    The script issues only HTTP GET requests against two endpoints:
        GET /api/v1/documents/{clientUuid}                          -> folder tree (JSON)
        GET /api/v1/documents/{clientUuid}/documents/{fileUuid}/download
    It never calls any mutating endpoint (mark-as-read, mark-as-handled,
    upload, move, delete, restore, empty-trash). Downloading does NOT change
    a file's unread status: "read" is marked by a separate directory-level
    endpoint that this script deliberately does not touch. The only server-side
    traces are the unavoidable session keep-alive timestamp and any
    download-audit log entry inherent to fetching a file.

Python 3.11 compatible. Standard library only (urllib, json, argparse).

Usage:
    python3 download.py \
        --url "https://portal.bizzfactory.se/documents/<clientUuid>" \
        --agency "<Agency cookie value>" \
        --session "<PLAY_SESSION cookie value>" \
        [--outdir BizzFactoryDocs]

The cookie values can also be supplied via the environment variables
BIZZ_AGENCY and BIZZ_SESSION instead of --agency / --session.
The output directory is created as a subdirectory of the current working
directory (the project folder) and defaults to "BizzFactoryDocs".
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = "https://portal.bizzfactory.se"
CLIENT_UUID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download all BizzFactory portal documents.")
    p.add_argument(
        "--url",
        required=True,
        help="Portal documents URL, e.g. "
        "https://portal.bizzfactory.se/documents/<clientUuid> "
        "(or just the bare client UUID).",
    )
    p.add_argument(
        "--agency",
        default=os.environ.get("BIZZ_AGENCY"),
        help="Value of the 'Agency' cookie (or set env BIZZ_AGENCY).",
    )
    p.add_argument(
        "--session",
        default=os.environ.get("BIZZ_SESSION"),
        help="Value of the 'PLAY_SESSION' cookie (or set env BIZZ_SESSION).",
    )
    p.add_argument(
        "--outdir",
        default="BizzFactoryDocs",
        help="Output subdirectory under the current folder (default: BizzFactoryDocs).",
    )
    return p.parse_args()


def client_uuid_from(url: str) -> str:
    m = CLIENT_UUID_RE.search(url)
    if not m:
        sys.exit(f"Could not find a client UUID in: {url!r}")
    return m.group(0)


def sanitize(name: str) -> str:
    name = name.replace("/", "_").replace("\\", "_").replace("\x00", "")
    name = name.strip().strip(".")
    return name or "_"


class Client:
    def __init__(self, agency: str, session: str) -> None:
        if not agency or not session:
            sys.exit(
                "Missing credentials. Provide --agency and --session "
                "(or env BIZZ_AGENCY / BIZZ_SESSION). See the skill's SKILL.md "
                "for how to copy them from your browser."
            )
        self.cookie = f"Agency={agency}; PLAY_SESSION={session}"

    def get(self, url: str) -> bytes:
        req = urllib.request.Request(
            url,
            headers={
                "Cookie": self.cookie,
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                sys.exit(
                    f"HTTP {e.code} for {url}\n"
                    "Your session is invalid or expired. Re-copy the Agency and "
                    "PLAY_SESSION cookies from a freshly loaded portal page."
                )
            raise


def main() -> None:
    args = parse_args()
    client = client_uuid_from(args.url)
    api = Client(args.agency, args.session)

    out_root = os.path.abspath(args.outdir)
    os.makedirs(out_root, exist_ok=True)

    print(f"Client UUID : {client}")
    print(f"Output dir  : {out_root}")
    print("Fetching folder tree...")
    tree = json.loads(api.get(f"{BASE}/api/v1/documents/{client}"))

    manifest: list[dict] = []
    stats = {"dirs": 0, "files": 0, "bytes": 0}
    errors: list[tuple[str, str, str]] = []

    def download_files(files: list[dict], fsdir: str, relpath: str) -> None:
        used: set[str] = set()
        for f in files:
            uuid = f["uuid"]
            fname = sanitize(f["name"])
            base, ext = os.path.splitext(fname)
            cand, i = fname, 1
            while cand.lower() in used:  # de-dup within the same folder
                cand = f"{base} ({i}){ext}"
                i += 1
            used.add(cand.lower())
            rel = os.path.join(relpath, cand)
            url = f"{BASE}/api/v1/documents/{client}/documents/{uuid}/download"
            try:
                data = api.get(url)
                with open(os.path.join(fsdir, cand), "wb") as fh:
                    fh.write(data)
                stats["files"] += 1
                stats["bytes"] += len(data)
                manifest.append(
                    {
                        "path": rel,
                        "uuid": uuid,
                        "bytes": len(data),
                        "mimeType": f.get("mimeType"),
                    }
                )
                print(f"  [{stats['files']}] {rel}  ({len(data)} B)")
            except Exception as e:  # noqa: BLE001 - report and continue
                errors.append((rel, uuid, str(e)))
                print(f"  !! FAILED {rel}: {e}", file=sys.stderr)

    def walk(dirs: list[dict], fsparent: str, relparent: str) -> None:
        for d in dirs:
            name = sanitize(d["name"])
            fsdir = os.path.join(fsparent, name)
            rel = os.path.join(relparent, name)
            os.makedirs(fsdir, exist_ok=True)
            stats["dirs"] += 1
            ch = d.get("children", {})
            download_files(ch.get("files", []), fsdir, rel)
            walk(ch.get("directories", []), fsdir, rel)

    # Root-level loose files (if any), then the directory tree.
    download_files(tree.get("files", []), out_root, "")
    walk(tree.get("directories", []), out_root, "")

    with open(os.path.join(out_root, "_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)

    print(f"\nDirectories created : {stats['dirs']}")
    print(f"Files downloaded    : {stats['files']}  ({stats['bytes']} bytes)")
    print(f"Manifest            : {os.path.join(out_root, '_manifest.json')}")
    if errors:
        print(f"ERRORS: {len(errors)}")
        for rel, uuid, msg in errors:
            print(f"  {rel} ({uuid}): {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
