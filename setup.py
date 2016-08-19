#!/usr/bin/python
# -*- coding: utf-8 -*-

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from setuptools import setup

VERSION = '1.0.0'

setup(
    name='bbremote',
    version=VERSION,
    scripts=['bbremote'],
    packages=['remote'],
    author='Barebox',
    author_email='barebox@lists.infradead.org',
    maintainer='Barebox',
    maintainer_email='barebox@lists.infradead.org',

    description='barebox remote control.',
    long_description='''barebox remote control is for controlling barebox from a remote host via scripts..''',
    url='http://www.barebox.org/doc/latest/index.html',
    keywords='serial remote control',
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Embedded Systems",
    ],
)
