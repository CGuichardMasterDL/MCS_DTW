# -*- coding: utf-8 -*-
"""
    Fichier de test pour les fonctionnalités du yaml manager
"""

#========== IMPORT ==========#

import unittest
import yaml

from .context import mcs_dtw

#=========  TESTS   =========#

class TestYamlManager(unittest.TestCase):
    """
        Classe de test pour le fichier yamlmanager de mcs_dtw.
    """
    ID = 0

    def get_file_name(self):
        """Get a name for a test file"""
        self.__class__.ID += 1
        return "out/tests/%s-%s.yml" % (self.__class__.__name__, self.__class__.ID)

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
        mcs_dtw.yamlmanager.write_yaml(filetest, data)
        data2 = mcs_dtw.yamlmanager.load_yaml(filetest)
        self.assertEqual(data, data2)

    def test_yamlmanager_error(self):
        """
            Test si des fichiers non yaml échouent bien.
        """
        filetest = self.get_file_name()
        with open(filetest, "w") as yaml_file:
            yaml_file.write(":")
        with self.assertRaises(yaml.YAMLError):
            mcs_dtw.yamlmanager.load_yaml(filetest)


#=========   EXEC   =========#

if __name__ == '__main__':
    unittest.main()
