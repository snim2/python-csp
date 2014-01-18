.. python-csp documentation master file, created by
   sphinx-quickstart on Sat Apr 10 00:03:15 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-csp v\ |version| - message-passing concurrency in Python
===============================================================

.. image:: https://pypip.in/v/python-csp/badge.png
    :target: https://crate.io/packages/python-csp/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/python-csp/badge.png
    :target: https://crate.io/packages/$REPO/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/snim2/python-csp.png?branch=master
    :target: https://travis-ci.org/snim2/python-csp
    :alt: Current state of tests on continuous integration server

python-csp adds C.A.R. (Tony) Hoare's Communicating Sequential Processes to 
Python:

::

    >>> @process
    ... def writer(channel, n):
    ...      for i in xrange(n):
    ...              channel.write(i)
    ...      channel.poison()
    ...      return
    ... 
    >>> @process
    ... def reader(channel):
    ...      while True:
    ...              print channel.read()
    ... 
    >>> # Run the two processes in parallel
    >>> # connected by a channel
    >>> chan = Channel()
    >>> Par(reader(chan), writer(chan, 5)).start()
    0
    1
    2
    3
    4
    >>>
    

What is CSP?
------------

Concurrent and parallel programming are generally seen as "difficult" tasks. This is partly because most people have a mental model of how computers work which is fundamentally sequential, and partly because concurrent programs are susceptible to errors such as race hazards, deadlocks, and so on. 

CSP stands for Communicating Sequential Processes, which is a framework for writing concurrent or program via *message passing*. The advantage of message passing is that it makes race hazards impossible and provides a model of concurrency that is much easier to think about and more fun to program with.


Why CSP for Python?
-------------------

Python currently has some support for threaded concurrency via the `thread` and `threading` module, support for parallel programming and the `processing` module. Threads are very low level, difficult to work with and cannot take advantage of multicore architectures that are now becoming commonplace. The `processing` module provides good support for process and thread-safe data structures but neither provide support for the message passing paradigm of programming and the sorts of constructs common to CSP style languages (such as OCCAM, OCCAM-pi, JCSP, C++CSP and so on). python-csp is design to plug this gap and also to provide an idiomatically _pythonic_ implementation of the ideas in CSP.


Installation
------------

python-csp can be installed using PIP (PIP Installs Python):

::

    $ sudo pip install python-csp

or from a source distribution using setup.py:

::

    $ sudo python setup.py install

python-csp lives on GitHub. If you want a copy of the source code you can clone it directly:

::

    $ git clone git://github.com/snim2/python-csp.git

Then install python-csp using the usual Python setup protocol:

::

    $ cd python-csp
    $ sudo python setup.py install


..

Tutorial
========

Beginner
--------

.. toctree::
   :maxdepth: 1

   tutorial/part00/tutorial0
   tutorial/part01/tutorial1
   tutorial/part02/tutorial2
   tutorial/part03/tutorial3
   tutorial/part04/tutorial4
   tutorial/part05/tutorial5

Intermediate
------------

- Part 6 - Using different channel types
.. toctree::
   :maxdepth: 1
   tutorial/part07/tutorial7
   tutorial/part08/tutorial8


Advanced 
--------

.. toctree::
   :maxdepth: 1

- Part 9 – Debugging python-csp programs with extra tool support
- Part 10 – Reactive (or dataflow) programming with python-csp

..

API guide
=========

.. toctree::
   :maxdepth: 2

   csp.rst
   builtins.rst
   guards.rst
   patterns.rst
   mandelbrot.rst


..

Further documentation on python-csp
===================================

- S. Mount, M. Hammoudeh, S. Wilson, R. Newman (2009) CSP as a Domain-Specific Language Embedded in Python and Jython. In Proceedings of Communicating Process Architectures 2009. Eindoven, Netherlands. 1st -- 4th November 2009. Published IOS Press.  

See `here <https://github.com/python-concurrency/extradocs/tree/master/papers>`_ for PDF copies of peer-reviewed papers.

..

Other CSP resources
===================

 * Hoare's original `CSP book <http://www.usingcsp.com/>`_
 * `WoTUG <http://wotug.org/>`_ The place for Communicating Processes
 * `25 years of CSP <http://books.google.co.uk/books?id=4ygZed-24LsC&printsec=frontcover&dq=communicating+sequential+processes&source=bl&ots=VfQoVDyIXn&sig=xDJ3FwyC82NSJ5J1bCMnkWPsS8M&hl=en&ei=c8K_S-K8HZX20gT618GWCQ&sa=X&oi=book_result&ct=result&resnum=12&ved=0CEYQ6AEwCw#v=onepage&q&f=false>`_


..

Other concurrency packages for Python
=====================================

 * `PyCSP <http://code.google.com/p/pycsp/>`_ is another CSP library for Python, and somewhat similar to python-csp. In the medium term it is intended that PyCSP and python-csp will merge.
 * `Trellis <http://peak.telecommunity.com/DevCenter/Trellis>`_ reactive programming for Python
 * `STM <http://peak.telecommunity.com/DevCenter/TrellisSTM>`_ software transactional memory for Python
 * `Kamaelia <http://www.kamaelia.org/Home.html>`_ message passing concurrency using asynchronous channels
 * `Twisted <http://twistedmatrix.com/trac/>`_ event-driven Python programming
 * `Multiprocessing <http://docs.python.org/library/multiprocessing.html>`_ this is the best support in the current standard library for running forked processes. 


..

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

