#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    MCS_DTW est un module de reconnaissance vocal utilisé pour reconnaitre
    des ordres pour un petit robot.
"""

__author__ = "Clément GUICHARD, Dorian AZEMA, Kévin DELCOURT"
__version__ = "0.1.0"
__description__ = __doc__
__maintainer__ = "Clément GUICHARD"
__email__ = "clement.guichard@master-developpement-logiciel.fr"

name = "mcs_dtw"  # pylint: disable=invalid-name


def is_imported():
    """
        Used in tests/test_basic.py to test if package
        imported correctly.
    """
    return True


def cmd_mcsdtw():
    """
        Command linked.
    """
    print("\033[1;34m#======= MCS_DTW =======#\033[0m\n",
          "Author: %s" % (__author__),
          "Version: %s" % (__version__),
          "Description: %s" % (__description__),
          sep="\n")
