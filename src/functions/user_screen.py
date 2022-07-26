# user_screen.py

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


from gi.repository import Gtk, Adw
from gettext import gettext as _
import re, subprocess

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/user_screen.ui')
class UserScreen(Adw.Bin):
    __gtype_name__ = "UserScreen"

    username_entry = Gtk.Template.Child()
    password_entry = Gtk.Template.Child()
    password_confirmation = Gtk.Template.Child()
    enable_sudo_switch = Gtk.Template.Child()
    enable_root_switch = Gtk.Template.Child()
    next_page_button = Gtk.Template.Child()

    username = ""
    sudo_enabled = True
    root_enabled = True
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page
        self.sudo_enabled = True
        self.root_enabled = True
        self.enable_root_switch.set_active(self.root_enabled)
        self.enable_sudo_switch.set_active(self.sudo_enabled)
        self.username_entry.connect('changed', self.username_passes_regex)
        self.enable_root_switch.connect('state-set', self.enable_root_user)
        self.enable_sudo_switch.connect('state-set', self.enable_sudo)
        self.password_entry.connect('changed', self.verify_password)
        self.password_confirmation.connect('changed', self.verify_password)
        self.next_page_button.connect('clicked', self.carousel_next)

    def username_passes_regex(self, widget):
        input = self.username_entry.get_text()
        print(input)
        if not re.search("^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)$", input):
            print("Invalid username!")
            self.username_entry.add_css_class('error')
            self.next_page.set_sensitive(False)
        else:
            print("Valid username!")
            self.username_entry.remove_css_class('error')
            self.next_page.set_sensitive(True)
            self.username = input

    def enable_root_user(self, widget, switch_state):
        print("root")
        print(self.root_enabled)
        print(switch_state)
        if switch_state == False and not self.sudo_enabled:
            self.root_enabled = switch_state
            self.sudo_enabled = not switch_state
            self.enable_sudo_switch.set_active(not switch_state)
        else:
            self.root_enabled = switch_state



    def enable_sudo(self, widget, switch_state):
        print("sudo")
        print(self.root_enabled)
        print(switch_state)
        if switch_state == False and not self.root_enabled:
            self.sudo_enabled = switch_state
            self.root_enabled = not switch_state
            self.enable_root_switch.set_active(not switch_state)
        else:
            self.sudo_enabled = switch_state

    def verify_password(self, widget):
        if self.password_entry.get_text() == self.password_confirmation.get_text():
            self.next_page.set_sensitive(True)
            self.password_confirmation.remove_css_class('error')
            self.password = self.encrypt_password(self.password_entry.get_text())
        else:
            self.next_page.set_sensitive(False)
            self.password_confirmation.add_css_class('error')

    def encrypt_password(self, password):
        command=subprocess.run(["openssl", "passwd", "-crypt", password], capture_output=True)
        password_encrypted=command.stdout.decode('utf-8').strip('\n')
        return password_encrypted


    def carousel_next(self, widget):
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)
