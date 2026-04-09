palavras = []
arei = []

while True:
    palavra = input("Digite uma palavra: ")
    
    if palavra == "":
        break
    
    if palavra not in palavras:
        palavras.append(palavra)

print("\nPalavras digitadas:")
for p in palavras:
    print(p)