import random

def gerar_cartela_bingo():
    bingo = {
        "B" : [],
        "I" : [],
        "N" : [],
        "G" : [],
        "O" : []
    }

    intervalos = {
        "B" : [1,15],
        "I" : [16,30],
        "N" : [31,45],
        "G" : [46,60],
        "O" : [61,75]
    }

    for letra in bingo:
        incio, fim = intervalos[letra]

        while len(bingo[letra]) < 5:
            numero = random.randint(incio,fim)
            if numero not in bingo[letra]:
                bingo[letra].append(numero)
    
    return bingo

def mostrar_cartela(cartela):
    for letra in cartela:
        print(letra, cartela[letra])

def mostrar_cartela(cartela):
    print(" B |  I  |  N  |  G  |  O")
    print("---------------------------")
    for i in range(5):
        print(
            f"{cartela['B'][i]:2} |  "
            f"{cartela['I'][i]:2} |  "
            f"{cartela['N'][i]:2} |  "
            f"{cartela['G'][i]:2} |  "
            f"{cartela['O'][i]:2}"
        )

cartela = gerar_cartela_bingo()
mostrar_cartela(cartela)
            
