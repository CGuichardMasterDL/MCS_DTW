"""
    Fonctions relatives à l'algorithme de dtw
"""
import math
import numpy as np
from mcs_dtw.distance import entre_fenetres_audio


def get_distance(matrix):
    """
        Formule de la distance retournée par l'algorithme dtw (g(I,J)/(I+J))
    """
    return matrix[matrix.shape[0]-1][matrix.shape[1]-1] / (matrix.shape[0]+matrix.shape[1])


def distance_de_case_a_diagonale(point_x, point_y, len_x, len_y):
    """
        Distance entre le point (point_x,point_y) et la diagonale du rectangle de taille len_x*len_y
    """
    return abs(len_x*point_y-len_y*point_x)/math.sqrt(len_x*len_x + len_y*len_y)


def dtw(sequence_i, sequence_j, distance=entre_fenetres_audio, w_0=1, w_1=1, w_2=1, d_max_diagonale=math.inf):
    """
        Comparaison dynamique entre deux séquence sequence_i et sequence_j
    """
    g = np.zeros(shape=(len(sequence_i)+1, len(sequence_j)+1))
    g[0][0] = 0

    for j in range(1, len(sequence_j)+1):
        g[0][j] = math.inf

    for i in range(1, len(sequence_i)+1):
        g[i][0] = math.inf
        for j in range(1, len(sequence_j)+1):
            if distance_de_case_a_diagonale(i, j, len(sequence_i)+1, len(sequence_j)+1) <= d_max_diagonale:
                g[i][j] = min([
                    g[i-1][j] + w_0*distance(sequence_i[i-1], sequence_j[j-1]),
                    g[i-1][j-1] + w_1 *
                    distance(sequence_i[i-1], sequence_j[j-1]),
                    g[i][j-1] + w_2*distance(sequence_i[i-1], sequence_j[j-1])
                ])
            else:
                g[i][j] = math.inf

    return (g, get_distance(g))


def find_d_max_diagonale(sequence_i, sequence_j, d=entre_fenetres_audio, w_0=1, w_1=1, w_2=1):
    """
        Trouver à partir de quelle distance de la diagonale
        le résultat de la'algorithme dtw ne change pas
    """
    valeur_distance = max(len(sequence_i), len(sequence_j))
    distance_parfaite = dtw(sequence_i, sequence_j, d, w_0, w_1, w_2)[1]
    distance = distance_parfaite
    while distance == distance_parfaite and valeur_distance >= 0:
        valeur_distance = valeur_distance-1
        distance = dtw(sequence_i, sequence_j, d, w_0,
                       w_1, w_2, valeur_distance)[1]

    return valeur_distance+1


def find_dtw_match(unknown_sound, base, params=None):
    """
        Trouve le son le plus proche de unknown_sound dans le tableau de sons passé en paramètre
    """
    match = ""
    distance_min = math.inf
    for sound in base:
        distance = dtw(unknown_sound.get_mfcc(),
                       sound.get_mfcc(), d_max_diagonale=6)[1]
        if distance < distance_min:
            match = sound
            distance_min = distance
    return match
