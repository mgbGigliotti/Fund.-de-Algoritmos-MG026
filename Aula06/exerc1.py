qtd = int(input("Digite uma quantidade de números para serem testados: "))

i = 1
total_primos = 0

while i <= qtd:
    numero = int(input(f"Digite o número {i}: "))
    if numero > 1:
        divisor = 1
        quantidade_divisores = 0
        while divisor <= numero:
            if numero % divisor == 0:
                quantidade_divisores = quantidade_divisores + 1
                divisor = divisor + 1
        if quantidade_divisores == 2:
                 total_primos = total_primos + 1
    i=i+1
print("Você digitou ", total_primos, "números primos de um total de ", qtd, "numeros")