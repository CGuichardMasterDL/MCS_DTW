# -*- coding: utf-8 -*-
"""
    Objet contenant les résultats d'une comparaison entre
    base de test et base d'apprentissage
"""

#========== IMPORT ==========#

import numpy as np

from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

#========== CLASSE ==========#


class Result(object):
    """
        Objet contenant les résultats d'une comparaison entre
        base de test et base d'apprentissage
    """

    def __init__(self, verbose=True):
        """
            Constructor
        """
        self.sons_donnes = []
        self.sons_predis = []
        self.ordres_donnes = []
        self.ordres_predis = []
        self.verbose = verbose


    def append_sounds(self, son_donne, son_predis):
        """
            Ajoute une correspondnace netre deux sons
        """
        self.sons_donnes.append(son_donne)
        self.sons_predis.append(son_predis)
        self.ordres_donnes.append(son_donne.get_ordre())
        self.ordres_predis.append(son_predis.get_ordre())
        if self.verbose:
            _print_line(son_donne, son_predis)


    def get_confusion_matrix(self):
        """
            Retourne la matrice de confusion du système
        """
        return confusion_matrix(self.ordres_donnes, self.ordres_predis)


    def get_stats(self):
        """
            Retourne:
                le taux de reco du bon ordres
                le taux de reco du bon ordre + bon locuteur
                le nb d'erreurs sur l'ordre
                le nb d'erreurs sur l'ordre et le locuteur
        """
        taux_ordre = 0.0
        taux_ordre_locuteur = 0.0
        for i in range(len(self.ordres_donnes)):
            if self.ordres_donnes[i] == self.ordres_predis[i]:
                taux_ordre += 1.0
                if self.sons_donnes[i].get_locuteur() == self.sons_predis[i].get_locuteur():
                    taux_ordre_locuteur += 1.0

        return (
            taux_ordre/len(self.ordres_donnes),
            taux_ordre_locuteur/len(self.ordres_donnes),
            int(len(self.ordres_donnes)-taux_ordre),
            int(len(self.ordres_donnes)-taux_ordre_locuteur)
        )


    def get_formatted_stats(self):
        """
            Utilisé pour l'affichage des statistiques dans matplotlib et dans le terminal
        """
        stats = self.get_stats()
        return "%d sons testés\n" % (len(self.sons_donnes)) \
        + "Taux de reconnaissance sur l'ordre : %.2f%% (%d erreurs)\n" % ((stats[0]*100), stats[2])\
        + "Taux de reconnaissance sur l'ordre et le locuteur : %.2f%% (%d erreurs)\n" % (
            (stats[1]*100), stats[3])


    def print(self):
        """
            Afficher les résultats dans le terminal
        """

        print(
            "\n\033[1;35m#======       RÉSULTATS        =====#\033[0m\n\033[0;36m")
        print(self.get_formatted_stats(), end='\n\033[0m')


    def affichage(self, title, plt, axes):
        """
            Set up de l'affichage des résultats dans matplotlib
        """

        c_matrix = confusion_matrix(self.ordres_donnes, self.ordres_predis)
        classes = unique_labels(self.ordres_donnes)
        axes.imshow(c_matrix, interpolation='nearest', cmap=plt.cm.Blues)
        axes.set(xticks=np.arange(c_matrix.shape[1]),
                 yticks=np.arange(c_matrix.shape[0]))

        axes.set_xlabel('Ordres prédis', fontsize=10)
        axes.set_ylabel('Ordres donnés', fontsize=10)
        axes.set_xticklabels(classes, fontsize=8)
        axes.set_yticklabels(classes, fontsize=8)

        axes.set_title(title+"\n"+self.get_formatted_stats(),
                       fontsize=10, pad=10.0)
        plt.setp(axes.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")
        for i in range(c_matrix.shape[0]):
            for j in range(c_matrix.shape[1]):
                axes.text(j, i, format(c_matrix[i, j], 'd'),
                          ha="center", va="center")


#======== FUNCTIONS =========#


def _print_line(son_donne, son_predis):
    """
        Affichage d'une comparaison
    """
    if son_donne.get_ordre() == son_predis.get_ordre():
        print("\033[0;33m", end='')
        if son_donne.get_locuteur() == son_predis.get_locuteur():
            print("\033[0;32m", end='')
    else:
        print("\033[0;31m", end='')
        print("{0} : {1}     \t a été reconnu comme étant\t {2} : {3}\033[0m"
              .format(
                  son_donne.get_locuteur(),
                  son_donne.get_ordre(),
                  son_predis.get_locuteur(),
                  son_predis.get_ordre()
              )
             )
