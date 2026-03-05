cont= 0
acum = 0
while True:
 entrada = int(input("Digite alguns números ou 0 pra terminar: "))
 if entrada == 0:
  med = acum/cont
  print("Quantos números foram digitado: ", cont)
  print("A soma de todos números digitados: ", acum)
  print("Média aritmética dos números %.2f" % med)
  break
 else:
  cont = cont + 1
  acum = acum + entrada



 