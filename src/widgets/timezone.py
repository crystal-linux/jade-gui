# timezone.py

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

from datetime import datetime
import pytz
from gi.repository import Gtk, GLib, Adw
from gettext import gettext as _

@Gtk.Template(resource_path='/al/getcryst/jadegui/widgets/timezone.ui')
class TimezoneEntry(Adw.ActionRow):
    __gtype_name__ = 'TimezoneEntry'

    time_label = Gtk.Template.Child()

    def __init__(self, window, region, location, locale, application, **kwargs):
        super().__init__(**kwargs)

        self.region = region
        self.location = location
        self.locale = locale

        self.set_title(region+"/"+location)
        self.time_label.set_text(self.calculate_time(location=location, region=region))

    def calculate_time(self, location, region):
        timezone = pytz.timezone(region+"/"+location)
        datetime_timezone = datetime.now(timezone)
        return datetime_timezone.strftime('%H:%M')
