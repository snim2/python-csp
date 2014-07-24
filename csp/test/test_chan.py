"""
Test channels.

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


def test_channels_one_channel():
    c1 = Channel()
    p = Par(recv1(c1), send1(c1))
    p.start()
    return


def test_channels_one_chan_per_proc_pair():
    chans = [Channel() for i in range(5)]
    p = [send1(chan) for chan in chans] + [recv1(chan) for chan in chans]
    pp = Par(*p)
    pp.start()
    return


def test_channels_many_proc_one_chan():
    chan = Channel()
    p = [send1(chan) for i in range(5)] + [recv1(chan) for i in range(5)]
    pp = Par(*p)
    pp.start()
    return
