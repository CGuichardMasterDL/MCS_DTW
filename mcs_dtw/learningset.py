# -*- coding: utf-8 -*-
"""
    Fichier permettant de gérer le jeu d'apprentissage lié au projet
"""

#========== IMPORT ==========#

from mcs_dtw.sound import Sound
from mcs_dtw.scandir import ScanDir
from mcs_dtw.yamlmanager import write_yaml, load_yaml

#========== CLASSE ==========#


class LearningSet(object):
    """
        Jeu d'apprentissage, généré a partir des fichiers audios.
    """

    AUDIO_FILE_EXTENSION = "wav"


    def __init__(self, folder=None, files=None, yaml_file=None):
        """LearningSet constructor"""
        self._values = set()
        if folder is not None:
            self._populate(folder=folder)
        elif files is not None:
            self._populate(files=files)
        elif yaml_file is not None:
            self._load(yaml_file=yaml_file)


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.values() == other.values()
        return False


    def _populate(self, folder=None, files=None):
        """
            Remplit le jeu d'apprentissage avec les fichiers audios se trouvant
            dans le folder, ou bien avec les fichiers audios donnés dans files.
        """
        if folder is not None:
            self.add(folder=folder)
        elif files is not None:
            self.add(files=files)


    def _load(self, yaml_file):
        """
            Charge le jeu d'apprentissage depuis un fichier yaml donné.
        """
        yaml_data = load_yaml(yaml_file)
        for data in yaml_data:
            self._add_audiofile(audiofile_values=data)


    def _add_audiofile(self, audiofile=None, audiofile_values=None):
        """
            Ajoute un fichier audio au jeu d'apprentissage
        """
        if audiofile is not None:
            self._values.add(_load_audiofile(audiofile=audiofile))
        elif audiofile_values is not None:
            self._values.add(_load_audiofile(audiofile_values=audiofile_values))


    def _audiofiles_of(self, folder):
        """
            Retourne les chemins des fichiers audio (.wav) du dossier 'folder'.
        """
        return ScanDir(folder).filter(extension=self.__class__.AUDIO_FILE_EXTENSION)


    def size(self):
        """Taille du jeu d'essai"""
        return len(self._values)


    def values(self):
        """Renvoie les sons du jeu d'essai"""
        return self._values


    def simplify(self):
        """
            Renvoie une représentation
        """
        sounds = []
        for sound in self._values:
            sound_repr = {}
            for getter in _getters(sound):
                prop = "_".join(getter.split("_")[1:])
                sound_repr[prop] = getattr(sound, getter)()
            sounds.append(sound_repr)
        return sounds


    def add(self, folder=None, file=None, files=None, yaml_file=None):
        """
            Ajoute à un jeu d'apprentissage déjà existant de nouveaux fichiers
            audio d'un dossier, ou bien juste un seul fichier audio, ou bien
            une liste de fichier.
        """
        if folder is not None:
            for f_path in self._audiofiles_of(folder=folder):
                self._add_audiofile(audiofile=f_path)
        elif file is not None:
            self._add_audiofile(audiofile=file)
        elif files is not None:
            for f_path in files:
                self._add_audiofile(audiofile=f_path)
        elif yaml_file is not None:
            self._load(yaml_file=yaml_file)
        return self


    def save(self, yaml_file):
        """
            Sauvegarde un jeu d'apprentissage dans un fichier yaml.
        """
        write_yaml(yaml_file, self.simplify())
        return self


#======== FUNCTIONS =========#


def _getters(obj):
    return [method for method in dir(obj) if "get_" in method or "is_" in method]


def _load_audiofile(audiofile=None, audiofile_values=None):
    if audiofile is not None:
        return Sound(audiofile)
    elif audiofile_values is not None:
        return Sound(values=audiofile_values)
    return None
