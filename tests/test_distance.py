"""
    Test des fonctions de distance
"""

import unittest
import numpy
from mcs_dtw import distance


class TestDistance(unittest.TestCase):
    """
        Test de la classe Sound
    """
    fenetre_a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    fenetre_b = numpy.array([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_distance_euclidienne(self):
        """
            Test de la distance entre deux nombres abs(a-b)
        """
        self.assertEqual(distance.euclidienne(-2, 3), 5)
        self.assertEqual(distance.euclidienne(-2, -3), 1)

    def test_distance_adn(self):
        """
            Doit retourner 1 si les caractères sont différents, 0 sinon
        """
        self.assertEqual(distance.entre_sequences_adn('A', 'B'), 1)
        self.assertEqual(distance.entre_sequences_adn('A', 'A'), 0)

    def test_signaux_audios_exercice(self):
        """
            Comparer les U,V,X etc.
        """
        self.assertEqual(distance.entre_signaux_audio_exercice('U', 'V'), 1)
        self.assertEqual(distance.entre_signaux_audio_exercice('X', 'V'), 2)
        self.assertEqual(distance.entre_signaux_audio_exercice('U', 'U'), 0)

    def test_distance_fenetres_audio(self):
        """
            Test de la distance entre deux vecteurs issus de fenêtres mfcc
        """
        self.assertEqual(distance.entre_fenetres_audio(
            self.fenetre_a, self.fenetre_a), 0)
        self.assertAlmostEqual(distance.entre_fenetres_audio(
            self.fenetre_a, self.fenetre_b), 23.916521, places=5)


if __name__ == '__main__':
    unittest.main()
