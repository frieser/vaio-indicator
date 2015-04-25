#
# Copyright (C) 2015  Hector Molano <fiti.pol@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import pyudev
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gettext import gettext as _


class VaioIndicator:
    profilesOptions = []
    udevPath = "/sys/devices/platform/sony-laptop"
    indicatorName = "vaio-indicator"
    indicatorIcon = "system"
    indicatorCategory = appindicator.IndicatorCategory.HARDWARE

    def __init__(self):
        self.indicator = appindicator.Indicator.new(
            self.indicatorName,
            self.indicatorIcon,
            self.indicatorCategory)

        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

        self.retrive_device_information()
        self.build_menu()

    def build_menu(self):
        menu = gtk.Menu()

        for option in self.profilesOptions:
            item = gtk.MenuItem(_(option.capitalize()))
            menu.append(item)
            item.connect("activate", self.set_thermal_control_profile, option)
            item.show()

        quit_separator = gtk.SeparatorMenuItem()
        menu.append(quit_separator)
        quit_separator.show()

        quit_menu_item = gtk.MenuItem(_('Quit'))
        quit_menu_item.connect('activate', self.quit)
        quit_menu_item.show()
        menu.append(quit_menu_item)

        self.indicator.set_menu(menu)

    def set_thermal_control_profile(self, w, profile):
        os.system('echo ' + profile + ' | pkexec tee ' + self.udevPath + '/thermal_control')

    def retrive_device_information(self):
        context = pyudev.Context()
        devices = context.list_devices().match_subsystem('platform').match_property('DRIVER', 'sony-laptop')

        for device in devices:
            self.udevPath = device.sys_path
            attributes = device.attributes
            self.profilesOptions.extend(attributes.asstring('thermal_profiles').split())

    def quit(self, widget):
        gtk.main_quit()
