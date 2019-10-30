import glob

import mcs_dtw
from mcs_dtw.sound import Sound


def getAllFiles():
    files = glob.glob(mcs_dtw.ROOT_PATH+"/corpus/*/*.wav")
    for i in range(0, len(files) - 1):
        files[i] = Sound(files[i])
    return files


def main():
    mcs_dtw.cmd_mcsdtw()
    sound = Sound(mcs_dtw.ROOT_PATH +
                  "/corpus/dronevolant_bruite/M02_avance.wav")
    print(sound.getMfcc()[0][0])
    print(sound.getMfcc().shape)
    # print(len(getAllFiles()))


if __name__ == "__main__":
    main()
