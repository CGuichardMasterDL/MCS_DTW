"""
    Algo de classification par k-plus proches voisins en utilisant la librairie sklearn
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

k_ordre = 3
k_locuteur = 9


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


def pretraitement_acp_dual(base):
    """
        Préparer l'analyse kppv sur les ordres et sur les locuteurs
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

    kppv_ordre = KNeighborsClassifier(n_neighbors=k_ordre)
    kppv_locuteur = KNeighborsClassifier(n_neighbors=k_locuteur)

    data = [sound.get_composantes_principales() for sound in base]
    classes_ordre = [sound.get_ordre() for sound in base]
    classes_locuteur = [sound.get_locuteur() for sound in base]

    kppv_ordre.fit(data, classes_ordre)
    kppv_locuteur.fit(data, classes_locuteur)
    return (kppv_ordre, kppv_locuteur, scaler, np.transpose(acp.components_))


def find_dual_kppv_match(unknown_sound, base, params):
    """
        Trouve le son le plus proche de unknown_sound dans le tableau de sons passé en paramètre
    """
    (kppv_ordre, kppv_locuteur, scaler, base_vectorielle) = params
    update_composantes_principales(unknown_sound, base_vectorielle, scaler)

    ordre_predis = kppv_ordre.predict(
        [unknown_sound.get_composantes_principales()])[0]

    locuteur_predis = kppv_locuteur.predict(
        [unknown_sound.get_composantes_principales()])[0]

    return [x for x in base if x.get_ordre() == ordre_predis and x.get_locuteur() == locuteur_predis][0]


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


def etude_valeurs_k_ordre_locuteur(learning_framework, base_test):
    """
        Comparer l'algorithme kppv dual pour toutes les valeurs
        de 0 < k_ordre < 18 (car 18 locuteurs max par ordre dans le voisinage)
        et 0 < k_locuteur < 13 (car 13 ordres max par locuteur dans le voisinage)
    """
    data = []
    global k_ordre, k_locuteur
    original_ko = k_ordre
    original_kl = k_locuteur
    range_ordre = range(1, 19)
    range_locuteur = range(1, 14)
    for k_ordre in range_ordre:
        data_line = []
        for k_locuteur in range_locuteur:
            result = learning_framework.analyse(
                base_test, find_dual_kppv_match, pretraitement_acp_dual).get_stats()
            data_line.append(100*result[1])
        data.append(data_line)
    k_ordre = original_ko
    k_locuteur = original_kl
    return (data, range_ordre, range_locuteur)


def show_etude_valeurs_k(results):
    """
        matplotlib hell
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    Z = np.transpose(np.asarray(results[0]))
    X = np.asarray(results[1])
    Y = np.asarray(results[2])

    X, Y = np.meshgrid(X, Y)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("k_ordre")
    ax.set_ylabel("k_locuteur")
    ax.set_zlabel("Taux de reconnaissance ordre et locuteur %")

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


def affichages_effets_audios(sounds):
    """
        Afficher en 3d les points correspondants aux fichiers audios en paramètres
        En mettant en évidence les différences entre les effets audios
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    sounds_dict = {}
    for sound in sounds:
        if sound.get_locuteur()+" : "+sound.get_ordre() not in sounds_dict:
            sounds_dict[sound.get_locuteur()+" : "+sound.get_ordre()] = (
                [sound],
                [sound.get_composantes_principales()[0]],
                [sound.get_composantes_principales()[1]],
                [sound.get_composantes_principales()[2]],
            )
        else:
            sounds_dict[sound.get_locuteur()+" : "+sound.get_ordre()
                        ][0].append(sound)
            sounds_dict[sound.get_locuteur()+" : "+sound.get_ordre()
                        ][1].append(sound.get_composantes_principales()[0])
            sounds_dict[sound.get_locuteur()+" : "+sound.get_ordre()
                        ][2].append(sound.get_composantes_principales()[1])
            sounds_dict[sound.get_locuteur()+" : "+sound.get_ordre()
                        ][3].append(sound.get_composantes_principales()[2])

    for key, value in sounds_dict.items():
        ax.plot(value[1], value[2], value[3])
        ax.text(value[1][0], value[2][0], value[3][0],  '%s' % (key+"\n"+sound.get_effet()),
                size=9, zorder=1, color='k')
        for i, sound in enumerate(value[0]):
            if i != 0:
                (x, y, z) = sound.get_composantes_principales()
                ax.text(x, y, z,  '%s' % (sound.get_effet()),
                        size=8, zorder=1, color='k')

    plt.show()
