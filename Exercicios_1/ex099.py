from time import sleep
def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')

def linha():
    print('-'*40)


from random import randint
titulo('Descobrindo o Maior Número')
maior = 0
menor = 0

def maior(*num):
    if len(num) > 0:
        print('Analizando os valores...')
        for i in num:
            print(f'{i} ', end='')
            sleep(0.5)
        print(f'Foram encontrados {len(num)} valores.')

        for i, n in enumerate(num):
            if i == 0:
                maior = n
            else:
                if n > maior:
                    maior = n
        print(f'maior valor: {maior}')
    else:
        print('Não foi recebido nenhum parâmetro')


#Principal
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
n6 = randint(1, 10)
maior(n1, n2, n3, n4, n5, n6)
linha()
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
maior(n1, n2, n3)
linha()
n1 = randint(1, 10)
n2 = randint(1, 10)
maior(n1, n2)
n1 = randint(1, 10)
maior(n1)
linha()
maior()
linha()


