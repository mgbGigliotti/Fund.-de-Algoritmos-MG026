# Lê o arquivo pares.txt
arquivo = open("Aula12/pares.txt", "r")

linhas = arquivo.readlines()
arquivo.close()

# Inverte a ordem das linhas
linhas_invertidas = linhas[::-1] #inverte a ordem das linhas

# Escreve no novo arquivo
saida = open("invertido.txt", "w")

for linha in linhas_invertidas:
    saida.write(linha)

saida.close()