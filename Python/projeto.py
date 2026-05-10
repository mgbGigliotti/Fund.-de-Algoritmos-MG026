usuarios = [] # lista que vai guardar os usuários na memória

def load_usuario():
    arquivo = open("usuarios.txt","r")
    for linha in arquivo:
        dados = linha.strip().split(";") # remove caracteres indesejados e divide uma string em partes (remove /n e substitui por ;)
        if len(dados) == 3: # checa valor correto na linha
            id_usuario = int(dados[0]) # converte id para numero
            nome = dados[1]
            senha = dados [2]
            usuarios.append([id_usuario, nome, senha])
    arquivo.close()

def save_usuario(id_usuario, nome, senha):
    arquivo = open("usuarios.txt", "a") # escreve mantendo o conteúdo existente e adicionando ao final
    arquivo.write(f"{id_usuario};{nome};{senha}\n")
    arquivo.close()


def cadastro():
    print("\n   Cadastro")
    nome = input("Digite o seu nome de usuário: ").strip()
    senha = input("Digite uma senha: ")

    for usuario in usuarios: # verifica se o usuario ja existe 
        if usuario[1] == nome:
            print("Esse usuário já existe.")
            return

    id_usuario = len(usuarios) + 1 # criador de id
    novo_usuario = [id_usuario, nome, senha] #salva usuario como lista

    usuarios.append(novo_usuario) # adiciona na lista
    save_usuario(id_usuario, nome, senha)

    print("O seu cadastro foi realizado com sucesso.")

def login():
    print("\n   Login")
    nome = input("Digite o seu Usuário: ").strip()
    senha = input("Digite sua senha: ")
    for usuario in usuarios:
        if usuario[1] == nome and usuario[2] == senha: # verificador de login 
            print(f"Login realizado com sucesso, Bem-vindo {nome}.")
            return usuario # devolve o usuario logado
    print("Usuário ou senha inválidos.")
    return None #caso nao encontre nao retorna nada
        
def menu():
    while True:
        print("\n   MENU")
        print("1 - Cadastro")
        print("2 - Login")
        print("0 - Sair")

        opcao = input("Escolha uma opção das demais: ")
        if opcao == "1":
            cadastro()
        elif opcao == "2":
            usuario_logado = login()
            if usuario_logado:
                print("Você entrou no FEItv!")
                menu_usuario(usuario_logado)
                break
        elif opcao == "0":
            print("Você Saiu.")
            break
        else:
            print("Opção inválida!")

def menu_usuario(usuario_logado):
    while True:
        print(f"\n BEM VINDO AO FEI Tv, {usuario_logado[1]}")
        print(" 1 - Buscar Filmes ")
        print(" 2 - Histórico ")
        print(" 3 - Curtir e Descurtir Filmes Assistidos ")
        print(" 4 - Gerenciar Favoritos ")
        print(" 0 - Logout ")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            buscar_filmes(usuario_logado)
        elif opcao == "2":
            mostrar_historico(usuario_logado)
        elif opcao == "3":
            menu_curtir_descurtir(usuario_logado)
        elif opcao == "4":
            gerenciar_fav(usuario_logado)
        elif opcao == "0":
            print("Logout realizado.")
            break
        else:
            print("Opção inválida!")

filmes = []

def load_filmes():
    arquivo = open("filmes.txt","r")
    for linha in arquivo:
        dados = linha.strip().split(";") # novamente, para separar os dados 
        if len(dados) == 5: # checa valor correto na linha
            id_filme = int(dados[0])
            nome_filme = dados[1]
            duracao = int(dados[2])
            ano = int(dados[3])
            sinopse = dados[4]
            filmes.append([id_filme, nome_filme, duracao, ano, sinopse])
    arquivo.close()      

def filme(id_filme):
    for filme in filmes:
        if filme[0] == id_filme:
            return True

    return False

def catalogo():
    print("\n   CATÁLOGO DE FILMES")
    for filme in filmes:
        print(f"{filme[0]} - {filme[1]}")

