python-csp: Communicating Sequential Processes for Python
=========================================================

Copyright (C) Sarah Mount, 2009 under the GNU GPL v2. See the file LICENSE for
more details.

[![Build Status](https://travis-ci.org/snim2/python-csp.png?branch=master)](https://travis-ci.org/snim2/python-csp)
[![Requirements Status](https://requires.io/github/snim2/python-csp/requirements.png?branch=master)](https://requires.io/github/snim2/python-csp/requirements/?branch=master)
[![PyPi version](https://pypip.in/v/python-csp/badge.png)](https://crate.io/packages/python-csp/)
[![PyPi downloads](https://pypip.in/d/python-csp/badge.png)](https://crate.io/packages/python-csp/)

Installation
------------

python-csp can be installed using PIP (PIP Installs Python):

```bash
    $ sudo pip install python-csp
```

or from a source distribution using setup.py:

```bash
    $ python setup.py install
```

Introduction
------------

python-csp adds C.A.R. (Tony) Hoare's Communicating Sequential Processes to 
Python. A brief example:

```python
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
>>> chan = Channel()
>>> Par(reader(chan), writer(chan, 5)).start()
0
1
2
3
4
>>>
```

Documentation.
-------------

There are several sources of documentation for python-csp:

 * Online documentation, including a tutorial, is hosted on [Read the Docs](http://python-csp.readthedocs.org/en/latest/)

 * If you are running the python-csp shell, type "info csp" to list available in-shell help.

 * Some community documentation, such as sprint reports and PDFs of peer-reviewed publications can be found at [extradocs](http://github.com/python-concurrency/extradocs)


Support and contributing.
------------------------

We have a [mailing list](https://groups.google.com/forum/#!forum/python-csp) where you can ask questions. 

If you wish to contribute to this project, please fork the repo on GitHub and issue a pull request.

Publications.
------------

S. Mount, M. Hammoudeh, S. Wilson, R. Newman (2009) CSP as a Domain-Specific 
Language Embedded in Python and Jython. In Proceedings of Communicating Process
Architectures 2009. Eindoven, Netherlands. 1st -- 4th November 2009. Published 
IOS Press. [[PDF] (http://github.com/python-concurrency/extradocs)]
