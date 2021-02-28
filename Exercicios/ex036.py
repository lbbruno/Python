print('=' * 30, 'Emprestimo Bancário', '=' * 30)

casaVlr = float(input('Primeiramente informe o valor do imóvel a ser comprado:'))
salario = float(input('Informe o seu salário:'))

vlrMaximoParcela = salario * 0.3  # Calcula 30% do salário que não deve ser excedido
minimoParcelas = casaVlr // vlrMaximoParcela + 1
numParcelas = int(input('Quantidade de anos:'))
parcelas = numParcelas * 12
verificacao = vlrMaximoParcela <= casaVlr / parcelas



if verificacao:
    print('\033[31mNão é possível realizar o empréstimo.')
    print('O valor da parcela excede 30% do seu salário: {:.2f}'.format(vlrMaximoParcela))
    print('\033[037m=' * 60)
    print('Condições para parcelamento neste caso')
    print('Quantidade mínima de parcelas: {:.>40}'.format(int(minimoParcelas)))
    print('Valor mínimo das parcelas: {:.>44.2f}'.format(vlrMaximoParcela))
else:
    print('\033[34mSerá possível realizar o empréstimo.')
    print('30% do salário: R${:.2f}'.format(vlrMaximoParcela))
    print('Valor do imóvel: R${:.2f}'.format(casaVlr))
    print('Quantidade de parcelas(mês): {}'.format(int(parcelas)))
    print('Valor da parcela: R${:.2f}'.format(casaVlr / parcelas))
