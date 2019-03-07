#!/usr/bin/env python
from setuptools import setup

setup(
    name = 'django-simplesass',
    version = '0.0.1',
    url = 'https://github.com/rtts/django-simplesass',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    license = 'GPL3',
    packages = ['simplesass'],
    install_requires = [
        'django',
        'libsass',
    ],
)
