#!/usr/bin/bash
flatpak-spawn --host blkid -o device | grep -v zram | grep -v loop | grep -v sr