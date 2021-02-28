div = '-'*30
print(div)
print('      LOJA ATRAVESSADÃO')
print(div)
totalCompra = totMaior1000 = menorPreco = cont = 0
nomeProd = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    resp =' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    totalCompra += preco
    if preco >= 1000:
        totMaior1000 += 1
    cont += 1
    if cont == 1:
        nomeProd
        menorPreco = preco
    else:
        if preco < menorPreco:
            nomeProd
            menorPreco = preco
    if resp in 'N':
        break
print(f'Total da compra: R$ {totalCompra:.2f}')
print(f'Produtos com preço maior que R$ 1000.00: {totMaior1000}')
print(f'Produto com menor preço: {nomeProd} custando: R$ {menorPreco}')
print('FIM')
