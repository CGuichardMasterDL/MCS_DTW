# -*- coding: utf-8 -*-
"""
    Test de la classe Sound
"""

#========== IMPORT ==========#

import unittest
import pickle

from tests.context import path
from mcs_dtw.sound import Sound

#=========  TESTS   =========#


class TestSound(unittest.TestCase):
    """
        Test de la classe Sound
    """

    MYSOUND = Sound(path("mcs_dtw/corpus/dronevolant_bruite/M02_avance.wav"))
    SOUNDS = [
        MYSOUND,
        pickle.loads(MYSOUND.serialize())
    ]


    def test_sound_get_locuteur(self):
        """
            Vérifier si le son créé a bien le bon locuteur
        """
        for sound in TestSound.SOUNDS:
            self.assertEqual(sound.get_locuteur(), "M02")


    def test_sound_get_path(self):
        """
            Vérifier si le son créé a bien le bon path
        """
        for sound in TestSound.SOUNDS:
            self.assertTrue(
                "/corpus/dronevolant_bruite/M02_avance.wav" in sound.get_path())


    def test_sound_get_genre(self):
        """
            Vérifier si le son créé a bien le bon genre (M ou F)
        """
        for sound in TestSound.SOUNDS:
            self.assertEqual(sound.get_genre(), 'M')


    def test_sound_get_ordre(self):
        """
            Vérifier si le son créé a bien le bon ordre
        """
        for sound in TestSound.SOUNDS:
            self.assertEqual(sound.get_ordre(), "avance")


    def test_sound_is_bruite(self):
        """
            Vérifier si le son créé est bruité ou non
        """
        for sound in TestSound.SOUNDS:
            self.assertEqual(sound.is_bruite(), True)


    def test_sound_get_mfcc(self):
        """
            Vérifier si la matrice mfcc est bien construite
            Notamment si elle bien composée de n vecteurs de longueur 12 (pas l'inverse)
        """
        for sound in TestSound.SOUNDS:
            mfcc = sound.get_mfcc()
            self.assertEqual(len(mfcc[0]), 12)
            self.assertEqual(mfcc.shape, (16, 12))
            self.assertAlmostEqual(mfcc[0][0], -228.14565, places=5)


    def test_sound_get_composantes_principales(self): # pylint: disable=invalid-name
        """
            Vérifier la dimension (3,1)
        """
        for sound in TestSound.SOUNDS:
            self.assertEqual(len(sound.get_composantes_principales()), 3)

    def test_equals(self):
        """
            Test l'égalité de sons
        """
        self.assertTrue(len(TestSound.SOUNDS) >= 2 and len(TestSound.SOUNDS) % 2 == 0)
        for i in range(0, len(TestSound.SOUNDS), 2):
            sound_1 = TestSound.SOUNDS[i]
            sound_2 = TestSound.SOUNDS[i+1]
            print(sound_1.get_mfcc(), sound_2.get_mfcc(), sep="\n\n")
            self.assertTrue(sound_1 == sound_2)



#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
