"""
Tests for ALTing.

Copyright (C) Sarah Mount, 2014.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from base import *


def test_alt0():
    ta0 = testAlt0()
    ta0.start()
    return


def test_alt1():
    ch1 = Channel()
    Par(testAlt1(ch1), sendAlt(ch1, 100)).start()
    return


def test_alt2():
    ch2, ch3, ch4 = Channel(), Channel(), Channel()
    Par(testAlt2(ch2, ch3, ch4),
        sendAlt(ch2, 100),
        sendAlt(ch3, 200),
        sendAlt(ch4, 300)).start()
    return


def test_alt3():
    ch5, ch6, ch7 = Channel(), Channel(), Channel()
    ta3 = Par(testAlt3(ch5, ch6, ch7),
              sendAlt(ch5, 100),
              sendAlt(ch6, 200),
              sendAlt(ch7, 300))
    ta3.start()
    return


def test_alt4():
    ch8, ch9, ch10 = Channel(), Channel(), Channel()
    Par(testAlt4(ch8, ch9, ch10),
        sendAlt(ch8, 100),
        sendAlt(ch9, 200),
        sendAlt(ch10, 300)).start()
    return
