import numpy
import librosa


class Sound:
    def __init__(self, path):
        self.__path = path
        self.__locuteur = path.split('/')[-1][:3]
        self.__genre = self.__locuteur[0]
        self.__ordre = path.split('/')[-1].split('_')[1].split('.')[0]
        self.__bruite = path.split('/')[-2] == 'dronevolant_bruite'
        self.__mfcc = buildMfcc(path)

    def getPath(self):
        return self.__path

    def getLocuteur(self):
        return self.__locuteur

    def getGenre(self):
        return self.__genre

    def getOrdre(self):
        return self.__ordre

    def isBruite(self):
        return self.__bruite

    def getMfcc(self):
        return self.__mfcc


def buildMfcc(filepath):
    y, sr = librosa.load(filepath)
    return numpy.transpose(librosa.feature.mfcc(y=y, sr=sr, hop_length=1024, htk=True, n_mfcc=12))
