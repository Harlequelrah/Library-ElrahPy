#renvoie le nombre en binaire sans le prefixe ob
def binary(x):
    x = bin(x)
    x = x[2:]  # pour effacer le prefixe ob
    x = int(x)
    return x


#base decimal d , base hexadecimal x et base binaire b
def base_format(n, f):

    if f == "b":
        return "{0:b}".format(n)
    elif f == "h":
        return "{0:x}".format(n)
    elif f == "d":
        return "{0:d}".format(n)
    else:
        return None


