#!/usr/bin/env python3
"""Entrypoint for the 20 November 2026 front page.

Stdlib only: the grader runs Python 3.13 with no third-party packages and
no network, so this program only copies the pre-rendered entry.png into the
output directory. The image itself was rendered locally during the build
(see render_image.py); the grader never needs any extra package.
"""
import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pick_output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir and os.path.isdir(env_dir):
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return "."


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    dest_dir = pick_output_dir()
    dest = os.path.join(dest_dir, "entry.png")
    if os.path.abspath(dest) == os.path.abspath(source):
        print("entry.png already in place:", dest)
        print("sha256:", sha256_of(source))
        return 0
    shutil.copyfile(source, dest)
    source_hash = sha256_of(source)
    dest_hash = sha256_of(dest)
    if dest_hash != source_hash:
        print("error: copied file hash mismatch", file=sys.stderr)
        return 1
    print("wrote:", dest)
    print("bytes:", os.path.getsize(dest))
    print("sha256:", dest_hash)
    return 0


if __name__ == "__main__":
    sys.exit(main())
