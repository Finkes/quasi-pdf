#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QuasiPDF
-------------

Simple merging of multiple pdf files.

"""
from setuptools import setup

setup(
    name='quasipdf',
    version='0.1',
    url='https://github.com/Finkes/quasi-pdf',
    license='BSD',
    author='Dominik Finkbeiner',
    author_email='finkes93@gmail.com',
    description='PDF slice and merge',
    long_description=__doc__,
    py_modules=['quasipdf'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'pyPdf'
    ],
    entry_points = {
        'console_scripts': ['quasipdf = quasipdf:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)