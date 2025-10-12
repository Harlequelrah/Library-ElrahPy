def fibonacci(n: int):
    a, b, fib_sequence = 0, 1, []
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
