# window.py

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

from gi.repository import Gtk, Gdk, Adw
from jade_gui.classes.partition import Partition
from jade_gui.widgets.timezone import TimezoneEntry
from jade_gui.widgets.layout import KeyboardLayout
from jade_gui.widgets.variant import KeyboardVariant
from jade_gui.widgets.desktop import DesktopEntry
from jade_gui.widgets.disk import DiskEntry
from jade_gui.widgets.partition import PartitionEntry
from jade_gui.functions.keyboard_screen import KeyboardScreen
from jade_gui.functions.timezone_screen import TimezoneScreen
from jade_gui.functions.user_screen import UserScreen
from jade_gui.functions.desktop_screen import DesktopScreen
from jade_gui.functions.misc_screen import MiscScreen
from jade_gui.functions.partition_screen import PartitionScreen
from jade_gui.functions.manual_partitioning import ManualPartitionScreen
from jade_gui.functions.summary_screen import SummaryScreen
from jade_gui.functions.install_screen import InstallScreen
from jade_gui.functions.finished_screen import FinishedScreen
from jade_gui.locales.locales_list import locations
from jade_gui.keymaps import keymaps
from jade_gui.desktops import desktops
from jade_gui.utils import disks

@Gtk.Template(resource_path='/al/getcryst/jadegui/window.ui')
class JadeGuiWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'JadeGuiWindow'

    event_controller = Gtk.EventControllerKey.new()
    carousel = Gtk.Template.Child()

    ### Page and widgets on welcome screen
    welcome_page = Gtk.Template.Child()
