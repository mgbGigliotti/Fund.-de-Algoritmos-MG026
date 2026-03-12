N = int(input("Digite um numero inteiro natural positivo: "))

def contadordigitos (n):
    contador = 0
    while n > 0:
        n = n // 10
        contador = contador + 1
    return contador

resultado = contadordigitos(N)

print("Quantidade de Dígitos: ", resultado)        


