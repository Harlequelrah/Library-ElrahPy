import string

printables = string.printable
range_interval = len(string.printable)


def crypt_cesar(word: str, operation: int = 1 | -1, k=3):
    result = ""
    for i in word:
        if i in printables:
            result += printables[(printables.index(i) + k * operation) % range_interval]
        else:
            result += i
    return result


def verify_cesar(word: str, crypted_word: str, k: int):
    expected_crypted_word = crypt_cesar(word=word, operation=1, k=k)
    return crypted_word == expected_crypted_word


def search_cesar(word: str):
    dic = {}
    for i in range(range_interval):
        dic[crypt_cesar(word, -1, i)] = i
    return dic


def z_cesar(chaine):

    if chaine.isspace() == False:
        dico = {}
        for a in range(range_interval):
            l = []
            for i in chaine.split(" "):
                for j, k in search_cesar(i).items():
                    if a == k:
                        l.append(j)
            if l:
                dico[a] = " ".join(l)
        return dico
    else:
        return search_cesar(chaine)
