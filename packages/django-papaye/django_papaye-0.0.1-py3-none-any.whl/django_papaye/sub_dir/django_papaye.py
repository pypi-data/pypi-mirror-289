#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Guy-Yann VECTOL"
__credits__ = ["Guy-Yann VECTOL"]
__Lisence__ = "BSD"
__maintainer__ = "Guy-Yann VECTOL"
__email__ = "guyyann.vectol@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

# Default python packages
import logging
import os
import shutil

from distutils.dir_util import copy_tree


class DjangoPapaye:
    """Class that allows the developer to use Transcript with ease"""

    def __init__(self, conf_path=os.getcwd()):
        """Saves config file location"""
        self.conf_path = conf_path

    def configure(self):
        """Creates all the required files and folders"""
        print('Installing DjangoPapaye inside your Django project...')

        try:
            shutil.copytree('./django_papaye/src/t_logic', './t_logic')
        except:
            print('-- t_logic folder already existing, skipping --')

        copy_tree('./django_papaye/src/npm', './')

        os.system('npm install')

        print('... done => Everything is now ready!')


if __name__ == "__main__":
    DjangoPapaye().configure()
