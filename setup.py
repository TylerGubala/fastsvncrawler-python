#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup, find_packages
from setuptools.extension import Extension

_EXTENSION = Extension(name = "fastsvncrawler", 
                       include_dirs = ["external/apr/include",
                                       "external/subversion/subversion/include",
                                       "external/subversion/subversion/libsvn_ra"],
                       sources = ["fastsvncrawler/fastsvncrawler-python.c"])

setup(name = "fastsvncrawler-python",
      version = "0.0.1a0",
      description = "Efficient svn traversal in python",
      author = "Tyler Gubala",
      author_email = "gubalatyler@gmail.com",
      url = "https://github.com/TylerGubala/fastsvncrawler-python",
      ext_modules = [_EXTENSION])
