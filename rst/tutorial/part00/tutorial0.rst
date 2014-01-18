Part 0 - Downloading and installing python-csp
==============================================

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

Tool support
------------

"Vanilla" Python comes with an interpreter shell that gives you access to the programming language, built in help, and so on. python-csp comes with a variant of this shell with some additions. To start the shell just type:

::

    $ python-csp


at the command line.

..

Command history
^^^^^^^^^^^^^^^

Unlike the ordinary Python shell, by default the python-csp shell has command history enabled. This means that you can press the "up" or "down" arrows on your keyboard to scroll through the code you have entered into the shell, saving you valuable typing time.

..

python-csp specific help
^^^^^^^^^^^^^^^^^^^^^^^^

You can use Python's `help()` function to examine any module, class, function or variable that comes with python-csp, just like you can with any other library. However, the python-csp shell comes with a set of specific documentation that you can access via the `info` command. 


You can start by typing `info csp` to get general information about the python-csp library, or you can ask for `info` on a specific topic to drill down into the details. Note that `info` is a command and not a function, so you say `info csp` not `info(csp)`.

Here's an example python-csp shell session:

::

    $ python-csp
    
    CSP Python (c) 2008. Licensed under the GPL(v2).
    Type "info csp" for more information.
    Press Ctrl-C to close the CSP channel server.
    
    >>> info
    
    *** python-csp: general info ***
    
    python-csp is an implementation of Hoare's Communicating Sequential
    Processes in Python. For specific info on any aspect of CSP, use the
    following:
    
    For info on Skip, type: 	info skip
    For info on channels, type: 	info channel
    For info on Alternative, type: 	info alt
    For info on CSPServer, type: 	info server
    For info on poisoning, type: 	info poison
    For info on built-ins, type: 	info builtin
    For info on Sequence, type: 	info seq
    For info on Timer, type: 	info timer
    For info on Parallel, type: 	info par
    For info on processes, type: 	info process
    
    >>> 
    
..

Next in the tutorial
--------------------

:doc:`../part01/tutorial1`

..

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

