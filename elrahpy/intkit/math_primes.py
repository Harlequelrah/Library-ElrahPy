def is_prime(number: int):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True



def factor_products(nbr: int):
    liste = [int(i) for i in range(1, int(nbr / 2)) if is_prime(i)]
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


def count_dividers(number: int):
    if is_prime(number):
        return 1
    a = 1
    for i in factor_products(number).values():
        a += i + 1
    return a

def list_dividers(number: int):
    liste = []
    for i in factor_products(number):
        liste.append(i)
    for i in factor_products(number):
        liste.append(int(number / i))
    liste.append(number)
    liste.append(1)
    liste.sort()
    return liste