def buscar_filmes(usuario_logado): 
    print("\n Catálogo de Filmes") 
    for filme in filmes: # mostra os filmes pelo ID e com ID
        print(f"{filme[0]} - {filme[1]}") 
    print("\n1 - Buscar por nome")
    print("2 - Buscar por ID")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_busca = input("Digite o nome do filme: ").strip().lower()
        encontrado = False
        for filme in filmes:
            if filme[1].lower() == nome_busca:
                print("\nFilme encontrado!")
                print(f"\n {filme[1]}")
                print(f"Ano: {filme[3]} | Duração: {filme[2]} min")
                print(f"Sinopse: {filme[4]}")

                historico(usuario_logado[0], filme[0])

                encontrado = True
                break
        if not encontrado:
            print("Este filme não está no nosso catálogo.")

    elif opcao == "2":
        id_busca = input("Digite o ID do filme: ").strip()

        if not id_busca.isdigit(): # verifica se o que foi digitado é apenas um número
            print("ID inválido.")
            return

        id_busca = int(id_busca)
        encontrado = False

        for filme in filmes:
            if filme[0] == id_busca:
                print("\nFilme encontrado!")
                print(f"\n {filme[1]}")
                print(f"Ano: {filme[3]} | Duração: {filme[2]} min")
                print(f"Sinopse: {filme[4]}")

                historico(usuario_logado[0], filme[0])

                encontrado = True
                break
        if not encontrado:
            print("Este filme não está no nosso catálogo.")
    else:
        print("Opção inválida.")

