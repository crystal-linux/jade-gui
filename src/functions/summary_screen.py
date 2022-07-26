# summary_screen.py

#
# Copyright 2022 user

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

import subprocess
from jade_gui.utils import disks
from jade_gui.classes.install_prefs import InstallPrefs
from jade_gui.utils.threading import RunAsync
from gi.repository import Gtk, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/summary_screen.ui')
class SummaryScreen(Adw.Bin):
    __gtype_name__ = "SummaryScreen"

    next_page_button = Gtk.Template.Child()

    timezone_label = Gtk.Template.Child()
    timezone_button = Gtk.Template.Child()
    keyboard_label = Gtk.Template.Child()
    keyboard_button = Gtk.Template.Child()
    username_label = Gtk.Template.Child()
    username_button = Gtk.Template.Child()
    sudo_label = Gtk.Template.Child()
    sudo_button = Gtk.Template.Child()
    root_label = Gtk.Template.Child()
    root_button = Gtk.Template.Child()
    desktop_label = Gtk.Template.Child()
    desktop_button = Gtk.Template.Child()
    partition_label = Gtk.Template.Child()
    partition_button = Gtk.Template.Child()
    uefi_label = Gtk.Template.Child()
    ipv_label = Gtk.Template.Child()
    ipv_button = Gtk.Template.Child()
    timeshift_label = Gtk.Template.Child()
    timeshift_button = Gtk.Template.Child()
    #unakite_label = Gtk.Template.Child()

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.main_carousel = main_carousel
        self.next_page = next_page
        self.next_page_button.connect("clicked", self.carousel_next)

    def carousel_next(self, widget):
        self.main_carousel.scroll_to(self.next_page, True)
        #(self.window.installer_screen.install())
        subprocess.run(["bash", "-c", "bash -- /app/share/jade_gui/jade_gui/scripts/savePrefs.sh '"+self.installprefs.generate_json()+"'"], capture_output=False)
        RunAsync(self.window.installer_screen.install)

    def initialize(self):
        self.timezone_button.connect("clicked", self.window.nextPage)
        self.keyboard_button.connect("clicked", self.window.timezone_screen.carousel_next_summary)
        self.username_button.connect("clicked", self.window.keyboard_screen.carousel_next_summary)
        self.sudo_button.connect("clicked", self.window.keyboard_screen.carousel_next_summary)
        self.root_button.connect("clicked", self.window.keyboard_screen.carousel_next_summary)
        self.desktop_button.connect("clicked", self.window.user_screen.carousel_next_summary)
        self.partition_button.connect("clicked", self.window.desktop_screen.carousel_next_summary)
        self.ipv_button.connect("clicked", self.window.desktop_screen.carousel_next_summary)
        self.timeshift_button.connect("clicked", self.window.desktop_screen.carousel_next_summary)

        self.timezone_label.set_title(self.window.timezone_screen.chosen_timezone.region+"/"+self.window.timezone_screen.chosen_timezone.location)
        self.timezone_label.set_subtitle(self.window.timezone_screen.chosen_timezone.locale)

        self.keyboard_label.set_title(self.window.keyboard_screen.layout.country)
        self.keyboard_label.set_subtitle(self.window.keyboard_screen.variant.variant)

        self.username_label.set_title(self.window.user_screen.username)
        self.sudo_label.set_title("sudo enabled" if self.window.user_screen.sudo_enabled else "sudo disabled")
        self.root_label.set_title("root enabled" if self.window.user_screen.root_enabled else "root disabled")

        self.desktop_label.set_title(self.window.desktop_screen.chosen_desktop)

        self.partition_label.set_title(self.window.partition_screen.selected_partition.disk)
        self.partition_label.set_subtitle(self.window.partition_screen.selected_partition.disk_size)
        self.uefi_label.set_title("UEFI" if disks.get_uefi() else "Legacy BIOS")

        self.ipv_label.set_title("ipv6 enabled" if self.window.misc_screen.ipv_enabled else "ipv6 disabled")
        self.timeshift_label.set_title("timeshift enabled" if self.window.misc_screen.timeshift_enabled else "timeshift disabled")
        #self.theme_label.set_title("Crystal theming enabled" if self.window.misc_screen.crystal_theming_enabled else "Crystal theming disabled")
        #self.unakite_label.set_title("Unakite enabled "+"enabled" if self.window.misc_screen.)
        
        self.installprefs = InstallPrefs(
            timezone=self.window.timezone_screen.chosen_timezone,
            layout=self.window.keyboard_screen.layout,
            variant=self.window.keyboard_screen.variant,
            username=self.window.user_screen.username,
            password=self.window.user_screen.password,
            enable_sudo=self.window.user_screen.sudo_enabled,
            disk=self.window.partition_screen.selected_partition,
            hostname=self.window.misc_screen.hostname,
            ipv_enabled=self.window.misc_screen.ipv_enabled,
            timeshift_enable=self.window.misc_screen.timeshift_enabled,
            desktop=self.window.desktop_screen.chosen_desktop,
        )
        
