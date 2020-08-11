def primos(a=0, b=100):
    def es_primo(n):
        for i in range(2, n-1):
            if n%i == 0:
                return False
        return True

    res = []
    for n in range(max(a,2), b+1):
        if es_primo(n):
            res.append(n)
    return res

print(primos(20, 50))
print(primos())
