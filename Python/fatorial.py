def fat(n):
    r = 1
    for i in range(n, 0, -1):
        r *= i
    return r

fatorial = fat(8)
print(fatorial)