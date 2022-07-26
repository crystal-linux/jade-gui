# timezone_screen.py

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

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/timezone_screen.ui')
class TimezoneScreen(Adw.Bin):
    __gtype_name__ = 'TimezoneScreen'

    event_controller = Gtk.EventControllerKey.new()

    ### Page and widgets on timezone screen
    list_timezones = Gtk.Template.Child()
    timezone_entry_search = Gtk.Template.Child()
    timezone_search = Gtk.Template.Child()

    chosen_timezone = None
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page

        self.event_controller.connect("key-released", self.search_timezones)
        self.timezone_entry_search.add_controller(self.event_controller)
        self.list_timezones.connect("row-selected", self.selected_timezone)

    def selected_timezone(self, widget, row):
            print(row)
            if row is not None or row is not self.timezone_search:
                print(row.get_title())
                self.chosen_timezone = row
                self.carousel_next()
            else:
                print("row is none!!")

    def carousel_next(self):
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)

    def search_timezones(self, *args):
        terms = self.timezone_entry_search.get_text()
        self.list_timezones.set_filter_func(self.filter_timezones, terms)

    @staticmethod
    def filter_timezones(row, terms=None):
        try:
            text = row.get_title()
            text = text.lower() + row.get_subtitle().lower()
            if terms.lower() in text:
                return True
        except:
            return True
        return False
