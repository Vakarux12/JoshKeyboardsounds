import os
import sys
import platform
import webbrowser
import tkinter as tk
from tkinter import messagebox
import requests
import pygame
from pynput import keyboard

# Initialize mixer
pygame.mixer.init()

# 🧠 Detect base path depending on if script is frozen (compiled with PyInstaller)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Temporary folder used by PyInstaller
else:
    base_path = os.path.dirname(__file__)  # Normal script path

# Set path to sounds folder (works for both .py and .exe)
AUDIO_DIR = os.path.join(base_path, "sounds")

# Read version from file alongside the script
VERSION_FILE = os.path.join(base_path, "VERSION")
try:
    with open(VERSION_FILE, "r") as vf:
        __version__ = vf.read().strip()
except Exception:
    __version__ = "0.0.0"

UPDATE_URL = "https://raw.githubusercontent.com/Vakarux12/JoshKeyboardsounds/main/VERSION"

# Special keys mapping to filenames
special_keys = {
    "\\": "backslash",
    "/": "frontslash",
    ":": "colon",
    ";": "semicolon",
    #"'": "quote",
    "\"": "quote",
    ".": "period",
    "?": "questionmark",
    " ": "spacebar",
    "space": "spacebar",
    "enter": "enter",
    "\r": "enter",
    "\n": "enter",
    "backspace": "backspace",
    "\b": "backspace",
    "esc": None,
    #"tab": "tab",  # Only works if you have tab.mp3
}

# Load all sounds into memory as Sound objects
sound_map = {}
for file in os.listdir(AUDIO_DIR):
    if file.endswith(".mp3"):
        keyname = file[:-4].lower()
        full_path = os.path.join(AUDIO_DIR, file)
        try:
            sound_map[keyname] = pygame.mixer.Sound(full_path)
        except pygame.error as e:
            print(f"Failed to load {file}: {e}")

def check_for_updates():
    """Check GitHub for a newer VERSION file and prompt the user."""
    try:
        resp = requests.get(UPDATE_URL, timeout=5)
        if resp.status_code == 200:
            latest = resp.text.strip()
            if latest != __version__:
                root = tk.Tk()
                root.withdraw()
                if messagebox.askyesno(
                    "Update Available",
                    f"Version {latest} is available. Open download page?",
                ):
                    webbrowser.open(
                        "https://github.com/Vakarux12/JoshKeyboardsounds"
                    )
                root.destroy()
    except Exception:
        pass

def play_key_sound(key):
    try:
        if hasattr(key, 'char') and key.char:
            key_str = key.char.lower()
        else:
            key_str = str(key).replace('Key.', '').lower()
    except:
        return

    mapped = special_keys.get(key_str, key_str)
    if mapped in sound_map:
        sound_map[mapped].play()  # Allows overlapping

def on_press(key):
    play_key_sound(key)

def main():
    check_for_updates()
    print("🔊 Soundboard running in background. Press ESC to exit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
