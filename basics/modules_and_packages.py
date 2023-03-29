from day10 import add
import os
from prettytable import PrettyTable
import mk01.mk0101 as mk
from module2 import *
from module1 import *
from util import is_even
import numpy as np
import sys
import random
other_folder = os.path.join(os.getcwd(), '..', '100days')
folder_abspath = os.path.abspath(other_folder)
print(folder_abspath)
sys.path.append(folder_abspath)  # add other directory to path

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


# absolute path of this script: /Users/mk/dev/python/basics/modules_and_packages.py
current_path = os.path.abspath(__file__)
print(current_path)
# absolute path of this script's directory: /Users/mk/dev/python/basics
print(os.getcwd())


# MODULES
# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.

# Import Module (the entire file)
# add module name to the current namespace. Using the module name you can access the functions:


random.randint(1, 5)    # referenced with its full name


# import using an alias
# Using the alias you can access the functions


# a variant of the import statement that imports names directly into the importing module’s namespace:
# import specific part(s)
# no <modulename>. prefix before members
x = is_even(10)     # no <modulename>. prefix before members
print(x)


# Packages
# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
# Suppose you want to design a collection of modules (a “package”) for the uniform handling of sound files and sound data:

#       sound/                            Top-level package
#               __init__.py               Initialize the sound package
#               formats/                  Subpackage for file format conversions
#                       __init__.py
#                       wavread.py
#                       wavwrite.py
#                       auread.py
#                       auwrite.py
#                       ...
#               effects/                  Subpackage for sound effects
#                       __init__.py
#                       echo.py
#                       surround.py
#                       ...
#               filters/                  Subpackage for filters
#                       __init__.py
#                       equalizer.py
#                       karaoke.py
#                       ...

# Users of the package can import individual modules from the package, for example:
#
#       import sound.effects.echo

# This loads the submodule sound.effects.echo. It must be referenced with its full name.

#       sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# An alternative way of importing the submodule is:

#       from sound.effects import echo
# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

#       echo.echofilter(input, output, delay=0.7, atten=4)


# from exercises import menu  # we can import a function from a module !

# naming conflicts
# The advantage of importing everything from the math module is that your code can be more concise.
# The disadvantage is that there might be conflicts between names defined in different modules, or between a name from a module and one of your variables.
print(x)    # defined both local and in modules: True


print(get_name())   # "Module 1"
print(x)            # defined both local and in modules: "Module 1"


print(get_name())   # "Module 2"
print(x)    # defined both local and in modules: "Module 2"


# INSTALL a package
# ------------------

# The Python Package Index (PyPI) is a repository of software for the Python programming language.
# PyPI helps you find and install software developed and shared by the Python community.
# Package authors use PyPI to distribute their software.
# It’s important to note that the term “package” in this context is being used to describe a bundle of software to be installed
# (i.e. as a synonym for a distribution).

# The two main tools that install Python packages are pip and conda.
# PIP is a package manager for Python packages and installs from the Python Package Index (https://pypi.org/)
# conda installs from its own channels (typically “defaults” or “conda-forge”).
# The Python Package Index (PyPI) is a repository of software for the Python programming language.

# To install the latest version of “SomeProject”:
# $ pip3 install <package-name>

# To install a specific version:
# $ pip3 install "SomeProject==1.4"

# Upgrade an already installed SomeProject to the latest from PyPI:
# python3 -m pip install --upgrade <package-name>

# Install a project from VCS in “editable” mode:
# python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git

# CREATE A PACKAGE
# -----------------
#  __init__.py file will tell Python to treat directories as modules (or sub-modules).


# import from a subfolder
# assume there is a folder on the same level as this source file (data), and under that folder there is a module (questions.py)
# from data.questions import question_list

# import mk01.mk0101;    mk01.mk0101.introduce()      # import dir.filename
mk.introduce()         # give an alias

# import from another folder
# assume we want to access file2.py from file1.py (go one level op, select another folder, go in that folder)

# project/
#         basics/
#                 modules_and_packages.py
#         100days/
#                 file2.py

# sys.path.append("module1")


# prettytable package - A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
# https://pypi.org/project/prettytable/
# pip install prettytable

tbl = PrettyTable()

# add data BY ROW
tbl.field_names = ["City name", "Area", "Population"]
tbl.add_row(["Adelaide", 1295, 1158259])
tbl.add_row(["Brisbane", 5905, 1857594])
tbl.add_row(["Darwin", 112, 120900])

# add data BY COLUMN
tbl.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7])
print(tbl)


print(x)
