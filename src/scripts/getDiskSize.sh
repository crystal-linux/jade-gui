#!/usr/bin/bash
flatpak-spawn --host lsblk -pdbo SIZE $1 | grep -v SIZE