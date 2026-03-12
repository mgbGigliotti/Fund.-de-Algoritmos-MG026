n = int(input("Digite o tamanho do tabuleiro: "))

for i in range(n):
    for j in range(n):
        if i>j:
            print("$",end=" ")
        else:
            print("@", end=" ")
    print()
        