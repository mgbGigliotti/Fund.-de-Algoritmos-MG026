horatrabalho = int(input("Digite o valor da hora de trabalho"))
horatrabalhada = int(input("Digite o número de horas trabalhadas no mês"))
salariobruto = horatrabalho*horatrabalhada
Ir = salariobruto*0.11
Inss = salariobruto*0.08
Sindicato = salariobruto*0.05
Salarioliquido = salariobruto-Ir-Inss-Sindicato
print("Salario Bruto: ",salariobruto)
print("IR: ",Ir)
print("INSS: ",Inss)
print("Sindicato: ",Sindicato)
print("Salário Líquido: ",Salarioliquido)
