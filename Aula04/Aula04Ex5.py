anonasc = int(input("Digite o ano do seu nascimento: "))
anoatual = int(input("Digite o ano atual: "))
Idade = anoatual - anonasc
if (Idade>=18):
    print("Você ja pode tirar sua carteira de habilitação e seu título de voto!")
elif (Idade>=16):
    print("Você pode tirar apenas seu título eleitoral")
else: 
    print("Você ainda não tem idade suficiente para tirar seu título eleitoral e carteira de habilitação")
 
 
