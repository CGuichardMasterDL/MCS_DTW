# -*- coding: utf-8 -*-
"""
    Module de test pour les fonctionnalités de scandir
"""

#========== IMPORT ==========#

import unittest

from tests.context import path
from mcs_dtw.learningset import LearningSet
from mcs_dtw.scandir import ScanDir

#=========  TESTS   =========#


class TestLearningSet(unittest.TestCase):
    """
        Classe de test pour le fichier yamlmanager de mcs_dtw.
    """

    CORPUS = path("corpus/")
    YAML_TEST = path("out/tests/TestLearningSet-1.yml")

    LS1 = LearningSet()
    LS2 = LearningSet(folder=CORPUS+"dronevolant_nonbruite").save(YAML_TEST)
    LS3 = LearningSet(yaml_file=YAML_TEST)
    LS4 = LearningSet().add(folder=CORPUS+"dronevolant_nonbruite")
    LS5 = LearningSet(files=ScanDir(CORPUS+"dronevolant_nonbruite")
                      .filter(extension=LearningSet.AUDIO_FILE_EXTENSION))


    def test_learningset_contruct(self):
        """
            Test le constructeur du LearningSet
        """
        self.assertTrue(TestLearningSet.LS1.size() == 0)
        self.assertTrue(TestLearningSet.LS2.size() > 0)
        self.assertTrue(TestLearningSet.LS3.size() > 0)
        self.assertTrue(TestLearningSet.LS4.size() > 0)
        self.assertTrue(TestLearningSet.LS5.size() > 0)


    def test_equals(self):
        """
            Test d'égalité des LearningSet
        """
        self.assertTrue(TestLearningSet.LS1 != TestLearningSet.LS2)
        self.assertTrue(TestLearningSet.LS2 == TestLearningSet.LS3)
        self.assertTrue(TestLearningSet.LS2 == TestLearningSet.LS4)
        self.assertTrue(TestLearningSet.LS2 == TestLearningSet.LS5)


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
