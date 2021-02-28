def leiaint(t):
    while True:
        n = str(input(f'{t}'))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[031mERRO! Digite um número intriro válido.\033[m')
    return n



n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')