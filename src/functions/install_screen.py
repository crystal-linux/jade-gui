# installer_Screen.py

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

import subprocess, os
import asyncio
from gi.repository import Gtk, GLib, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/pages/install_screen.ui')
class InstallScreen(Adw.Bin):
    __gtype_name__="InstallScreen"

    log_text = Gtk.Template.Child()

    def __init__(self, window, main_carousel, next_page, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window

    def install(self):
        prefs = self.window.summary_screen.installprefs.generate_json()
        with open(os.getenv("HOME")+"/test.log", "wb") as f:
            process = subprocess.Popen(["bash", "-c", "bash -- /app/share/jade_gui/jade_gui/scripts/install.sh"], stdout=subprocess.PIPE)
            for c in iter(lambda: process.stdout.read(1), b""):
                log=c
                try:
                    GLib.idle_add(self.update_output, c.decode("utf-8"))
                except:
                    pass
                f.write(c)

    def update_output(self, message):
        log=self.log_text.get_label()
        new_log=f"{log}{message}"
        self.log_text.set_label(new_log)
