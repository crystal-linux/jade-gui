# variant.py

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

from gi.repository import Gtk, GLib, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/widgets/variant.ui')
class KeyboardVariant(Adw.ActionRow):
    __gtype_name__ = 'KeyboardVariant'

    select_variant = Gtk.Template.Child()

    def __init__(self, window, variant, country, country_shorthand, button_group, application, **kwargs):
        super().__init__(**kwargs)
        self.window=window
        self.variant = variant
        self.country = country
        self.country_shorthand = country_shorthand

        self.set_title(variant)
        self.set_subtitle(country+" - "+country_shorthand)
        self.select_variant.set_group(button_group)
        self.select_variant.connect("toggled", self.selected)

    def selected(self, widget):
        self.window.keyboard_screen.variant=self
        self.window.keyboard_screen.next_page_button.set_sensitive(True)


