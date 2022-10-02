# language_screen.py

#
# Copyright 2022 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, only
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

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/language_screen.ui')
class LanguageScreen(Adw.Bin):
    __gtype_name__ = 'LanguageScreen'

    event_controller = Gtk.EventControllerKey.new()

    ### Page and widgets on timezone screen
    list_languages = Gtk.Template.Child()
    language_entry_search = Gtk.Template.Child()
    language_search = Gtk.Template.Child()
    next_page_button = Gtk.Template.Child()

    chosen_language = None
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page

        self.event_controller.connect("key-released", self.search_languages())
        self.language_entry_search.add_controller(self.event_controller)
        self.list_languages.connect("row-selected", self.selected_language)
        self.next_page_button.connect("clicked", self.carousel_next)

    def selected_language(self, widget, row):
        print(row)
        if row is not None or row is not self.language_search:
            print(row.get_title())
            self.chosen_language = row
            self.next_page_button.set_sensitive(False)
        else:
            print("row is none!!")

    def carousel_next(self, widget=None):
        self.window.set_previous_page(self.window)
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)

    def search_languages(self, *args):
        terms = self.language_entry_search.get_text()
        self.list_languages.set_filter_func(self.filter_languages, terms)

    @staticmethod
    def filter_languages(row, terms=None):
        try:
            text = row.get_title()
            text = text.lower() + row.get_subtitle().lower()
            if terms.lower() in text:
                return True
        except:
            return True
        return False


