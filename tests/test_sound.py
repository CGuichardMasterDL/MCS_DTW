# -*- coding: utf-8 -*-
"""
    Test de la classe Sound
"""

#========== IMPORT ==========#

import unittest
from .context import mcs_dtw
from mcs_dtw import ROOT_PATH
from mcs_dtw.sound import Sound

#=========  TESTS   =========#


class TestSound(unittest.TestCase):
    """
        Test de la classe Sound
    """
    sound_path = ROOT_PATH + "/corpus/dronevolant_bruite/M02_avance.wav"

    def setUp(self):
        self.sound = Sound(self.sound_path)

    def tearDown(self):
        del self.sound

    def test_getLocuteur(self):
        """
            Vérifier si le son créé a bien le bon locuteur
        """
        self.assertEqual(self.sound.getLocuteur(), "M02")

    def test_getPath(self):
        """
            Vérifier si le son créé a bien le bon path
        """
        self.assertEqual(self.sound.getPath(), self.sound_path)

    def test_getGenre(self):
        """
            Vérifier si le son créé a bien le bon genre (M ou F)
        """
        self.assertEqual(self.sound.getGenre(), 'M')

    def test_getOrdre(self):
        """
            Vérifier si le son créé a bien le bon ordre
        """
        self.assertEqual(self.sound.getOrdre(), "avance")

    def test_isBruite(self):
        """
            Vérifier si le son créé est bruité ou non
        """
        self.assertEqual(self.sound.isBruite(), True)

    def test_getMfcc(self):
        """
            Vérifier si la matrice mfcc est bien construite
            Notamment si elle bien composée de n vecteurs de longueur 12 (pas l'inverse)
        """
        mfcc = self.sound.getMfcc()
        self.assertEqual(len(mfcc[0]), 12)
        self.assertEqual(mfcc.shape, (16, 12))
        self.assertAlmostEqual(mfcc[0][0], -228.14565, places=5)


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
