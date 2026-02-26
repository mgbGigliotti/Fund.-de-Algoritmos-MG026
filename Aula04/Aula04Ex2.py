price = float(input("Insira o preço: "))
co = int(input("Insira o código de origem: "))
procedencia = str()
if (co == 1):
    procedencia="Sul"
elif (co == 2):
    procedencia="Norte"
elif (co == 3):
    procedencia="Leste"
elif(co == 4):
    procedencia="Oeste"
elif (co == 5) or (co==6):
    procedencia="Nordeste"
elif (co == 7) or (co == 8) or (co == 9):
    procedencia="Sudeste"
elif (co>=10) and (co<=20):
    procedencia="Centro-Oeste"
elif (co>=25) and (co<=30):
    procedencia="Noroeste"   
else:
    procedencia="importado"    
print(f"R$%.2f {procedencia}" %price )     
                

         
         

