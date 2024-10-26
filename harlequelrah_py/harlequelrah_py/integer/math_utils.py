

#renvoie la sequence de fibonacci de 1 jusqu'au nombre entré en paramètre


def fibonacci(n):
    a, b, fib_sequence = 0, 1, []
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# renvoie le factoriel d un nombre
def fct(n):

    if n == 0:
        return 1
    else:
        return n * fct(n - 1)
