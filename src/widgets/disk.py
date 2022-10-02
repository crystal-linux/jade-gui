# disk.py

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

@Gtk.Template(resource_path='/al/getcryst/jadegui/widgets/disk.ui')
class DiskEntry(Adw.ActionRow):
    __gtype_name__ = 'DiskEntry'

    size_label = Gtk.Template.Child()
    select_button = Gtk.Template.Child()

    def __init__(self, window, disk, disk_size, disk_type, button_group, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.disk = disk
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.set_title(disk[5:])
        self.set_subtitle(disk_type)
        self.size_label.set_label("Disk Size: "+disk_size)
        if button_group is not None:
            self.select_button.set_group(button_group)
        else:
            self.select_button.set_active(True)
        self.select_button.connect("toggled", self.toggled_cb)

    def toggled_cb(self, check_button):
        row = check_button.get_ancestor(Gtk.ListBoxRow)
        if check_button.props.active and len(self.window.available_disks) != 1:
            row.emit('activate')
        self.window.partition_screen.selected_partition = self
        self.window.partition_screen.next_page_button.set_sensitive(True)



