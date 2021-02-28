from random import randint
frame = '-' * 60
print(frame)
print('{:-^60}'.format(' JOKENPÔ '))
print(frame)
op =' 1. Pedra 2. Papel 3.Tesoura'
    ## 1 = pedra 2 = papel 3 = tesoura
usr = int(input('{}\nEscolha a opção:'.format(op)))
mqn = randint(1,3)
resM = ['Pedra', 'Papel', 'Tesoura']
resU = ['Pedra', 'Papel', 'Tesoura']

if usr == mqn:
    print('Empate.')
elif (usr == 1 and mqn == 2) or (usr == 2 and mqn == 3) or (usr == 3 and mqn == 1):
        print('Maquina Venceu!')
elif (mqn == 1 and usr == 2) or (mqn == 2 and usr == 3) or (mqn == 3 and usr == 1):
    print('Você Venceu!')

print('Máquina {} | Você {}'.format(resM[mqn-1], resU[usr-1]))
