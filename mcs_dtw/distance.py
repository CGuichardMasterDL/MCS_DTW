# -*- coding: utf-8 -*-
"""
    Fonctions de distance utilisées dans le TP
"""

#========== IMPORT ==========#

import numpy

#======== FUNCTIONS =========#


def euclidienne(num_a, num_b):
    """
        Distance euclidienne
    """
    return abs(num_a-num_b)


def entre_sequences_adn(char_a, char_b):
    """
        Distance entre deux séquences ADN (cf TD1)
    """
    if char_a == char_b:
        return 0
    return 1


def entre_signaux_audio_exercice(char_a, char_b):
    """
        Distance entre deux signaux audio (cf TD1)
    """
    if char_a == char_b:
        return 0
    if char_a == 'V' and char_b != 'U' or char_b == 'V' and char_a != 'U':
        return 2
    return 1


def entre_fenetres_audio(vec_a, vec_b):
    """
        Distance entre deux fenetres audios (vecteur de longueur 12 d'une mfcc)
    """
    vec_c = vec_b - vec_a
    return numpy.linalg.norm(vec_c)