def historico(id_usuario, id_filme):
    arquivo = open("historico.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            usuario_salvo = int(dados[0])
            filme_salvo = int(dados[1])

            if usuario_salvo == id_usuario and filme_salvo == id_filme: # não salva o mesmo filme duas vezes
                arquivo.close()
                return
    arquivo.close()
    arquivo = open("historico.txt","a")
    arquivo.write(f"{id_usuario};{id_filme}\n")
    arquivo.close()

def filme_curtido(id_usuario, id_filme):
    arquivo = open("curtidos.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            usuario_salvo = int(dados[0])
            filme_salvo = int(dados[1])
            if usuario_salvo == id_usuario and filme_salvo == id_filme: # verifica se o usuario ja curtiu o filme
                arquivo.close()
                return True #curtido
    arquivo.close()
    return False # nao curtido

def mostrar_historico(usuario_logado):
    print("\nHistórico:")
    id_usuario = usuario_logado[0]
    encontrou = False # controle para saber se o usuario ja tem histórico

    arquivo = open("historico.txt","r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            usuario_salvo = int(dados[0])
            id_filme = int(dados[1])
            if usuario_salvo == id_usuario: # faz com que o usuario apenas veja o seu histórico
                for filme in filmes:
                    if filme[0] == id_filme: # encontra o filme pelo seu id na lista
                        curtido = filme_curtido(id_usuario, id_filme) # utiliza a função para verificar o curtido
                        if curtido:
                            print(f"{filme[0]} - {filme[1]}❤️")
                        else:
                            print(f"{filme[0]} - {filme[1]}")
                            encontrou = True
    arquivo.close()
    if not encontrou:
        print("Você ainda não buscou por nenhum filme.")

def curtir_filme(id_usuario, id_filme):
    if filme_curtido(id_usuario, id_filme):
        print("Esse filme já está curtido.")
        return
    arquivo = open("curtidos.txt","a")
    arquivo.write(f"{id_usuario};{id_filme}\n")
    arquivo.close()
    print("Filme curtido com sucesso!")

def descurtir_filme(id_usuario,id_filme):
    if not filme_curtido(id_usuario, id_filme):
        print("Esse filme ainda não foi curtido.")
        return
    arquivo = open("curtidos.txt", "r")
    linhas = arquivo.readlines() # cada item do arquivo txt se torna um item da lista
    arquivo.close()

    arquivo = open("curtidos.txt","w")
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            usuario_salvo = int(dados[0])
            filme_salvo = int(dados[1])
            if usuario_salvo == id_usuario and filme_salvo == id_filme:
                continue
        arquivo.write(linha)
    arquivo.close()
    print("Filme descurtido com sucesso!")

def menu_curtir_descurtir(usuario_logado):
    print("Curtir / Descurtir Filmes")
    mostrar_historico(usuario_logado)
    id_filme = input("Digite o ID do filme: ").strip()
    if not id_filme.isdigit():
        print("Não temos um filme com este ID")
        return
    id_filme = int(id_filme)
    id_usuario = usuario_logado[0]
    print("1 - Curtir")
    print("2 - Descurtir")
    print("0 - Voltar")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        curtir_filme(id_usuario, id_filme)
    elif opcao == "2":
        descurtir_filme(id_usuario, id_filme)
    elif opcao == "0":
        return
    
    else:
        print("Opção inválida.")

def gerenciar_fav(usuario_logado):
    while True:
        print("\n   GERENCIAR FAVORITOS")
        print("1 - Criar lista")
        print("2 - Editar nome da lista")
        print("3 - Excluir lista")
        print("4 - Adicionar filme à lista")
        print("5 - Remover filme da lista")
        print("6 - Ver minhas listas")
        print("7 - Ver filmes de uma lista")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_lista(usuario_logado)
        elif opcao == "2":
            editar_lista(usuario_logado)
        elif opcao == "3":
            excluir_lista(usuario_logado)
        elif opcao == "4":
            adicionar_filme_lista(usuario_logado)
        elif opcao == "5":
            remover_filme_lista(usuario_logado)
        elif opcao == "6":
            mostrar_listas(usuario_logado)
        elif opcao == "7":
            ver_filmes_da_lista(usuario_logado)
        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

def criar_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    nome_lista = input("Digite o nome da nova lista: ").strip()
    arquivo = open("listas_favoritos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    id_lista = len(linhas) + 1
    arquivo = open("listas_favoritos.txt", "a")
    arquivo.write(f"{id_lista};{id_usuario};{nome_lista}\n")
    arquivo.close()
    print(f"Lista criada com sucesso! o ID da sua lista é: {id_lista}")

def mostrar_listas(usuario_logado):
    id_usuario = usuario_logado[0]
    print("\n   SUAS LISTAS")
    arquivo = open("listas_favoritos.txt", "r")
    encontrou = False
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            id_lista = int(dados[0])
            usuario_salvo = int(dados[1])
            nome_lista = dados[2]
            if usuario_salvo == id_usuario:
                print(f"{id_lista} - {nome_lista}")
                encontrou = True
    arquivo.close()
    if not encontrou:
        print("Você ainda não possui listas.")

def editar_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    mostrar_listas(usuario_logado)
    id_lista = input("\nDigite o ID da lista: ").strip()
    if not id_lista.isdigit():
        print("ID inválido.")
        return
    id_lista = int(id_lista)
    novo_nome = input("Digite o novo nome: ").strip()
    arquivo = open("listas_favoritos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("listas_favoritos.txt", "w")
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            lista_id = int(dados[0])
            usuario_salvo = int(dados[1])
            if lista_id == id_lista and usuario_salvo == id_usuario: # só permite editar lista do próprio usuário
                arquivo.write(f"{lista_id};{usuario_salvo};{novo_nome}\n")
            else:
                arquivo.write(linha)
    arquivo.close()
    print("Lista editada com sucesso!")

def excluir_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    mostrar_listas(usuario_logado)
    id_lista = input("\nDigite o ID da lista: ").strip()
    if not id_lista.isdigit():
        print("ID inválido.")
        return
    id_lista = int(id_lista)
    arquivo = open("listas_favoritos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("listas_favoritos.txt", "w")
    encontrou = False  # controle
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            lista_id = int(dados[0])
            usuario_salvo = int(dados[1])
            if lista_id == id_lista:
                if usuario_salvo == id_usuario:
                    encontrou = True
                    continue  # remove a lista
                else:
                    print("Você não pode excluir essa lista.")
                    arquivo.write(linha)
                    arquivo.close()
                    return
        arquivo.write(linha)
    arquivo.close()

    if not encontrou:
        print("Lista não encontrada.")
        return

    arquivo = open("itens_listas.txt", "r") # remove filmes da lista
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("itens_listas.txt", "w")
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            lista_id = int(dados[0])
            if lista_id == id_lista:
                continue
        arquivo.write(linha)
    arquivo.close()
    print("Lista excluída com sucesso!")

def mostrar_filmes_da_lista(id_lista):
    print("\n   FILMES DA LISTA")
    encontrou = False
    arquivo = open("itens_listas.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            lista_id = int(dados[0])
            id_filme = int(dados[1])
            if lista_id == id_lista:
                for filme in filmes:
                    if filme[0] == id_filme:
                        print(f"{filme[0]} - {filme[1]}")
                        encontrou = True
    arquivo.close()
    if not encontrou:
        print("Essa lista não possui filmes.")

def lista_existe_do_usuario(id_usuario, id_lista):
    arquivo = open("listas_favoritos.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            lista_id = int(dados[0])
            usuario_salvo = int(dados[1])
            if lista_id == id_lista and usuario_salvo == id_usuario:
                arquivo.close()
                return True
    arquivo.close()
    return False    

def adicionar_filme_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    mostrar_listas(usuario_logado)
    catalogo()
    id_lista = input("\nDigite o ID da lista: ").strip()
    id_filme = input("Digite o ID do filme: ").strip()
    if not id_lista.isdigit() or not id_filme.isdigit():
        print("ID inválido.")
        return
    id_lista = int(id_lista)
    id_filme = int(id_filme)
    if not lista_existe_do_usuario(id_usuario, id_lista):
        print("Essa lista não existe ou não pertence a você.")
        return
    if not filme(id_filme):
        print("Esse filme não existe no catálogo.")
        return
    arquivo = open("itens_listas.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            lista_id = int(dados[0])
            filme_id = int(dados[1])
            if lista_id == id_lista and filme_id == id_filme:
                arquivo.close()
                print("Filme já está na lista.")
                return
    arquivo.close()
    arquivo = open("itens_listas.txt", "a")
    arquivo.write(f"{id_lista};{id_filme}\n")
    arquivo.close()

    print("Filme adicionado à lista!")

def remover_filme_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    mostrar_listas(usuario_logado)
    id_lista = input("\nDigite o ID da lista: ").strip()
    if not id_lista.isdigit():
        print("ID inválido.")
        return
    id_lista = int(id_lista)
    if not lista_existe_do_usuario(id_usuario, id_lista):
        print("Essa lista não existe ou não pertence a você.")
        return
    mostrar_filmes_da_lista(id_lista)

    id_filme = input("\nDigite o ID do filme que deseja remover: ").strip()

    if not id_filme.isdigit():
        print("ID inválido.")
        return
    id_filme = int(id_filme)
    arquivo = open("itens_listas.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open("itens_listas.txt", "w")
    removeu = False
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            lista_id = int(dados[0])
            filme_id = int(dados[1])
            if lista_id == id_lista and filme_id == id_filme:
                removeu = True
                continue
        arquivo.write(linha)
    arquivo.close()
    if removeu:
        print("Filme removido da lista!")
    else:
        print("Esse filme não está na lista.")

def ver_filmes_da_lista(usuario_logado):
    id_usuario = usuario_logado[0]
    mostrar_listas(usuario_logado)
    id_lista = input("\nDigite o ID da lista que deseja ver: ").strip()
    if not id_lista.isdigit():
        print("ID inválido.")
        return
    id_lista = int(id_lista)
    if not lista_existe_do_usuario(id_usuario, id_lista):
        print("Essa lista não existe ou não pertence a você.")
        return
    print("\n   FILMES DA LISTA")
    encontrou = False
    arquivo = open("itens_listas.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 2:
            lista_id = int(dados[0])
            id_filme = int(dados[1])
            if lista_id == id_lista:
                for filme in filmes:
                    if filme[0] == id_filme:
                        print(f"{filme[0]} - {filme[1]}")
                        encontrou = True
    arquivo.close()
    if not encontrou:
        print("Essa lista ainda não possui filmes.")




load_usuario()
load_filmes()
menu()