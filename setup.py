#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'sympy',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(miguelgondu): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='generalrepytivity',
    version='0.1.0',
    description="generalrelativity holds some algorithms that render useful when doing computations related to general relativity.",
    long_description=readme + '\n\n' + history,
    author="Miguel Gonzalez Duque",
    author_email='miguelgondu@gmail.com',
    url='https://github.com/miguelgondu/generalrepytivity',
    packages=find_packages(include=['generalrepytivity']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='generalrepytivity',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
