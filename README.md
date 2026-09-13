
# Josh's Opera GX Keyboard Sounds (But Worse™)

This is a **completely useless** Python app that plays sounds from **Let's Game It Out... but cursed** mod in Opera GX based on what key you press.

Except it's even better (or worse?) – because Josh actually **announces** the correct key you press out loud (not like the actual mod, picking it randomly), using ~stolen~ extracted `.mp3` files. 🎧

> Warning: you can't close the app. There's no UI. No tray icon. No exit button.  
> To stop it you must stop the process

---

## Features

- Plays keyboard sounds **in the background**.
- Supports **special keys** like `colon`, `backslash`, and `period`.
- Works on **Windows**, **macOS**, and **Linux**.
---

## How to Use

Clone or download this repo first:

```bash
git clone https://github.com/Vakarux12/JoshKeyboardsounds.git
cd JoshKeyboardsounds
```

This program automatically checks for updates on startup and only shows a window if a newer version is found.

### Windows

```bash
pip install pygame pynput requests pyinstaller
python main.py
```

To bundle it as an `.exe` you can run `pyinstaller --onefile --noconsole --add-data "sounds;sounds" main.py`.

### Linux (Debian/Ubuntu, Arch, etc.)

Install Python 3 from your distro's package manager and then:

```bash
pip3 install pygame pynput requests
python3 main.py
```

### macOS

Install Python 3 (e.g. `brew install python`) and run:

```bash
pip3 install pygame pynput requests
python3 main.py
```
---

## Credits

* Sound files: **Let's Game It Out... but cursed** on Opera GX mods

---

## Disclaimer

This project is purely for fun.
Do not use in production (or at all).
