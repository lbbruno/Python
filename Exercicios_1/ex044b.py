frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Forma de Pagamento '))
print(frame)

preco = float(input('Valor das compras: '))
print('''FORMA DE PAGAMENTOS
[ 1 ] À vista em dinheiro/chque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Escolha a opção: '))
if op == 1:
    total = preco * 0.9
    print('O valor da compra é {} e com desconto é {}'.format(preco, total))
elif op == 2:
    total =  preco * 0.95
    print('O valor da compra é {} e com desconto é {}'. format(preco, total))
elif op == 3:
    print('O valor da  ompra é {} e parcelado em 2x é {}'.format(preco, preco / 2))
elif op == 4:
    qntParc = int(input('Número de prestações: '))
    total = preco * 1.2
    parcelas = total / qntParc
    print('O valor total da compra é de {} e será parcelado em {}'.format(total, parcelas))
else:
    print('Opção inválida, tente novamente.')
