a = int(input("Insira um número inteiro: "))
b = int(input("Insira um número inteiro: "))
c = int(input("Insira um número inteiro: "))
if (a>b) and (a>c):
    primeiro = a
elif (b>a) and (b>c):
    primeiro = b
elif (c>a) and (c>b):
    primeiro = c
if (a>=b) and (a<=c) or (a<=b) and (a>=c):
    segundo = a
elif (b>=a) and (b<=c) or (b<=a) and(b>=c):
    segundo = b
elif (c>=a) and (c<=b) or (c<=a) and (c>=b):
    segundo = c
if (primeiro==a) and (segundo==b) or (primeiro==b) and (segundo==a):
    print(primeiro, segundo, c)
elif (primeiro==b) and (segundo==c) or (primeiro==c) and (segundo==b):
    print(primeiro, segundo, a)
elif (primeiro==c) and (segundo==a) or (primeiro==a) and (segundo==c):
    print(primeiro, segundo, b)
