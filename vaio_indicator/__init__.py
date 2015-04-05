#
#    Copyright (C) 2015  Hector Molano <fiti.pol@gmail.com>
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

NAME = 'vaio-indicator'
DISPLAY_NAME = 'VaioIndicator'
COMMENTS = 'Sony Vaio Indicator'
VERSION = '0.1'
LICENSE = 'GPL-3'
COPYRIGHT = 'Copyright (C) 2015 Hector Molano'
WEBSITE = 'https://github.com/frieser/vaio-indicator'

AUTHORS = [
	'Hector Molano <fiti.pol@gmail.com>'
]


from gi.repository import Gtk as gtk
from vaio_indicator.indicator import *

def main():
	# Workaround to python gtk bug (#622084) causing Ctrl+C not to work
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	vaio_indicator = VaioIndicator()
	gtk.main()