#   quit_button = Gtk.Template.Child()
    next_button = Gtk.Template.Child()
    back_button = Gtk.Template.Child()
    about_button = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.finished_screen = FinishedScreen(window=self, **kwargs)
        self.installer_screen = InstallScreen(window=self, main_carousel=self.carousel, next_page=self.finished_screen, **kwargs)
        self.summary_screen = SummaryScreen(window=self, main_carousel=self.carousel, next_page=self.installer_screen, **kwargs)
        self.partition_screen = PartitionScreen(window=self, main_carousel=self.carousel, next_page=self.summary_screen, **kwargs)
        self.manual_partition = ManualPartitionScreen(window=self, main_carousel=self.carousel, next_page=self.summary_screen, **kwargs)
        self.misc_screen = MiscScreen(window=self, main_carousel=self.carousel, next_page=self.partition_screen, **kwargs)
        self.desktop_screen = DesktopScreen(window=self, main_carousel=self.carousel, next_page=self.misc_screen, **kwargs)
        self.user_screen = UserScreen(window=self, main_carousel=self.carousel, next_page=self.desktop_screen, **kwargs)
        self.keyboard_screen = KeyboardScreen(window=self, main_carousel=self.carousel, next_page=self.user_screen, **kwargs)
        self.timezone_screen = TimezoneScreen(window=self, main_carousel=self.carousel, next_page=self.keyboard_screen, **kwargs)
        self.carousel.append(self.timezone_screen)
        self.carousel.append(self.keyboard_screen)
        self.carousel.append(self.user_screen)
        self.carousel.append(self.desktop_screen)
        self.carousel.append(self.misc_screen)
        self.carousel.append(self.partition_screen)
        #self.carousel.append(self.manual_partition)
        self.carousel.append(self.summary_screen)
        self.carousel.append(self.installer_screen)
        self.carousel.append(self.finished_screen)
        print(self.carousel.get_n_pages())
        ### Widgets for first page (welcome screen)
        #self.quit_button.connect("clicked", self.confirmQuit)
        #self.summary_screen.connect_buttons()
        self.next_button.connect("clicked", self.carousel_next)
        self.back_button.connect("clicked", self.previousPage)
        self.about_button.connect("clicked", self.show_about)
        self.partition_mode = "Auto"
        ### ---------
        self.previous_page = None
        self.set_previous_page(None)
        ### Test timezones
        for i in locations:
            for locale in i:
                self.timezone_screen.list_timezones.append(TimezoneEntry(window=self, region=locale.region, location=locale.location, locale=locale.locales, **kwargs))
        ### ---------

        ### Test layouts
        for keymap in keymaps:
            layout = KeyboardLayout(window=self, country=keymap.layout, country_shorthand=keymap.backend_layout, variants=keymap.variant, **kwargs)
            firstvariant = KeyboardVariant(window=self, variant=keymap.variant[0], country=layout.country, country_shorthand=layout.country_shorthand, button_group=None, **kwargs)
            layout.add_row(firstvariant)
            for variant in keymap.variant:
                if variant != firstvariant.variant:
                    layout.add_row(KeyboardVariant(window=self, country=layout.country, country_shorthand=layout.country_shorthand, variant=variant, button_group=firstvariant.select_variant, **kwargs))
            self.keyboard_screen.layout_list.add(layout)
        ### ---------

        ### Test desktops
        firstdesktop = DesktopEntry(window=self, desktop=desktops[0], button_group=None, **kwargs) # Manually specifying onyx since the other entries need a button group to attach to
        self.desktop_screen.list_desktops.append(firstdesktop)
        self.desktop_screen.chosen_desktop = self.desktop_screen.list_desktops.get_row_at_index(0).get_title()
        self.desktop_screen.list_desktops.select_row(firstdesktop)
        for desktop in desktops:
            if desktop != desktops[0]:
                self.desktop_screen.list_desktops.append(DesktopEntry(window=self, desktop=desktop, button_group=firstdesktop.select_button, **kwargs))
        ### ---------

        ### Test partitions
        self.available_disks = disks.get_disks()
        firstdisk = DiskEntry(
            window=self,
            disk=self.available_disks[0],
            disk_size=disks.get_disk_size(self.available_disks[0]),
            disk_type=disks.get_disk_type(self.available_disks[0]),
            #disk_model=disks.get_disk_model(available_disks[0]),
            button_group=None,
            **kwargs
        )
        self.partition_screen.disk_list.append(firstdisk)
        firstdisk.toggled_cb(firstdisk.select_button)
        self.partition_screen.selected_partition=firstdisk
        for disk in self.available_disks:
            if disk != self.available_disks[0]:
                self.partition_screen.disk_list.append(
                    DiskEntry(
                        window=self,
                        disk=disk,
                        disk_size=disks.get_disk_size(disk),
                        disk_type=disks.get_disk_type(disk),
                        #disk_model=disks.get_disk_model(disk),
                        button_group=firstdisk.select_button,
                        **kwargs
                    )
                )

        self.available_partitions = disks.get_partitions()
        for partition in self.available_partitions:
            self.partition_screen.partition_list.append(
                PartitionEntry(
                    window=self,
                    partition=Partition(partition=partition, mountpoint="", filesystem="", size="10000nab (neco arc bytes)"),
                    **kwargs
                )
            )
        ### ---------

    def set_previous_page(self, previous_page):
        if previous_page is None:
            self.back_button.set_visible(False)
        else:
            self.back_button.set_visible(True)
        self.previous_page = previous_page

    def previousPage(self, widget):
        if self.previous_page is not None:
            self.previous_page.carousel_next(widget)

    def carousel_next(self, widget):
        self.set_previous_page(None)
        self.carousel.scroll_to(self.timezone_screen, True)

    def confirmQuit(self, idk):

        def handle_response(_widget, response_id):
            if response_id == Gtk.ResponseType.YES:
                _widget.destroy()
                self.destroy()
            elif response_id == Gtk.ResponseType.NO:
                _widget.destroy()

        dialog = Gtk.MessageDialog(
            transient_for=self,
            modal=True,
            parent=self,
            text="Do you want to try\nCrystal without installing?",
            buttons=Gtk.ButtonsType.YES_NO
        )
        dialog.connect("response", handle_response)
        dialog.present()

    def show_about(self, *args):
        builder = Gtk.Builder.new_from_resource("/al/getcryst/jadegui/about.ui")
        about_window = builder.get_object("aboutWindow")
        about_window.set_transient_for(self)
        about_window.present()
