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

    layout_event_controller = Gtk.EventControllerKey.new()
    variant_event_controller = Gtk.EventControllerKey.new()

    keyboard_carousel = Gtk.Template.Child()
    list_keyboard_layouts = Gtk.Template.Child()
    list_keyboard_variants = Gtk.Template.Child()
    keyboard_layouts = Gtk.Template.Child()
    keyboard_variants = Gtk.Template.Child()
    layout_search = Gtk.Template.Child()
    layout_entry_search = Gtk.Template.Child()
    variant_search = Gtk.Template.Child()
    variant_entry_search = Gtk.Template.Child()

    layout = None
    variant = ""
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page
        self.list_keyboard_layouts.connect("row-selected", self.selected_layout)
        self.list_keyboard_variants.connect("row-selected", self.selected_variant)
        self.layout_event_controller.connect("key-released", self.search_layouts)
        self.variant_event_controller.connect("key-released", self.search_variants)
        self.layout_entry_search.add_controller(self.layout_event_controller)
        self.variant_entry_search.add_controller(self.variant_event_controller)

    def search_layouts(self, *args):
        terms = self.layout_entry_search.get_text()
        self.list_keyboard_layouts.set_filter_func(self.filter_text, terms)

    def search_variants(self, *args):
        print("in variant")
        terms = self.variant_entry_search.get_text()
        self.list_keyboard_variants.set_filter_func(self.filter_text, terms)

    def selected_layout(self, widget, row, *args):
        if row is not None or row is not self.layout_entry_search:
            if self.layout is not None:
                for n in range(len(self.layout.variants)):
                    print(n)
                    print(self.list_keyboard_variants.get_row_at_index(n))
                    if self.list_keyboard_variants.get_row_at_index(n) is not None:
                        self.list_keyboard_variants.remove(self.list_keyboard_variants.get_row_at_index(n))
            self.layout = row
            for variant in row.variants:
                self.list_keyboard_variants.append(KeyboardVariant(window=self.window, country=row.country, country_shorthand=row.country_shorthand, variant=variant, *args))
            self.keyboard_carousel.scroll_to(self.keyboard_variants, True)
        else:
            print("row is none!! layout")

    def selected_variant(self, widget, row):
        if row is not None or row is not self.variant_entry_search:
            self.variant = row
            self.carousel_next()
        else:
            print("row is none!! variant")

    def carousel_next(self):
        if self.move_to_summary:
            self.window.summary_screen.initialize()
            self.carousel.scroll_to(self.window.summary_screen, True)
        else:
            self.carousel.scroll_to(self.next_page, True)

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary=True
        self.carousel.scroll_to(self.next_page, True)

    @staticmethod
    def filter_text(row, terms=None):
        try:
            text = row.get_title()
            text = text.lower() + row.get_subtitle().lower()
            if terms.lower() in text:
                return True
        except:
            print("exception")
            return True
        return False
