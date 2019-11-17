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
from mcs_dtw.analyser import AnalyserFramework, algorithme_test
from scipy.io import wavfile
from mpl_toolkits import mplot3d

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
    # sound = Sound(mcs_dtw.ROOT_PATH +"/corpus/dronevolant_bruite/M02_avance.wav")
    # print(vars(sound))
    # fech, audio = wavfile.read(mcs_dtw.ROOT_PATH +
    #                           "/corpus/dronevolant_bruite/M02_avance.wav")
    # plt.figure()

    # plt.plot(np.arange(audio)/fech, audio)
    # plt.xlabel('temps (s)')
    # plt.ylabel('Amplitude')
    # plt.title('Signal audio')
    # plt.grid(True)
    # plt.show()
    # print(sound.get_composantes_principales())
    # print(sound.serialize())
    # print(len(getAllFiles()))
    #files = get_all_files()
    # base_apprentissage = [sound for sound in files
    #                      if sound.get_locuteur() == 'M01' and not sound.is_bruite()]
    # base_test = [sound for sound in files
    #             if sound.get_locuteur() == 'M01' and not sound.is_bruite()]
    # analyser = AnalyserFramework(base_apprentissage, base_test)
    # print(analyser.analyse(algorithme_test))
    # analyser.show_confuxion_matrix()
    # visualize3d(files)
    print('you')


#=========   EXEC   =========#

if __name__ == "__main__":
    main()
