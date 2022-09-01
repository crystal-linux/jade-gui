#!/usr/bin/bash
flatpak-spawn --host [ -d /sys/firmware/efi ] && echo UEFI || echo BIOS