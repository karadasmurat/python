#!/bin/bash
osascript <<EOF
tell application "System Events"
    tell application process "Terminal"
        keystroke "f" using {control down, command down}
    end tell
end tell
EOF
cd /Users/mk/dev/python/python_basics/games
python hangman.py
