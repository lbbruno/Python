n1 = int(input('Digite primero número:'))
n2 = int(input('Digite segundo número:'))
n3 = int(input('Digite terceiro número:'))
if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
elif n2 > n3:
    print(n2)
else:
    print(n3)