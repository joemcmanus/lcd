#!/usr/bin/env python
# File    : lcd.py  A very simple LCD script for Galileo Gen 2
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.3  04/05/2016
# Copyright (C) 2016 Joe McManus
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

import os
import serial
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Simple LCD Display Script for Galileo')
parser.add_argument('lineOne', help="The message you want to display on line 1 of the LCD", type=str)
parser.add_argument('lineTwo', help="The message you want to display on line 2 of the LCD", type=str, nargs='?')
parser.add_argument('--version', action='version',version='%(prog)s 0.2')
args=parser.parse_args()


def setPins(pin, mode):
	pin=str(pin)
	mode=str(mode)

	if not os.path.isdir('/sys/class/gpio/gpio' + pin):
		fh=open("/sys/class/gpio/export", "w")
		fh.write(pin)
		fh.close()

	fh=open('/sys/class/gpio/gpio' + pin + '/direction', "w")
	fh.write('out')
	fh.close()

	fh=open('/sys/class/gpio/gpio' + pin + '/value', "w")
	fh.write(mode)
	fh.close()

print("Setting up GPIO Pins")
setPins(28, 0) 
setPins(32, 1) 
setPins(33, 1)
setPins(45, 1)

os.system('stty -F /dev/ttyS0 9600')
lcd=serial.Serial('/dev/ttyS0', 9600)

#Clear screen 
lcd.write(b"                ");
lcd.write(b"                ");

#Move to first line
lcd.write(b"\xFE\x80")

print("Sending your message to /dev/ttyS0")
#Write a message
lcd.write(args.lineOne)

if args.lineTwo:
	lcd.write(b"\xFE\xC0")
	lcd.write(args.lineTwo)

quit()
