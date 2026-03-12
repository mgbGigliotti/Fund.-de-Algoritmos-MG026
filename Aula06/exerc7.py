entrada = int(input("Digite um número inteiro: "))

def fibonacci(entrada):
    num = 0
    num2 = 1

    while num <= entrada:
        if num == entrada:
            return True
        
        proximo = num + num2
        num = num2
        num2 = proximo
    return False

if fibonacci(entrada):
    print("Verdadeiro (Pertence a Fibonacci)")
else:
    print("Falso (Não pertence a Fibonacci)")
        
