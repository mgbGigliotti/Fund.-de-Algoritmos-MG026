import random

def simular_dados():
    resultados = []

    for x in range(1000):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        soma = dado1 + dado2
        resultados.append(soma)

    return resultados

def a_resultados(resultados):
    contagem = {}
    for i in range (2,13):
        contagem[i] = 0
    for valor in resultados:
        contagem[valor] += 1
    
    return contagem

def exibir_tabela(contagem,total):
    print("Resultado | Frequência (%)")

    for soma in range(2,13):
        porcentagem = (contagem[soma] / total) * 100
        print(f"{soma:9} | {porcentagem:10.2f}%")

def principal():
    resultados = simular_dados()
    contagem = a_resultados(resultados)
    exibir_tabela(contagem, len(resultados))

principal()