d = {
    "alpha" : 1,
    "bravo" : 2,
    "charlie" : 1,
    "delta" : 3,
    "echo" : 1
}

def procuraChave():
    valor = int(input("Digite o valor que deseja buscar: "))
    chaves_encontradas = []
    for chave, v in d.items():
        if v == valor:
            chaves_encontradas.append(chave)
    if chaves_encontradas:
        print(f"Procurando chaves com valor {valor}: ")
        print(chaves_encontradas)
    else:
        print("Nenhuma chave encontrada.")
                
    return

procuraChave()
            
           


            
        
    


