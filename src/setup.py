
from distutils.core import setup, Extension

module = Extension("remain", sources = ["remain.c"])

setup(name="PackageName",
      version = "0.01",
      description = "Network Scrapper In C.",
      ext_modules = [module]);
