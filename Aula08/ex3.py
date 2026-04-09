z = []
maiorvalor = -99999
maiorindice = -1

# laço de repetição para criar a lista com 10 elementos digitados
for i in range(10):
    nros = int(input("Digite um número real: "))
    z.append(nros)

#laço de repetição para encontrar o maior valor e o seu índice
for i in range(len(z)):
    if z[i] > maiorvalor:
        maiorvalor = z[i]
        maiorindice = i

print("O maior valor é: ",maiorvalor)
print("E está no índice: ",maiorindice)


