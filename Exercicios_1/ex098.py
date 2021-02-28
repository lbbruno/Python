from time import sleep
def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')

def linha():
    print('-'*40)


titulo('PASSO A PASSO - Contador')


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim+1, passo):
            print(f'{c} ', end='')
    else:
        fim = fim - (passo)
        if passo > 0:
            passo = passo * -1
        if passo == 0:
            passo = -1
        for c in range(inicio, fim, passo):
            print(f'{c} ', end='')
            sleep(0.3)

    print('FIM')


i = 1
f = 10
p = 1
contador(i, f, p)
linha()
i = 10
f = -1
p = -2
contador(i, f, p)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
