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

import subprocess, shutil
from gi.repository import Gtk, Adw
from gettext import gettext as _
from jade_gui.utils import disks
from jade_gui.widgets.partition import PartitionEntry
from jade_gui.classes.partition import Partition

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/partition_screen.ui')
class PartitionScreen(Adw.Bin):
    __gtype_name__ = "PartitionScreen"

    disk_list = Gtk.Template.Child()
    open_bash = Gtk.Template.Child()
    open_gparted = Gtk.Template.Child()
    partition_list = Gtk.Template.Child()
    next_page_button = Gtk.Template.Child()
    reload_partitions = Gtk.Template.Child()
    manual_partitioning = Gtk.Template.Child()
    automatic_partitioning = Gtk.Template.Child()
    manual_partitioning_page = Gtk.Template.Child()
    automatic_partitioning_page = Gtk.Template.Child()

    selected_partition = None
    move_to_summary = False

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.carousel = main_carousel
        self.next_page = next_page
        self.next_page_button.connect("clicked", self.carousel_next)
        self.disk_list.connect("row_selected", self.row_selected)
        self.manual_partitioning.connect("clicked", self.switch_manual_partitioning)
        self.reload_partitions.connect("clicked", self.check_partitions)
        self.automatic_partitioning.connect("clicked", self.switch_automatic_partitioning)
        self.open_bash.connect("clicked", self.bash)
        self.open_gparted.connect("clicked", self.gparted)

    def gparted(self, widget):
        subprocess.run([shutil.which("bash"), "-c", "bash -- /app/share/jade-gui/jade_gui/scripts/openGparted.sh"])

    def bash(self, widget):
        subprocess.run([shutil.which("bash"), "-c", "bash -- /app/share/jade-gui/jade_gui/scripts/openBash.sh"])

    def check_partitions(self, widget):
        self.partition_list.select_all()
        print(self.partition_list.get_row_at_index(2))
        for i in range(0, len(self.window.available_partitions)):
            self.partition_list.remove(self.partition_list.get_row_at_index(0))
        self.available_partitions = disks.get_partitions()
        self.window.available_partitions = self.available_partitions
        for partition in self.available_partitions:
            self.partition_list.append(
                PartitionEntry(
                    window=self,
                    partition=Partition(partition=partition, mountpoint="", filesystem="", size="10000nab (neco arc bytes)"),
                    application=None
                )
            )

    def switch_automatic_partitioning(self, widget):
        self.automatic_partitioning_page.set_visible(True)
        self.manual_partitioning_page.set_visible(False)
        self.window.partition_mode = "Auto"


    def switch_manual_partitioning(self, widget):
        self.automatic_partitioning_page.set_visible(False)
        self.manual_partitioning_page.set_visible(True)
        self.window.partition_mode = "Manual"

    def row_selected(self, widget, row):
        if row is not None:
            print(row.get_title())
            row.select_button.set_active(True)
            self.selected_partition = row
        else:
            print("ERROR: invalid row slected")

    def carousel_next(self, widget):
        self.window.set_previous_page(self.window.misc_screen)
        self.window.summary_screen.initialize()
        self.carousel.scroll_to(self.next_page, True)
