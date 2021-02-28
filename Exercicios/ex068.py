from random import randint
print('Vamos jogar PAR OU IMPAR!')
print('-==-'*5)

cont = vitorias= 0
while True:
    # Usuário escolhe um número..
    numusr = int(input('Escolha um número: '))
    # Usuário escolhe par ou impra..
    escolhausr = str(input('Par ou impar [P/I]')).upper().strip()
    # Computador escolhe um número
    numcomp = randint(1,10)
    # Computador define par ou impar de acordo com a escolha do usuário
    escolhacomp = ''
    if escolhausr == 'P':
        escolhacomp = 'I'
    else:
        escolhacomp = 'P'

    # Soma e verifica o resto; se 0 par se não impar.
    '''# Já calcula também squem foi o ganhador; Computador vence se condição é verdadeira
    Se a condição for falsa o usuário vence.'''

    res = (numcomp + numusr) % 2
    if res == 0 and escolhacomp =='P':
        print('VOCE PERDEU!!')
    elif res != 0 and escolhacomp == 'I':
        print('VOCÊ PERDEU!!')
    else:
        print('VOCÊ VENCEU!!')
        vitorias += 1
    print('-'*20)
    print(f'Você jogou {numusr} e o computador escolheu {numcomp}.')
    print('-' * 20)
    cont += 1
    if cont == 3:
        break
    print('Vamos jogar novamente...')
    print('-==-'*5)
print('-==-'*5)
print(f'GAME OVER!!! Você venceu {vitorias} vez(es)')