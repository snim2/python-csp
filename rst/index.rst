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

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

