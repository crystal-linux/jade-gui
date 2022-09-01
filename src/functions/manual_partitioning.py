# partition_screen.py

#
# Copyright 2022 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only.
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

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/manual_partitioning.ui')
class ManualPartitionScreen(Adw.Bin):
    __gtype_name__ = "ManualPartitionScreen"

    open_fdisk = Gtk.Template.Child()
    open_gparted = Gtk.Template.Child()
    partition_list = Gtk.Template.Child()
    #next_page_button = Gtk.Template.Child()
    #custom_partition = Gtk.Template.Child()

    selected_partition = None
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page
      #  self.next_page_button.connect("clicked", self.carousel_next)

    def carousel_next(self, widget):
        self.window.set_previous_page(self.window.misc_screen)
        self.window.summary_screen.initialize()
        self.carousel.scroll_to(self.next_page, True)
