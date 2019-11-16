# -*- coding: utf-8 -*-
"""
    Fichier de test pour les fonctionnalités du yaml manager.
"""

#========== IMPORT ==========#

import unittest
import yaml

from tests.context import path
from mcs_dtw.yamlmanager import write_yaml, load_yaml

#=========  TESTS   =========#

class TestYamlManager(unittest.TestCase):
    """
        Classe de test pour le fichier yamlmanager de mcs_dtw.
    """

    ID = 0
    OUT = path("out/tests/")


    def get_file_name(self):
        """Get a name for a test file"""
        self.__class__.ID += 1
        return TestYamlManager.OUT + ("%s-%s.yml" % (self.__class__.__name__, self.__class__.ID))


    def test_yamlmanager_basic(self):
        """
            Test simple pour vérifier si le yamlmanager fonctionne bien.
        """
        filetest = self.get_file_name()
        data = {"a": ["pomme", "banane"],
                "b": "compote",
                "c": 5,
                "d": {"compote", "gateaux"},
                "e": {"test": True, "bonus": False}
               }
        write_yaml(filetest, data)
        data2 = load_yaml(filetest)
        self.assertEqual(data, data2)


    def test_yamlmanager_yamlerror(self):
        """
            Test si des fichiers non yaml échouent bien.
        """
        filetest = self.get_file_name()
        with open(filetest, "w") as yaml_file:
            yaml_file.write(":")
        with self.assertRaises(yaml.YAMLError):
            load_yaml(filetest)


    def test_yamlmanager_filenotfounderror(self): # pylint: disable=invalid-name
        """
            Test si des fichiers non existants échouent bien.
        """
        with self.assertRaises(FileNotFoundError):
            load_yaml(TestYamlManager.OUT+"non-existant.yml")


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
