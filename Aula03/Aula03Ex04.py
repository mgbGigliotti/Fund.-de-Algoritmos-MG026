S = int(input("Digite o valor do seu salário: "))
if S > 1250:
    NS = 1250 * 1.10
    print("Seu novo salário é de: R$%.2f" %NS)
if S <= 1250:
    NS2 = 1250 * 1.15
    print("Seu novo salário é de: R$%.2f" %NS2)
