#!/usr/bin/bash
flatpak-spawn --host lsblk -d -o rota $1 | grep -v ROTA