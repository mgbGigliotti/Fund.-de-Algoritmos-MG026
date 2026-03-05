maior = None
for x in range(6):
    num = int(input(f"Digite o {x + 1}° número: "))
    if maior is None or num > maior:
        maior = num
print(f"O Maior número foi: ", maior)

 