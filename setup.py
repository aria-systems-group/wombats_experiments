# Copyright (C) 2020 University of Colorado at Boulder
# This software may be modified and distributed under the terms of the
# MIT license. See the accompanying LICENSE file for details.
from sys import platform
from setuptools import setup
from setuptools.command.install import install
from subprocess import call
import pathlib
import pkg_resources
LIBRARY_NAME = "wombats"


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


## Installation of pygraphviz
# linux
if platform == "linux" or platform == "linux2":
    pass
    install_requires.append('pygrpahviz')
    cmdclass = {}
# OS X
elif platform == "darwin":
    class CustomInstall(install):
        """
        Somehow installing pygraphviz fails on mac.
        We have to tell pip where the graphviz libraries are on this machine.
        Plus, parse_requirements cannot handle arguments,
        so I had to use CustomInstall.
        """
        def run(self):
            call(['pip', 'install', '--global-option=build_ext', '--global-option="-I/usr/local/include"', '--global-option="-L/usr/local/lib"', 'pygraphviz'])
            install.run(self)
    cmdclass = {'install': CustomInstall}
# Windows...
elif platform == "win32":
    raise Exception('Not Supported')


setup(
    name=LIBRARY_NAME,
    version='1.0.0',
    author="Nicholas Renninger",
    author_email="nicholas.renninger@colorado.edu",
    description="",
    license="",
    url='https://github.com/aria-systems-group/wombats',
    python_requires='>=3.5',
	package_dir={'':LIBRARY_NAME},
    cmdclass=cmdclass,
    install_requires=install_requires,
)
