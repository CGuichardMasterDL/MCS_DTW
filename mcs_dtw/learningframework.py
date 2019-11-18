"""
    Objectif:
        lancer une analyse (dtw ou kppv ou autre) entre deux jeux de sons.
        Afficher le résultat sous forme de matrice de confusion.
"""

import random
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels
from dtw import find_dtw_match
from kppv import find_kppv_match, pretraitement_acp
from result import Result


def algorithme_test(sound, base):
    """
        Disparaîtra en faveur de la dtw / kppv
    """
    return base[random.randint(0, len(base)-1)]


class LearningFramework:
    """
        framework d'analyse
    """

    ALGORITHMES = {
        "Programmation dynamique": (find_dtw_match, lambda x: None),
        "K plus proches voisins": (find_kppv_match, pretraitement_acp)
    }

    def __init__(self, base_apprentissage):
        """
            Initialiser l'objet avec une base d'apprentissage et une base de tests
            (deux listes d'objet Sound)
        """
        self.base_apprentissage = base_apprentissage

    def analyse(self, base_test, algorithme, pretraitement):
        """
            Compare chaque fichier de la base de test avec la base d'apprentissage selon
            l'algorithme de la forme:
            algorithme(objetSound,baseApprentissage): ordreReconnu
        """
        result = Result()
        params = pretraitement(self.base_apprentissage)
        for unknown_sound in base_test:
            predicted_sound = algorithme(
                unknown_sound, self.base_apprentissage, params)
            result.append_sounds(unknown_sound, predicted_sound)
        return result

    def analyse_all_algorithms(self, base_test, printed=False, windowed=True, verbose=False):
        """
            Exécute une analyse avec tout les algorithmes créés
            Affiche les résultats dans le terminal et/ou dans une fenêtre
        """
        plot_id = 0
        fig = plt.figure(figsize=(6*len(self.ALGORITHMES), 7))
        for key, alg in self.ALGORITHMES.items():
            plot_id += 1

            result = self.analyse(base_test, alg[0], alg[1])

            if printed:
                print("\033[1;32m\n#=========================================#\n" +
                      key+"\n#=========================================#\n\033[0;")
                result.print(verbose=verbose)
            if windowed:
                ax = plt.subplot(1, len(self.ALGORITHMES), plot_id)
                result.affichage(key, plt, ax)
        if windowed:
            fig.tight_layout()
            plt.show()
