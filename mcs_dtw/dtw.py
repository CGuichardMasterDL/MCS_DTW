# -*- coding: utf-8 -*-
"""
    Fonctions relatives à l'algorithme de dtw
"""

#========== IMPORT ==========#

import math
import numpy as np
import matplotlib.pyplot as plt

from mcs_dtw.distance import entre_fenetres_audio

#======== FUNCTIONS =========#


def get_distance(matrix):
    """
        Formule de la distance retournée par l'algorithme dtw (g(I,J)/(I+J))
    """
    return matrix[matrix.shape[0]-1][matrix.shape[1]-1] / (matrix.shape[0]+matrix.shape[1])


def get_path(matrix):
    """
        Déterminer le chemin optimal
    """
    i = matrix.shape[0]-1
    j = matrix.shape[1]-1
    path = [(i, j)]
    while i != 0 and j != 0:
        val1 = matrix[i-1][j]
        val2 = matrix[i-1][j-1]
        val3 = matrix[i][j-1]
        minimum = min([val1, val2, val3])
        if minimum == val1:
            i -= 1
        elif minimum == val2:
            i -= 1
            j -= 1
        else:
            j -= 1
        path.append((i, j))
    return path


def distance_de_case_a_diagonale(point_x, point_y, len_x, len_y):
    """
        Distance entre le point (point_x,point_y) et la diagonale du rectangle de taille len_x*len_y
    """
    return abs(len_x*point_y-len_y*point_x)/math.sqrt(len_x*len_x + len_y*len_y)


def dtw(sequence_i, sequence_j, distance=entre_fenetres_audio, # pylint: disable=R0913
        w_0=1, w_1=1, w_2=1, d_max_diagonale=math.inf):
    """
        Comparaison dynamique entre deux séquence sequence_i et sequence_j
    """
    g_mat = np.zeros(shape=(len(sequence_i)+1, len(sequence_j)+1))
    g_mat[0][0] = 0

    for j in range(1, len(sequence_j)+1):
        g_mat[0][j] = math.inf

    for i in range(1, len(sequence_i)+1):
        g_mat[i][0] = math.inf
        for j in range(1, len(sequence_j)+1):
            if distance_de_case_a_diagonale(i, j, len(sequence_i)+1,
                                            len(sequence_j)+1) <= d_max_diagonale:
                g_mat[i][j] = min([
                    g_mat[i-1][j] + w_0*distance(sequence_i[i-1], sequence_j[j-1]),
                    g_mat[i-1][j-1] + w_1 *
                    distance(sequence_i[i-1], sequence_j[j-1]),
                    g_mat[i][j-1] + w_2*distance(sequence_i[i-1], sequence_j[j-1])
                ])
            else:
                g_mat[i][j] = math.inf

    return (g_mat, get_distance(g_mat), get_path(g_mat))


def find_dtw_match(unknown_sound, base, params=None): # pylint: disable=W0613
    """
        Trouve le son le plus proche de unknown_sound dans le tableau de sons passé en paramètre
    """
    match = ""
    d_diagonale = 7
    distance_min = math.inf
    for sound in base:
        distance = dtw(unknown_sound.get_mfcc(),
                       sound.get_mfcc(), d_max_diagonale=d_diagonale)[1]
        if distance < distance_min:
            match = sound
            distance_min = distance
    return match


def find_d_max_diagonale(sequence_i, sequence_j, # pylint: disable=R0913
                         dist_func=entre_fenetres_audio, w_0=1, w_1=1, w_2=1):
    """
        Trouver à partir de quelle distance de la diagonale
        le résultat de la'algorithme dtw ne change pas
    """
    valeur_distance = max(len(sequence_i), len(sequence_j))
    distance_parfaite = dtw(sequence_i, sequence_j, dist_func, w_0, w_1, w_2)[1]
    distance = distance_parfaite
    while distance == distance_parfaite and valeur_distance >= 0:
        valeur_distance = valeur_distance-1
        distance = dtw(sequence_i, sequence_j, dist_func, w_0,
                       w_1, w_2, valeur_distance)[1]

    return valeur_distance+1


def etude_d_max_diagonale(sounds):
    """
        Appliquer find_d_max_diagonale pour chaque couple de valeurs de la base en paramètre
        le représenter dans matplotlib
    """
    x_ticks = []
    matrix = []
    for x_sound in sounds:
        x_ticks.append(x_sound.get_locuteur()+" : "+x_sound.get_ordre())
        matrix_line = []
        for y_sound in sounds:
            matrix_line.append(find_d_max_diagonale(
                x_sound.get_mfcc(), y_sound.get_mfcc()))
        matrix.append(matrix_line)
    matrix = np.asarray(np.asarray(matrix))

    _, axes = plt.subplots()

    ims = axes.imshow(matrix, interpolation='nearest', cmap=plt.cm.Reds) # pylint: disable=E1101
    axes.figure.colorbar(ims, ax=axes)

    axes.set(xticks=np.arange(matrix.shape[1]),
             yticks=np.arange(matrix.shape[0]))

    axes.set_yticklabels(x_ticks, fontsize=7)
    axes.set_xticklabels(x_ticks, fontsize=7)
    axes.set_title("Distance maximale de la diagonale")
    plt.setp(axes.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            axes.text(j, i, format(matrix[i, j], 'd'),
                      ha="center", va="center")

    plt.show()
