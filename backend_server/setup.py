#!/usr/bin/env python
from setuptools import setup, find_packages
import os


def read(ftext):
    return open(os.path.join(os.path.dirname(__file__), ftext)).read()


requirements = [r.strip() for r in open("requirements.txt") if r.strip() and not r.strip().startswith("#")]

setup(
    name="hemontika",
    version="1.0",
    packages=find_packages(),
    description="Hemontika is for literatures",
    long_description=read("backend_guide"),
    author="Hemontika",
    author_email="chakrabortyabhradeep79@gmail.com",
    url="https://github.com/Hemontika/hemontika-web",
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Intended Audience :: Other Audience",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "open source",
        "novels",
        "literature",
    ],
    install_requires=requirements,
)
