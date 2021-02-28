frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Forma de Pagamento '))
print(frame)

divider = '{: <60}\n'.format('-'*40)
title1 = '1. À vista | 2. Parcelado'
title2 = '1. Dinheiro/Cheque | 2. Cartão'
title3 = '1. Parcelado em 2x | Parcelado em 3x'
opInvalida = '\033[031mOpção inválida, reinicie o programa.'


op = int(input('{}\nEscolha a forma de pagamento: '.format(title1)))
print(divider)
if op == 1:
    condicao = 'à vista'
    op = int(input('Pagamento à vista\n{}\nEscolha a forma de pagamento: '.format(title2)))
    print(divider)
    if op == 1:
        desc = 0.9  # Equivalente a 10% de desconto
    elif op == 2:
        desc = 0.95  # Equivalente a 5% de desconto
    else:
        print(opInvalida)
        exit()
elif op == 2:
    op = int(input('Pagamento parcelado no cartão\n{}\nEscolha a forma de pagamento: '.format(title3)))
    print(divider)
    if op == 1:  # Sem desconto
        condicao = 'parcelado em 2x de'
        desc = 1
    elif op == 2:
        condicao = 'parcelado em 3x de'
        desc = 1.2  # Acréscimo de 20% de juros
    else:
        print(opInvalida)
        exit()
else:
    print(opInvalida)
    exit()

vlr = float(input('Valor do produto'))
total = vlr * desc

if desc == 1:
    vlrPagto = vlr * desc / 2
elif desc > 1:
    vlrPagto = vlr * desc / 3
else:
    vlrPagto = total

print('\033[036mO valor de pagamento é de \033[033mR${:.2f} \033[036mna condição {} \033[033mR${:.2f}'.format(total, condicao, vlrPagto))