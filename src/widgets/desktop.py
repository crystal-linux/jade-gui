# desktop.py

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

@Gtk.Template(resource_path='/al/getcryst/jadegui/widgets/desktop.ui')
class DesktopEntry(Adw.ActionRow):
    __gtype_name__ = 'DesktopEntry'

    select_button = Gtk.Template.Child()

    def __init__(self, window, desktop, button_group, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.set_title(desktop)
        self.select_button.set_group(button_group)
        self.select_button.connect("toggled", self.toggled_cb)

    def toggled_cb(self, check_button):
        if check_button.props.active:
            row = check_button.get_ancestor(Gtk.ListBoxRow)
            row.activate()
            self.selected_partition = row.get_title()

