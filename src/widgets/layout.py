# layout.py

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

@Gtk.Template(resource_path='/al/getcryst/jadegui/widgets/layout.ui')
class KeyboardLayout(Adw.ActionRow):
    __gtype_name__ = 'KeyboardLayout'

    variants=[]

    def __init__(self, window, country, country_shorthand, variants, application, **kwargs):
        super().__init__(**kwargs)

        self.country = country
        self.country_shorthand = country_shorthand

        self.set_title(country)
        self.set_subtitle(country_shorthand)
        self.variants = variants

