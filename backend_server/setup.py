#!/usr/bin/env python
from setuptools import setup, find_packages

requirements = [
    r.strip() for r in open("requirements.txt") if r.strip() and not r.strip().startswith("#")
]

setup(name='hemontika',
      version='1.0',
      packages=find_packages(),
      description='Hemontika is for literatures',
      long_description="In hemontika user can write their own stories, poems etc. and can read other's",
      author="Hemontika",
      author_email="chakrabortyabhradeep79@gmail.com",
      url="https://github.com/Hemontika/hemontika-web",
      zip_safe=False,
      classifiers=[
          # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
          "Development Status :: 4 - Beta",
          "Intended Audience :: Writers and Readers",
        #   "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
      ],
      keywords=[
          "open source",
          "novels"
          "literature",
      ],
      install_requires=requirements,
      )