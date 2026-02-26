altura = float (input("Digie a sua altura: "))
sexo = str(input("Digite (M) para Masculino e (F) para Feminino: ")).upper()
if(sexo=="M"):
    pi=(72.7 * altura) - 58
    print("Seu preso ideal seria de: %.2f kg"%pi)
elif (sexo=="F"):
    pi=(62.1 * altura) - 44.7
    print("Seu peso ideal seria de: %.2f kg"%pi)
else:
    print("Digite apenas entre (M) e (F)")










   
 