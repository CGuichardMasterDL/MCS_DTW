"""
    Objet son -> contient la matrice mfcc d'un fichier audio.
    + des informations sur le fichier (locuteur etc) utiles pour l'étude
"""
import numpy
import librosa


class Sound:
    """
        Objet son. Contient la matrice mfcc et d'autres informations.
    """

    def __init__(self, path):
        """
            Nouveau fichier son. path se termine en /bruite_ou_non/locuteur_ordre.wav
        """
        self.__path = path
        self.__locuteur = path.split('/')[-1][:3]
        self.__genre = self.__locuteur[0]
        self.__ordre = path.split('/')[-1].split('_')[1].split('.')[0]
        self.__bruite = path.split('/')[-2] == 'dronevolant_bruite'
        self.__mfcc = build_mfcc(path)

    def get_path(self):
        """
            Retourne l'adresse du fichier son
        """
        return self.__path

    def get_locuteur(self):
        """
            Retourne le locuteur du son (ex M01,F02 etc)
        """
        return self.__locuteur

    def get_genre(self):
        """
            'M' ou 'F'
        """
        return self.__genre

    def get_ordre(self):
        """
            Retourne l'ordre dicté dans le fichier (ex avance...)
        """
        return self.__ordre

    def is_bruite(self):
        """
            True si le fichier est bruité
        """
        return self.__bruite

    def get_mfcc(self):
        """
            Retourne la matrice mfcc associée au son
        """
        return self.__mfcc


def build_mfcc(filepath):
    """
        Calcule la matrice mfcc asoociée au son
    """
    y, sr = librosa.load(filepath)  # pylint: disable=invalid-name
    return numpy.transpose(librosa.feature.mfcc(y=y, sr=sr, hop_length=1024, htk=True, n_mfcc=12))
