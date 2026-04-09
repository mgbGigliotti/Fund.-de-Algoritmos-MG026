lista = []
somapar = 0
indice = 0
somaindpar = 0

for i in range(10):
    nros = int(input("Digite um número real: "))
    lista.append(nros)
    if nros % 2 == 0:
        somapar += nros

for i in range (len(lista)):
    if i % 2 == 0:
        somaindpar += lista[i]

print(somapar)
print(somaindpar)