"""
Module de lecture de fichier
"""
### Imports et définition des variables globales
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = [int(s) for s in line.split(";")]
            l.append(line)
    f.close()
    return l

def get_list_k(data, k):
    """retourne la liste à l'indice k de la liste donner

    Args:
        l (list): liste de nombre

    Returns:
        l: la liste à l'indice k donner
    """
    l = []
    for x in data[k] :
        l.append(int(x))
    return l

def get_first(l):
    """retourne le premier nombre de la liste

    Args:
        l (list): liste de nombre

    Returns:
        int: le dernier nombre de la liste
    """
    return int(l[0])

def get_last(l):
    """retourne le dernier nombre de la liste

    Args:
        l (list): liste de nombre

    Returns:
        int: le dernier nombre de la liste
    """
    return l[len(l)-1]

def get_max(l):
    """retourne le nombre maximum de la liste

    Args:
        l (list): liste de nombre

    Returns:
        max: le nombre maximum de la liste
    """
    return max(l)

def get_min(l):
    """retourne le nombre minimum de la liste

    Args:
        l (list): liste de nombre

    Returns:
        min: le nombre minimum de la liste
    """
    return min(l)

def get_sum(l):
    """retourne la somme d'une liste de nombre donner

    Args:
        l (list): liste de nombre

    Returns:
        sum: la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction de lancement
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    #k = 37
    #print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()