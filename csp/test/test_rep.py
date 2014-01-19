"""
Test process replication.

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


def test_rep0():
    ch1, ch2, ch3 = Channel(), Channel(), Channel()
    Par(sendAlt(ch1, 100), sendAlt(ch2, 200), sendAlt(ch3, 300),
        testAltRRep(ch1, ch2, ch3)).start()
    return


def test_rep1():
    ch1, ch2, ch3 = Channel(), Channel(), Channel()
    Par(sendAlt(ch1, 100), sendAlt(ch2, 200), sendAlt(ch3, 300),
        testAltLRep(ch1, ch2, ch3)).start()
    return


def test_rep2():
    hello() * 3
    2 * hello()
    return
