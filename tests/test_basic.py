# -*- coding: utf-8 -*-
"""
    Premier fichier de test. Sert à svoir si tout fonctionne.
"""

#========== IMPORT ==========#

import unittest
from .context import mcs_dtw


#=========  TESTS   =========#

class TestBasic(unittest.TestCase):
    """
        Classe de test basique.
    """

    def test_basic_true(self):
        """
            Test simple pour vérifier si unittest
            fonctionne bien
        """
        vrai = True
        self.assertTrue(vrai)

    def test_basic_import(self):
        """
            Test utilisé pour regardet si mcs_dtw est
            importé correctement
        """
        self.assertTrue(mcs_dtw.is_imported())


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
