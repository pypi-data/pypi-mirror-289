#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'task-tracker-cli'
DESCRIPTION = 'A simple CLI tool for managing tasks.'
URL = 'https://github.com/under-script/task-tracker-cli'
EMAIL = 'abdulmajidyunusov18@gmail.com'
AUTHOR = 'Yunusov Abdulmajid'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0.1'

# What packages are required for this module to be executed?
REQUIRED = [
    'click',
    'prettytable',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# Load the README file as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        'console_scripts': ['task-cli=main:cli'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/under-script/task-tracker-cli/issues',
        'Source': 'https://github.com/under-script/task-tracker-cli',
    },
)