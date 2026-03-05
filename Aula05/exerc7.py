cont = 0
acum = 0
num = 0
somatoria = 0
for x in range(10):
    num = int(input(f"Digite o {x + 1}° número: "))
    
    acum = acum + num
    cont = cont + 1
    print("Somatória: ", acum)
print("A soma de todos números digitados: ", acum)
print("Repetições: ", cont)

