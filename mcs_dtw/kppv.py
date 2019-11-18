"""
    Algo de classification par k-plus proches voisins en utilisant la librairie sklearn
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np


def find_kppv_match(unknown_sound, base, params):
    """
        Trouve le son le plus proche de unknown_sound dans le tableau de sons passé en paramètre
    """
    (kppv, scaler, base_vectorielle) = params
    update_composantes_principales(unknown_sound, base_vectorielle, scaler)

    return base[kppv.predict([unknown_sound.get_composantes_principales()])[0]]


def pretraitement_acp(base):
    """
        Construire la base de l'espace vectoriel correspondant aux vecteurs propres
        associés aux trois plus grandes valeurs propres de la matrice de covariance
        de la base d'apprentissage

        NB:

        PCA(n_components=3) indique qu'on souhaite réduire les données en 3 dimmensions

        acp.components_ contient alors la matrice 3*12 correspondant aux n_components
        vecteurs propres

        ---> (12,1)*(3,12) ---> (1,3) un point de l'espace
    """
    learning_base = []
    for sound in base:
        learning_base.append(mean_mfcc(sound))

    scaler = StandardScaler()
    learning_base = scaler.fit_transform(learning_base)
    acp = PCA(n_components=3)
    acp.fit_transform(learning_base)

    for sound in base:
        update_composantes_principales(
            sound, np.transpose(acp.components_), scaler)

    kppv = KNeighborsClassifier(n_neighbors=1)
    data = [sound.get_composantes_principales() for sound in base]
    classes = range(len(base))
    kppv.fit(data, classes)

    return (kppv, scaler, np.transpose(acp.components_))


def mean_mfcc(sound):
    """
        Retourne le vecteur de taille 12 correspondant à la moyenne des n fenêtres
        d'une mfcc
    """
    meaned_mfcc = []
    for fenetre in np.transpose(sound.get_mfcc()):
        meaned_mfcc.append(np.mean(fenetre))
    return meaned_mfcc


def update_composantes_principales(sound, base_vectorielle, scaler):
    """
        Mise à jour des 3 coordonnées représentatives d'un son
        d'après la base vectorielle passée en paramètre
    """
    meaned_mfcc = scaler.transform([mean_mfcc(sound)])
    sound.set_composantes_principales(
        np.dot(meaned_mfcc, base_vectorielle)[0])
