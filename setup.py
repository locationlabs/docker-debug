#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.2'

# Jenkins will replace __build__ with a unique value.
__build__ = ''

setup(name='docker-debug',
      version=__version__ + __build__,
      description='Docker container debugging tool',
      author='Location Labs',
      author_email='info@locationlabs.com',
      url='http://locationlabs.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0'
      ],
      install_requires=[
          'docker-py>=0.5.3',
      ],
      tests_require=[
          'mock'
      ],
      test_suite='dockerdebug.tests',
      entry_points={
          'console_scripts': [
              'docker-debug = dockerdebug.main:main',
          ]
      },
      )
