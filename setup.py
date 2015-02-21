#!/usr/bin/env python3

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.readlines()

setup(name='Octivity',
      version='0.0',
      description='Octivity',
      long_description="{}\n\n{}".format(README, CHANGES),
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Motoki Naruse',
      author_email='motoki@naru.se',
      url='',
      keywords='GitHub Activity',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = src.app:main
      [console_scripts]
      initialize_octivity_db = src.scripts.initializedb:main
      """,
      )
