#
# Copyright (C) 2015  Hector Molano <fiti.pol@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
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


class Vaio:
    subsystem = "platform"
    udev_path = "/sys/devices/platform/sony-laptop"

    def __init__(self):
        context = pyudev.Context()
        devices = context.list_devices().match_subsystem(self.subsystem).match_property('DRIVER', 'sony-laptop')
        for device in devices:
            self.device = device
            break

    def get_thermal_profiles(self):
        return self.device.attributes.asstring('thermal_profiles').split()

    def get_current_thermal_profile(self):
        return self.device.attributes.asstring('thermal_control')

    def set_thermal_control_profile(self, profile):
        os.system('echo ' + profile + ' | pkexec tee ' + self.udev_path + '/thermal_control')