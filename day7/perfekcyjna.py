def doskonala(n):
    suma = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0: suma = suma + i

    if suma == n: return True
    return False

doskonale = []
for i in range(2, 1000000, 2):
    if doskonala(i): doskonale.append(i)

print(doskonale)