from mychar import minusmaj


#  fonction qui prend une chaine de caractere/ liste et un caractere et renvoie une liste de toutes les occurences du caractere
def all_index(phrase_1, element):
    position = []
    for car in range(len(phrase_1)):
        if phrase_1[car] == element:
            position.append(car)
    return position


# 2:supprime toutes les occurences d un element dansune liste/chaine
def supp_all(liste, element):
    for i in range(len(liste)):
        if i in all_index(liste, element):
            del [liste[i]]
    return liste





# fonction qui renvoie True si la chaine/liste en parametre est un palindrome et False si ce n est pas un palindrome
def pal(nom):
    if nom.lower() == nom.lower()[::-1]:
        return True
    else:
        return False


# renvoie le nombre d occurence de chaque lettre dans la chaine
def nbr_let(txt, x=None):
    lettre = {}
    for i in txt:
        lettre[i] = lettre.get(i, 0) + 1
    if x == None:
        return dict(sorted(lettre.items()))
    else:
        return lettre[x]





# : pred en paramete une liste ou une chaine et renvoie la liste des majuscule et des minuscule avec un seul argument
# renvoie la liste des minuscule avec un second paramètre 0
##renvoie la liste des majuscule avec un second paramètre 1
# renvoie une liste avec le nombre de minuscule et majuscule


def casse(char_liste, casse=None):
    Up = []
    Lw = []
    m = 0
    M = 0

    for char in char_liste:
        if minusmaj(char):
            m += 1
            if char not in Lw:
                Lw.append(char)

        if not minusmaj(char):
            M += 1
            if char not in Up:
                Up.append(char)

    if casse == None:
        return sorted(Lw), sorted(Up)
    elif casse == 0:
        return sorted(Lw)
    elif casse == 1:
        return sorted(Up)
    elif casse == -1:
        return [m, M]


