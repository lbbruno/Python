vlr1 = int(input('Primeiro Valor: '))
vlr2 = int(input('Segundo Valor: '))
sair = False
while not sair:
    op = int(input('''\t[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    >>>>> Opção: '''))
    if op == 1:
        res = vlr1 + vlr2
        print('A soma entre {} e {} é igual a {}'.format(vlr1, vlr2, res))
    elif op == 2:
        res = vlr1 * vlr2
        print('A multiplicação de {} e {} é igual a {}'.format(vlr1, vlr2, res))
    elif op == 3:
        if vlr1 > vlr2:
            print('O número {} é maior'.format(vlr1))
        elif vlr2 > vlr1:
            print('O número {} é maior'.format(vlr2))
        else:
            print('Os dois números são iguais.')
    elif op == 4:
        vlr1 = int(input('Primeiro Valor: '))
        vlr2 = int(input('Segundo Valor: '))
    elif op == 5:
        sair = True
    else:
        print('Opção inválida! Tente novamente.')
    print('=-==-==-==-==-==-==-==-==-==-=')
print('Programa Finalizado com Sucesso!')
