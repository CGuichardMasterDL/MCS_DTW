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
from mcs_dtw.learningframework import LearningFramework, algorithme_test
from scipy.io import wavfile
from mpl_toolkits import mplot3d
from mcs_dtw.dtw import dtw, find_d_max_diagonale, find_dtw_match
from mcs_dtw.learningset import LearningSet
from mcs_dtw.kppv import pretraitement_acp

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
    sound_base = LearningSet(folder=mcs_dtw.SRC_PATH +
                             "/corpus/dronevolant_nonbruite")
    base_apprentissage = [
        sound for sound in sound_base.values() if sound.get_locuteur() == 'M01']

    base_test = [sound for sound in sound_base.values()
                 if sound.get_locuteur() == 'M02']

    framework = LearningFramework(base_apprentissage)
    framework.analyse_all_algorithms(base_test, printed=True, verbose=True)
    #print(find_d_max_diagonale(base_apprentissage[0].get_mfcc(), base_test[12].get_mfcc()))


#=========   EXEC   =========#
if __name__ == "__main__":
    main()
