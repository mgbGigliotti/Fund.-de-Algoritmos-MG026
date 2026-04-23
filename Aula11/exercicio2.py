seed = 12345

contagem = {}

for i in range(21):
    contagem[i] = 0

for _ in range (100):
    seed = (seed * 1103515245 + 12345) % (2**31)
    numero = seed % 21
    contagem[numero] += 1

for numero in range(21):
    print(f"{numero}: {contagem[numero]}")