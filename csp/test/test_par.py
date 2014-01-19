"""
Test parallel execution of processes.

FIXME: Make sure to test that the order of execution is "random".

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

from ..builtins import Generate, Plus, Printer


def test_par_infix():
    send_recv(1) // (send_recv(2), send_recv(3), send_recv(4), send_recv(5))
    return


def test_par_class():
    Par(send_recv(1),
        send_recv(2),
        send_recv(3),
        send_recv(4),
        send_recv(5)).start()
    return
