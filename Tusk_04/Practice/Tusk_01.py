n = 7
fib = {0: 0, 1: 1}

def fibFunc(n):
    if n not in fib:
        fib[n] = fibFunc(n - 1) + fibFunc(n - 2)
    return fib[n]

print(fibFunc(n))
print(fib.values())