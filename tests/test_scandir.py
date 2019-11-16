# -*- coding: utf-8 -*-
"""
    Module de test pour les fonctionnalités de scandir
"""

#========== IMPORT ==========#

import unittest

from tests.context import path
from mcs_dtw.scandir import ScanDir

#=========  TESTS   =========#


class TestScandDir(unittest.TestCase):
    """
        Classe de test pour le fichier yamlmanager de mcs_dtw.
    """

    CORPUS = path("mcs_dtw/corpus/")


    def test_scandir_contruct(self):
        """
            Test le constructeur
        """
        self.assertTrue(ScanDir().folder() == "./")
        self.assertTrue(ScanDir("").folder() == "./")
        self.assertTrue(ScanDir(None).folder() == "./")
        self.assertTrue(ScanDir(path("dossier-non-existant/")).all() == [])
        with self.assertRaises(TypeError):
            ScanDir(10)


    def test_scandir_all(self):
        """
            Test les résultats
        """
        self.assertTrue(len(ScanDir().all()) > 0)


    def test_scandir_filter(self):
        """
            Test les résultats des filtres
        """
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(extension="wav")) > 0)
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(extension="txt")) == 0)
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(pathcontains="dronevolant_bruite")) > 0)
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(pathcontains="droneroulant")) == 0)
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(name="M01_arretetoi")) > 0)
        self.assertTrue(len(ScanDir(TestScandDir.CORPUS)\
                                           .filter(name="test-non-existant")) == 0)


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
