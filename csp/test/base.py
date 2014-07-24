#!/usr/bin/env python

"""
Simple tests for basic python-csp functionality.

Copyright (C) Sarah Mount, 2009.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have rceeived a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
"""

import os
import random
import time

from ..csp import *
from ..guards import Timer
set_debug(True)


@process
def hello():
    t = Timer()
    for i in range(5):
        print i
        t.sleep(1)


@process
def send_recv(n):
    chan = Channel()
    Par(send1(chan, n), recv1(chan, n)).start()
    return


@process
def send1(cout, n):
    """
    readset =
    writeset = cout
    """
    cout.write(n)
    return


@process
def recv1(cin, expected):
    """
    readset = cin
    writeset =
    """
    obj = cin.read()
    assert obj == expected
    return


@process
def send5(cout):
    """
    readset =
    writeset = cout
    """
    for i in range(5):
        cout.write(i)
    return


@process
def recv5(cin):
    """
    readset = cin
    writeset =
    """
    objs = []
    for i in range(5):
        objs.append(cin.read())
    assert len(objs) == 5
    sort(objs)
    assert objs == range(5)
    return


@process
def send100(cout):
    """
    readset =
    writeset = cout
    """
    for i in range(100):
        cout.write(i)
    return


@process
def recv100(cin):
    """
    readset = cin
    writeset =
    """
    objs = []
    for i in range(100):
        objs.append(cin.read())
    assert len(objs) == 100
    sort(objs)
    assert objs == range(100)
    return


class MethodProcs(object):

    def __init__(self):
        self.chan = Channel()
        return

    @process
    def send(self, msg):
        """
        readset = self.chan
        writeset =
        """
        self.chan.write(msg)
        return

    @process
    def recv(self, expected):
        """
        readset = self.chan
        writeset =
        """
        obj = self.chan.read()
        assert obj == expected
        return


@process
def testpoison(chan):
    print('Sending termination event...')
    chan.poison()
    return


@process
def sendAlt(cout, num):
    """
    readset =
    writeset = cout
    """
    t = Timer()
    t.sleep(1)
    cout.write(num)
    return


@process
def testAlt0():
    alt = Alt(Skip(), Skip(), Skip())
    for i in range(3):
        print('*** TestAlt0 selecting...')
        val = alt.select()
        print('* Got this from Alt:' + str(val))
    return


@process
def testAlt1(cin):
    """
    readset = cin
    writeset =
    """
    alt = Alt(cin)
    numeric = 0
    while numeric < 1:
        print('*** TestAlt1 selecting...')
        val = alt.select()
        if isinstance(val, int):
            numeric += 1
        print('* Got this from Alt:' + str(val))
    return


@process
def testAlt2(cin1, cin2, cin3):
    """
    readset = cin1, cin2, cin3
    writeset =
    """
    alt = Alt(Skip(), cin1, cin2, cin3)
    numeric = 0
    while numeric < 3:
        print('*** TestAlt2 selecting...')
        val = alt.select()
        if isinstance(val, int):
            numeric += 1
        print('* Got this from Alt:' + str(val))
    return


@process
def testAlt3(cin1, cin2, cin3):
    """
    readset = cin1, cin2, cin3
    writeset =
    """
    # For obvious reasons, SKIP cannot go first
    alt = Alt(cin1, cin2, cin3, Skip())
    numeric = 0
    while numeric < 3:
        print('*** TestAlt3 selecting...')
        val = alt.pri_select()
        if isinstance(val, int):
            numeric += 1
        print('* Got this from Alt:' + str(val))
    return


@process
def testAlt4(cin1, cin2, cin3):
    """
    readset = cin1, cin2, cin3
    writeset =
    """
    alt = Alt(Skip(), cin1, cin2, cin3)
    numeric = 0
    while numeric < 3:
        print('*** TestAlt4 selecting...')
        val = alt.fair_select()
        if isinstance(val, int):
            numeric += 1
        print('* Got this from Alt:' + str(val))
    return


@process
def choose(cin1, cin2):
    """
    readset = cin1, cin2
    writeset =
    """
    print(cin1 | cin2)
    print(cin1 | cin2)
    return


@process
def testAltRRep(cin1, cin2, cin3):
    """
    readset = cin1, cin2, cin3
    writeset =
    """
    gen = Alt(cin1, cin2, cin3) * 3
    print(next(gen))
    print(next(gen))
    print(next(gen))
    return


@process
def testAltLRep(cin1, cin2, cin3):
    """
    readset = cin1, cin2, cin3
    writeset =
    """
    gen = 3 * Alt(cin1, cin2, cin3)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    return
