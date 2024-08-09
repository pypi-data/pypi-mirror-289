#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

setup(
  name = "smart-nn",
  version = "0.0.1",
  description = "A library for making it easier to work with neural networks",
  long_description = "A library for making it easier to work with neural networks",
  url ="https://github.com/jslegers/smart-nn",
  author ="John Slegers",
  license = "GNU v3",
  package_dir={"": "src"},
  packages=find_namespace_packages(where="src"),
  python_requires=">=3.8.0",
  install_requires = []
)
