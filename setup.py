#!/usr/bin/env python3

from setuptools import setup


setup(
    name='xivo-cli',
    version='1.0',
    description='XiVO CLI',
    author='Sebastien Duthil',
    author_email='duthils@free.fr',
    url='http://xivo.io/',
    scripts=['bin/xivo',
             'bin/xivo-l',
             'bin/xivo-log',
             'bin/xivo-r',
             'bin/xivo-restart'],
)
