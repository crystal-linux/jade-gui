#!/usr/bin/bash
echo "Running reflector to sort for fastest mirrors"
flatpak-spawn --host pkexec reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorlist
flatpak-spawn --host pkexec jade config ~/.config/jade.json
