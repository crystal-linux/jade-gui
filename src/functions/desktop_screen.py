# desktop_screen.py

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

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/desktop_screen.ui')
class DesktopScreen(Adw.Bin):
    __gtype_name__ = 'DesktopScreen'

    list_desktops = Gtk.Template.Child()
    next_page_button = Gtk.Template.Child()

    chosen_desktop = ""
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page

        self.list_desktops.connect("row-selected", self.selected_desktop)
        self.next_page_button.connect("clicked", self.carousel_next)

    def carousel_next(self, widget):
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)

    def selected_desktop(self, widget, row):
            if row is not None:
                print(row.get_title())
                self.chosen_desktop = row.get_title()
                row.select_button.set_active(True)
            else:
                print("row is none!!")
