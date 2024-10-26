# renvoie true si le nbr est premier et false sinon
def prem(nbr):
    if nbr == 0 or nbr == 1:
        return False
    for i in range(2, nbr):
        if nbr % i == 0:
            return False
    else:
        return True


# 4
# renvoie dictionnaire de facteurs premiers
def prd_fct(nbr: int):
    liste = [int(i) for i in range(1, int(nbr / 2)) if prem(i)]
    dico = {}
    for i in liste:
        cpt = 0
        nbr_i = int(nbr)
        while True:
            if nbr_i % i == 0:
                cpt += 1
            else:
                break
            nbr_i /= i
        if cpt != 0:
            dico[i] = cpt
    if not dico:
        dico[nbr] = 1
    return dico


# 5:renvoie le nombre de diviseur d un nombre
def nbr_div(nbr):
    if prem(nbr):
        return 1
    a = 0
    for i in prd_fct(nbr).values():
        a += i + 1
    return a


# 6:retourne la liste des diviseurs d un nombre
def list_div(nbr):
    liste = []
    for i in prd_fct(nbr):
        liste.append(i)
    for i in prd_fct(nbr):
        liste.append(int(nbr / i))
    liste.append(nbr)
    liste.append(1)
    liste.sort()

    return liste


print(nbr_div(36), list_div(36))
