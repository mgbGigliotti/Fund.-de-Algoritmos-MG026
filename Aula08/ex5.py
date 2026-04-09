n = int(input("Digite a qtde de numeros: "))
numeros = []

for i in range(n):
    num = int(input("Digite um numero: "))
    numeros.append(num)

print(f"\nNumeros: {numeros}")
print("Inverso:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])