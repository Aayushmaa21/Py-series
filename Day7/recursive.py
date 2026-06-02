def fibo(n):
    if n <= 0:
        return None
    elif n == 1:
        return 1

    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

print(fibo(10))