# $ which pip3
# /Library/Frameworks/Python.framework/Versions/3.10/bin/pip3

# ls -l /usr/local/bin/pip3
# lrwxrwxr-x  1 root  admin  67 Oct 24 14:54 /usr/local/bin/pip3 -> ../../../Library/Frameworks/Python.framework/Versions/3.10/bin/pip3

# $ pip3 --version    
# pip 22.2.2 from /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pip (python 3.10)

# ensure pip is up to date
# $ pip3 install --upgrade pip

# $ pip3 list
# Package    Version
# ---------- -------
# numpy      1.23.4
# pip        22.3.1
# setuptools 63.2.0

# Creating Virtual Environments
# ------------------------------
# Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. 
# How can you use both these applications? 
# Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, 
# rather than being installed globally.

# $ python3 -m venv /path/to/new/virtual/environment
# $ python3 -m venv /Users/mk/dev/python/environments/mkenv3.10

# to activate
# $ source /path/to/venv/bin/activate
# (mkenv3.10) $ which python    (prompt changes)
# /Users/mk/dev/python/environments/mkenv3.10/bin/python

#to deactivate
# (mkenv3.10) $ deactivate
# $



# INSTALL a package
# ------------------
# The two main tools that install Python packages are pip and conda. 
# PIP is a package manager for Python packages and installs from the Python Package Index (https://pypi.org/)
# conda installs from its own channels (typically “defaults” or “conda-forge”). 
# The Python Package Index (PyPI) is a repository of software for the Python programming language.

# To install the latest version of “SomeProject”:
# $ pip3 install "SomeProject"

# To install a specific version:
# $ pip3 install "SomeProject==1.4"


# CREATE A PACKAGE
# -----------------
#  __init__.py file will tell Python to treat directories as modules (or sub-modules).


# Import Module (the entire file)
# add module name to the current namespace. Using the module name you can access the functions:
import random 
random.randint(1, 5)

# import package using an alias
# Using the module name you can access the functions
import numpy as np


# a variant of the import statement that imports names directly into the importing module’s namespace:
from util import is_even
x = is_even(10)     # no <modulename> prefix
print(x)

# import sub-directory
# import mk01.mk0101;    mk01.mk0101.introduce()      # import dir.filename
import mk01.mk0101 as mk
mk.introduce()         # give an alias



# import a specific part(s) of a package
# from numpy import array