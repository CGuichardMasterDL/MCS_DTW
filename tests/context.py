# -*- coding: utf-8 -*-
# pylint: disable-all
"""
    Fichier de context utilisé par tous les fichiers de test.
    Ce fichier permet de récupérer le module mcs_dtw.
"""

#========== IMPORT ==========#

import sys
import os

# Correction du chemin pour l'import qui suit
ROOT_PATH =  os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/"
sys.path.insert(0, ROOT_PATH)

import mcs_dtw

#==========  DEFS  ==========#


def path(filepath):
    return ROOT_PATH+filepath
