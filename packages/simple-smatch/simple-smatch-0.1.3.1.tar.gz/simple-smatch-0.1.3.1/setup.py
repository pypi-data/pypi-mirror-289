#!/usr/bin/env python

import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()


setup(name="simple-smatch",
      version='0.1.3.1',
      setup_requires=['setuptools_scm'],
      description="Simple Smatch",
      long_description=README,
      long_description_content_type='text/markdown',
      author="Matt Buchholz",
      author_email="CzechEinsZwo@gmail.com",
      url="https://github.com/EinsZwo/smatch",
      license="MIT",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Linguistic',
          'Topic :: Utilities'
      ],
      keywords='nlp semantics amr evaluation',
      py_modules=["simplesmatchscore", "amr"],
      scripts=["simplesmatchscore.py"],
      )
