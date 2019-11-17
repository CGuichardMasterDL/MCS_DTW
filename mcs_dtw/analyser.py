"""
    Objectif:
        lancer une analyse (dtw ou kppv ou autre) entre deux jeux de sons.
        Donner le résultat sous forme de matrice de confusion.
"""

import random
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels


class AnalyserFramework:
    """
        framework d'analyse
    """

    def __init__(self, base_apprentissage, base_test, labels=None):
        """
            Initialiser l'objet avec une base d'apprentissage et une base de tests
            (deux listes d'objet Sound)
        """
        self.base_apprentissage = base_apprentissage
        self.base_test = base_test
        self.labels = labels
        self.taux_reco_ordre = 0.0
        self.taux_reco_ordre_et_locuteur = 0.0
        self.ordres_donnes = []
        self.ordres_predis = []
        self.confusion_matrix = []

    def analyse(self, algorithme):
        """
            Compare chaque fichier de la base de test avec la base d'apprentissage selon
            l'algorithme de la forme:
            algorithme(objetSound,baseApprentissage): ordreReconnu
        """
        self.ordres_donnes = []
        self.ordres_predis = []
        self.taux_reco_ordre = 0.0
        self.taux_reco_ordre_et_locuteur = 0.0
        for unknown_sound in self.base_test:
            self.ordres_donnes.append(unknown_sound.get_ordre())
            predicted_sound = algorithme(
                unknown_sound, self.base_apprentissage)
            self.ordres_predis.append(predicted_sound.get_ordre())
            if(unknown_sound.get_ordre() == predicted_sound.get_ordre()):
                self.taux_reco_ordre = self.taux_reco_ordre + 1.0
                if(unknown_sound.get_locuteur() == predicted_sound.get_locuteur()):
                    self.taux_reco_ordre_et_locuteur = self.taux_reco_ordre_et_locuteur + 1.0
        self.taux_reco_ordre = self.taux_reco_ordre / len(self.base_test)
        self.taux_reco_ordre_et_locuteur = self.taux_reco_ordre_et_locuteur / \
            len(self.base_test)
        self.confusion_matrix = confusion_matrix(
            self.ordres_donnes, self.ordres_predis, self.labels)
        return (self.ordres_donnes, self.ordres_predis)

    def show_confuxion_matrix(self):
        """
            Afficher la matrice de confusion
        """
        fig, ax = plt.subplots()
        im = ax.imshow(self.confusion_matrix,
                       interpolation='nearest')
        ax.figure.colorbar(im, ax=ax)
        title = "Reconnaissance d'ordre: %.2f%% / ordre + locuteur: %.2f%%" % (
            self.taux_reco_ordre*100, self.taux_reco_ordre_et_locuteur*100)
        ax.set(xticks=np.arange(self.confusion_matrix.shape[1]),
               yticks=np.arange(self.confusion_matrix.shape[0]),
               xticklabels=self.ordres_donnes, yticklabels=self.ordres_donnes,
               title=title,
               ylabel='Ordres donnés',
               xlabel='Ordres prédis')
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")
        for i in range(self.confusion_matrix.shape[0]):
            for j in range(self.confusion_matrix.shape[1]):
                ax.text(j, i, format(self.confusion_matrix[i, j], 'd'),
                        ha="center", va="center")
        fig.tight_layout()
        plt.show()


def algorithme_test(sound, base):
    """
        Disparaîtra en faveur de la dtw / kppv
    """
    return base[random.randint(0, len(base)-1)]
