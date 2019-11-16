# -*- coding: utf-8 -*-
"""
    Ce module sert à écrire des fichiers yaml, ainsi que les charger.
"""

#========== IMPORT ==========#

import yaml

#======== FUNCTIONS =========#


def write_yaml(filepath, data):
    """
        Ce fichier écrit data sous format yaml dans filepath.
    """
    with open(filepath, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)


def load_yaml(filepath):
    """
        Charge un fichier yaml dans python.
    """
    with open(filepath, 'r') as stream:
        return yaml.load(stream, Loader=yaml.Loader)
