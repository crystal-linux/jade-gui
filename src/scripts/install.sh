#!/usr/bin/bash
echo "Running reflector to sort for fastest mirrors"
pkexec reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorl
pkexec jade config ~/.config/jade.json
