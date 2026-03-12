linhas = int(input("informe a quantidade de linhas: "))
colunas = int(input("Informe a quantidade de colunas: "))


for i in range(linhas):
    for j in range(colunas):
        if i == 0 or i == linhas - 1 or j ==0 or j == colunas -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()



