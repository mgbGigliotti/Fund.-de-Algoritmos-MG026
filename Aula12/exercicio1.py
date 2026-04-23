def gerar_arquivos():
    pares = open("Aula12/pares.txt", "w")
    impares = open("Aula12/impares.txt", "w")

    for numero in range(1000):
        if numero % 2 == 0:
            pares.write(str(numero) + "\n")
        else:
            impares.write(str(numero) + "\n")

    pares.close()
    impares.close()


gerar_arquivos()