def dicionario(texto):
    contagem = {}
    for letra in texto:
        if letra in contagem:
           contagem[letra] += 1
        else:
            contagem[letra] = 1 

    return contagem

def comparar_dicionario(palavra1, palavra2):
    return dicionario(palavra1) == dicionario(palavra2)

def anagrama():
    p1 = input("Digite a primeira palavra: ")
    p2 = input("Digite a segunda palavra: ")

    if comparar_dicionario(p1,p2):
        print("São anagramas! ")
    else:
        print("Não são anagramas.")

anagrama()