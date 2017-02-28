from setuptools import setup
import os
import sys
from setuptools.command.test import test as TestCommand
from setuptools import find_packages

try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup


# create package path
PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))


setup(name='cosmonet',
      version='0.1',
      description='cosmonet',
      url='https://github.com/bnord/cosmonet',
      packages=find_packages(PACKAGE_PATH, "test"),
      include_package_data=True,
      package_dir={'cosmonet': 'cosmonet'},
      author='Brian Nord',
      author_email='briandnord@gmail.com',
      license='MIT',
      zip_safe=False)
