arquivo = open("Aula12/contatos.txt", "w")

while True:
    nome = input("Digite o nome (vazio para parar): ")

    if nome == "":
        break

    telefone = input("Digite o telefone: ")

    arquivo.write(nome + ";" + telefone + "\n")

arquivo.close()

arquivo = open("Aula12/contatos.txt", "r")

print("\n--- CONTATOS ---")

for linha in arquivo.readlines(): #traz "nome;telefone\n"
    linha = linha.strip() #remove \n
    nome, telefone = linha.split(";") #separa nome de telefone (nome;telefone) => (nome telefone)
    print("Nome:", nome, "| Telefone:", telefone)

arquivo.close()
