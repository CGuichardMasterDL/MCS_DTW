"""
    Test de la classe Sound
"""

import unittest
from mcs_dtw import ROOT_PATH
from mcs_dtw.sound import Sound


class TestSound(unittest.TestCase):
    """
        Test de la classe Sound
    """
    sound_path = ROOT_PATH + "/corpus/dronevolant_bruite/M02_avance.wav"

    def setUp(self):
        self.sound = Sound(self.sound_path)

    def tearDown(self):
        del self.sound

    def test_get_locuteur(self):
        """
            Vérifier si le son créé a bien le bon locuteur
        """
        self.assertEqual(self.sound.get_locuteur(), "M02")

    def test_get_path(self):
        """
            Vérifier si le son créé a bien le bon path
        """
        self.assertEqual(self.sound.get_path(), self.sound_path)

    def test_get_genre(self):
        """
            Vérifier si le son créé a bien le bon genre (M ou F)
        """
        self.assertEqual(self.sound.get_genre(), 'M')

    def test_get_ordre(self):
        """
            Vérifier si le son créé a bien le bon ordre
        """
        self.assertEqual(self.sound.get_ordre(), "avance")

    def test_is_bruite(self):
        """
            Vérifier si le son créé est bruité ou non
        """
        self.assertEqual(self.sound.is_bruite(), True)

    def test_get_mfcc(self):
        """
            Vérifier si la matrice mfcc est bien construite
            Notamment si elle bien composée de n vecteurs de longueur 12 (pas l'inverse)
        """
        mfcc = self.sound.get_mfcc()
        self.assertEqual(len(mfcc[0]), 12)
        self.assertEqual(mfcc.shape, (16, 12))
        self.assertAlmostEqual(mfcc[0][0], -228.14565, places=5)


if __name__ == '__main__':
    unittest.main()
