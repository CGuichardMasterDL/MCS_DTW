# -*- coding: utf-8 -*-
"""
    Module permettant de récupérer les fichiers se trouvant dans un dossier
"""

#========== IMPORT ==========#

import os

#========== CLASSE ==========#


class ScanDir(object):
    """
        Classe servant à scanner un dossier et récupérer l'ensemble des fichiers
        le composant.
    """

    def __init__(self, folder=None):
        """LearningSet constructor"""
        if folder == "" or folder is None:
            folder = "./"
        self._folder = folder
        self._files = []
        for path, _, files in os.walk(folder):
            for file in files:
                self._files.append(path+('/' if path[-1] != '/' else '')+file)


    def _copy_all(self):
        """Copie les fichiers"""
        files = []
        for file in self._files:
            files.append(file)
        return files


    def folder(self):
        """Retourne le dossier sujet"""
        return self._folder


    def all(self):
        """Retourne tous les fichiers"""
        return self._files


    def filter(self, extension=None, pathcontains=None, name=None):
        """Filtre les fichiers"""
        files = self._copy_all()
        if extension is not None:
            files = _extension_filter(files, extension)
        if pathcontains is not None:
            files = _pathcontains_filter(files, pathcontains)
        if name is not None:
            files = _name_filter(files, name)
        return files


#======== FUNCTIONS =========#


def _extension_filter(files, extension):
    """Filtre par extension"""
    filtered_files = []
    for file in files:
        file_extension = ("".join(file.split('/')[-1])).split('.')[-1]
        if file_extension == extension:
            filtered_files.append(file)
    return filtered_files


def _pathcontains_filter(files, pathcontains):
    """Filtre par chemin"""
    filtered_files = []
    for file in files:
        if pathcontains in file:
            filtered_files.append(file)
    return filtered_files


def _name_filter(files, name):
    """Filtre par nom de fichier"""
    filtered_files = []
    for file in files:
        file_name = ".".join("".join(file.split('/')[-1]).split('.')[:-1])
        if file_name == name:
            filtered_files.append(file)
    return filtered_files
