# -*- coding: utf-8 -*-
"""
    Tester des fonctions
"""

#========== IMPORT ==========#

import glob
import mcs_dtw
import numpy as np
import matplotlib.pyplot as plt
from mcs_dtw.sound import Sound
from mcs_dtw.learningframework import LearningFramework, show_resultats_finaux
from scipy.io import wavfile
from mpl_toolkits import mplot3d
from mcs_dtw.dtw import dtw, find_d_max_diagonale, find_dtw_match, etude_d_max_diagonale
from mcs_dtw.learningset import LearningSet
from mcs_dtw.kppv import pretraitement_acp_dual, find_dual_kppv_match, etude_valeurs_k_ordre_locuteur, show_etude_valeurs_k, affichages_effets_audios

#======== FUNCTIONS =========#


def get_all_files():
    """
        Récupérer tout les fichiers audios dans le dossier corpus
    """
    files = glob.glob(mcs_dtw.SRC_PATH+"/corpus/*/*.wav")
    sounds = []
    for file_path in files:
        sounds.append(Sound(file_path))
    return sounds


def visualize3d(sounds):
    """
        Test d'affichage 3d de points
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for sound in sounds:
        (x, y, z) = sound.get_composantes_principales()
        ax.scatter(x, y, z, c='#ff9900')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


def main():
    """
        Pas vraiment du but particulier pour le moment
    """
    files = [
        mcs_dtw.SRC_PATH + "/corpus/sans_effet/M01_avance.wav",
        mcs_dtw.SRC_PATH + "/corpus/sans_effet/F01_faisunflip.wav",
        mcs_dtw.SRC_PATH + "/corpus/hauteur_moins_50%/M05_gauche.wav",
        mcs_dtw.SRC_PATH + "/corpus/sans_effet/M10_recule.wav",
        mcs_dtw.SRC_PATH + "/corpus/hauteur_moins_50%/F02_etatdurgence.wav",
        mcs_dtw.SRC_PATH + "/corpus/hauteur_moins_50%/M07_tournedroite.wav",
    ]

    files_effets = [
        mcs_dtw.SRC_PATH + "/corpus/sans_effet/M01_avance.wav",
        mcs_dtw.SRC_PATH + "/corpus/hauteur_moins_50%/M01_avance.wav",
        mcs_dtw.SRC_PATH + "/corpus/dronevolant_nonbruite/M01_avance.wav",
        mcs_dtw.SRC_PATH + "/corpus/dronevolant_bruite/M01_avance.wav",
        mcs_dtw.SRC_PATH + "/corpus/sans_effet/M01_gauche.wav",
        mcs_dtw.SRC_PATH + "/corpus/hauteur_moins_50%/M01_gauche.wav",
        mcs_dtw.SRC_PATH + "/corpus/dronevolant_nonbruite/M01_gauche.wav",
        mcs_dtw.SRC_PATH + "/corpus/dronevolant_bruite/M01_gauche.wav",
    ]
    #base_apprentissage = [x for x in LearningSet(files=files_effets).values()]

    # base_apprentissage = [x for x in LearningSet(folder=mcs_dtw.SRC_PATH +
    #                                             "/corpus/sans_effet").values()]

    # base_test = [x for x in LearningSet(folder=mcs_dtw.SRC_PATH +
    #                                    "/corpus/hauteur_moins_50%").values()]

    # pretraitement_acp_dual(base_apprentissage)
    # affichages_effets_audios(base_apprentissage)
    #framework = LearningFramework(base_apprentissage)
    #results = etude_valeurs_k_ordre_locuteur(framework, base_test)
    # show_etude_valeurs_k(results)

    # result = framework.analyse(
    #    base_test, find_dual_kppv_match, pretraitement_acp_dual)
    #fig, ax = plt.subplots()
    #result.affichage("3/9-ppv - Hauteur moins 50%", plt, ax)
    # plt.show()
    # etude_d_max_diagonale(base_apprentissage)
    #framework.analyse_all_algorithms(base_test, printed=True, verbose=True)
    #print(find_d_max_diagonale(base_apprentissage[0].get_mfcc(), base_test[12].get_mfcc()))
    #sons_sans_effet = LearningSet(folder="./MCS_DTW/mcs_dtw/corpus/sans_effet")

    # base_apprentissage = [
    #    x for x in sons_sans_effet.values() if x.get_locuteur() == "M01"]
    # base_test = [x for x in sons_sans_effet.values()
    #             if x.get_locuteur() == "M02"]
    #framework = LearningFramework(base_apprentissage)

    #result = framework.analyse(base_test, find_dtw_match, lambda x: None)
    #fig, ax = plt.subplots()

    #result.affichage("DTW - M02 / M01 - Silences tronqués", plt, ax)
    # plt.show()

    resultats_finaux = {
        "Facteur de modification": [0.25, 0.50, 0.75, 0.85, 0.95, 1, 1.05, 1.15, 1.25, 1.50, 1.75],
        "Taux de reconnaissance totale dtw (%)": [20, 20, 30, 10, 40, 10, 90, 89, 90, 87, 11],
        "Taux de reconnaissance totale kppv (%)": [13, 67, 89, 34, 29, 48, 90, 90, 100, 2, 22],
    }

    show_resultats_finaux(resultats_finaux)


#=========   EXEC   =========#
if __name__ == "__main__":
    main()
