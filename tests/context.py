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
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mcs_dtw
