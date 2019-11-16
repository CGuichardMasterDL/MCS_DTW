# -*- coding: utf-8 -*-
"""
    Objet son -> contient la matrice mfcc d'un fichier audio.
    + des informations sur le fichier (locuteur etc) utiles pour l'étude
"""

#========== IMPORT ==========#

import pickle
import numpy
import librosa

from sklearn.decomposition import PCA

#========== CLASSE ==========#


class Sound:
    """
        Objet son. Contient la matrice mfcc et d'autres informations.
    """

    def __init__(self, path=None, values=None):
        """
            Nouveau fichier son. path se termine en /bruite_ou_non/locuteur_ordre.wav
        """
        if path is not None:
            self._path = path
            self._locuteur = path.split('/')[-1][:3]
            self._genre = self._locuteur[0]
            self._ordre = path.split('/')[-1].split('_')[1].split('.')[0]
            self._bruite = path.split('/')[-2] == 'dronevolant_bruite'
            self._mfcc = _build_mfcc(path)
            self._composantes_principales = PCA(
                n_components=3).fit(self._mfcc).singular_values_
        elif values is not None:
            for value in values.keys():
                setattr(self, '_'+value, values[value])


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_path() == other.get_path() and \
                self.get_locuteur() == other.get_locuteur() and \
                self.get_genre() == other.get_genre() and \
                self.get_ordre() == other.get_ordre() and \
                self.is_bruite() == other.is_bruite() and \
                (self.get_mfcc() == other.get_mfcc()).all()
        return False


    def __hash__(self):
        return hash(self.get_mfcc().tostring())


    def get_path(self):
        """
            Retourne l'adresse du fichier son
        """
        return self._path


    def get_locuteur(self):
        """
            Retourne le locuteur du son (ex M01,F02 etc)
        """
        return self._locuteur


    def get_genre(self):
        """
            'M' ou 'F'
        """
        return self._genre


    def get_ordre(self):
        """
            Retourne l'ordre dicté dans le fichier (ex avance...)
        """
        return self._ordre


    def is_bruite(self):
        """
            True si le fichier est bruité
        """
        return self._bruite


    def get_mfcc(self):
        """
            Retourne la matrice mfcc associée au son
        """
        return self._mfcc


    def get_composantes_principales(self):
        """
            Retourne les composantes principles d'un son (veteur (3,1))
        """
        return self._composantes_principales


    def serialize(self):
        """
            Serilisation (retourne un bytes)
        """
        return pickle.dumps(self)


#======== FUNCTIONS =========#


def _build_mfcc(filepath):
    """
        Calcule la matrice mfcc asoociée au son
    """
    y, sr = librosa.load(filepath)  # pylint: disable=invalid-name
    return numpy.transpose(librosa.feature.mfcc(y=y, sr=sr, hop_length=1024, htk=True, n_mfcc=12))
