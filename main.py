"""Kingdom Come 2 Desktop — Local Windows and macOS helper for Kingdom Come 2 data paths, config and export caches, and export folders."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='kingdom_come_2_desktop',
        description='Local Windows and macOS helper for Kingdom Come 2 data paths, config and export caches, and export folders.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Kingdom Come 2 Desktop')
    print('Find the Kingdom Come 2 folder fast and keep a local spare.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
