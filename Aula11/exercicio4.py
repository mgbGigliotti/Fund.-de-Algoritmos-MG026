def contagem_unica(texto):
    contagem = {}
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
        
    return len(contagem)


def principal():
    texto = input("Digite uma frase: ")
    resultado = contagem_unica(texto)
    print("Número de caracteres únicos: ", resultado)

principal()
