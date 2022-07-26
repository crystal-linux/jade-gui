#!/usr/bin/bash
flatpak-spawn --host lsblk -pdbo MODEL $1 | grep -v MODEL