arquivo = open("Aula12/text.txt", "r")

for linha in arquivo.readlines():
    print(linha)
arquivo.close()