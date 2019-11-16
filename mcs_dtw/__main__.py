# -*- coding: utf-8 -*-
"""
    Tester des fonctions
"""

#========== IMPORT ==========#

import glob
import mcs_dtw

from mcs_dtw.sound import Sound

#======== FUNCTIONS =========#


def get_all_files():
    """
        Récupérer tout les fichiers audios dans le dossier corpus
    """
    files = glob.glob(mcs_dtw.SRC_PATH+"/corpus/*/*.wav")
    for i in range(0, len(files) - 1):
        files[i] = Sound(files[i])
    return files


def main():
    """
        Pas vraiment du but particulier pour le moment
    """
    sound = Sound(mcs_dtw.SRC_PATH +
                  "/corpus/dronevolant_bruite/M02_avance.wav")
    print(sound.get_mfcc()[0][0])
    print(sound.get_mfcc().shape)
    print(sound.get_composantes_principales())
    print(sound.get_composantes_principales().shape)
    print(sound.serialize())
    # print(len(getAllFiles()))


#=========   EXEC   =========#

if __name__ == "__main__":
    main()
