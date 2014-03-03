#!/usr/bin/env python

from distutils.core import setup
import sys

version = '0.1'

if sys.version < '3':
    package_dir = {'': 'csp'}
else:
    package_dir = {'': 'csp3'}


setup(name='python-csp',
      version=version,
      description="Communicating sequential processes for Python",
      long_description="""\
python-csp adds communicating sequential processes to Python""",
      classifiers=["Intended Audience :: Developers",
                   ("License :: OSI Approved :: " +
                    "GNU General Public License (GPL)"),
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries",
                   "Topic :: System :: Distributed Computing"],
      keywords='concurrency multicore parallel',
      author='Sarah Mount',
      author_email='s.mount@wlv.ac.uk',
      url='http://github.com/snim2/python-csp/',
      license='GPL',
      package_dir=package_dir,
      scripts=['scripts/python-csp', ],
      )
