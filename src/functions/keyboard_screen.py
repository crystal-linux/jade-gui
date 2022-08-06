# keyboard_Screen.py

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


from jade_gui.locales.locales_list import locations
from jade_gui.widgets.variant import KeyboardVariant
from gi.repository import Gtk, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/keyboard_screen.ui')
class KeyboardScreen(Adw.Bin):
    __gtype_name__ = 'KeyboardScreen'

    next_page_button = Gtk.Template.Child()
    layout_list = Gtk.Template.Child()

    layout = None
    variant = ""
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page
        self.next_page_button.connect("clicked", self.carousel_next)

    def carousel_next(self, widget=None):
        self.window.set_previous_page(self.window.timezone_screen)
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)

