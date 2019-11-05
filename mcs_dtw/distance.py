"""
    Fonctions de distance utilisées dans le TP
"""


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
