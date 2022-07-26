# install_prefs.py
#
# Copyright 2022
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

from jade_gui.utils import disks
import json

class InstallPrefs:
    def __init__(
        self,
        timezone,
        layout,
        variant,
        username,
        password,
        enable_sudo,
        disk,
        hostname,
        ipv_enabled,
        timeshift_enable,
        desktop,
    ):
        self.timezone = timezone
        self.layout = layout
        self.variant = variant
        self.username = username
        self.password = password
        self.enable_sudo = enable_sudo
        self.disk = disk.disk
        self.hostname = hostname if len(hostname) != 0 else "crystal"
        self.ipv_enabled = ipv_enabled
        self.timeshift_enable = timeshift_enable
        self.desktop = desktop
        self.is_efi = disks.get_uefi()
        self.bootloader_type = "grub-efi" if self.is_efi else "grub-legacy"
        self.bootloader_location = "/boot/efi" if self.is_efi else self.disk

    def generate_json(self):
        prefs = {
            '"partition"': {
                '"device"': '"'+self.disk+'"',
                '"mode"': '"Auto"',
                '"efi"': self.is_efi,
                '"partitions"': [],
            },
            '"bootloader"': {
                '"type"': '"'+self.bootloader_type+'"',
                '"location"': '"'+self.bootloader_location+'"'
            },
            '"locale"': {
                '"locale"': [
                   '"'+ self.timezone.locale+'"'
                ],
                '"keymap"': '"'+self.layout.country_shorthand+'"',
                '"timezone"': '"'+self.timezone.region+"/"+self.timezone.location+'"'
            },
            '"networking"': {
                '"hostname"': '"'+self.hostname+'"',
                '"ipv6"': self.ipv_enabled
            },
            '"users"': [
                {
                    '"name"': '"'+self.username+'"',
                    '"password"': '"'+self.password+'"',
                    '"hasroot"': self.enable_sudo
                }
            ],
            '"rootpass"': '"'+self.password+'"',
            '"desktop"': '"'+self.desktop.lower()+'"',
            '"timeshift"': self.timeshift_enable,
            '"extra_packages"': [],
            '"flatpak"': True,
            '"unakite"': {
                '"enable"': False,
                '"root"': '"/dev/null"',
                '"oldroot"': '"'+self.disk+'"',
                '"efidir"': '"/dev/null"',
                '"bootdev"': '"/dev/null"'
            },
            '"kernel"': '"linux"'
        }
        return json.dumps(prefs)
