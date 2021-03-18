import os

def cabecalho(titulo):
    """
    -> Cabeçalho do programa.
    :param titulo: Titulo do programa
    :return: 
    """
    div =  '=' * int(len(titulo) + 10)
    print(f'{div}\n==== {titulo} ====\n{div}')

def tabela(dolar, euro, real):
    """ - Formatação em tabela para exibição da cotação.
    :param dolar:
    :param euro:
    :param real:
    :return:
    """
    print('\033[036m')
    print('|{:^10}|{:^10}|{:^10}|'.format('Dolar', 'Euro', 'Real'))
    print('|{:^10.2f}|{:^10.2f}|{:^10.2f}|'.format(dolar, euro, real))
    print('\033[039m')


def conversor(dolar, euro, real, op):
    """ -> Converte os valores
    :param dolar: novo valor dolar para ser convertido
    :param euro: novo valor euro para ser convertido
    :param real: novo valor real para ser convertido
    :param op: 1 - é convertido de real para dolar e euro.
               2 - é convertido de dolar para real e euro.
               3 - é convertido de euro para dolar e real.
    :return:
    """
    global dolar_dia
    global euro_dia

    if op == 0 or op == 1:
        dolar = dolar_dia * r
        euro = euro_dia * r
    elif op == 2:
        real = dolar / dolar_dia
        euro = euro_dia * r
    else:
        real = e / euro_dia
        dolar = dolar * dolar_dia

    tabela(dolar, euro, real)



dolar_dia = 5.54  # float(input('Informe o valor do Dollar:'))
euro_dia = 6.53  # float(input('Informe o valor do euro_dia:'))

d = dolar_dia
e = euro_dia
r = 1
op = 0
while (True):
    cabecalho('Conversor de Moedas')
    print(f'Dolar: {dolar_dia:2.2f} | Euro: {euro_dia:2.2f}')

    conversor(d, e, r, op)
    print('''O que deseja fazer?
    1 - Converter novo valor Real
    2 - Converter novo valor dolar_dia
    3 - Converter novo valor euro_dia
    4 - Sair''')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        r = float(input('Qual o novo valor de real:'))
    elif op == 2:
        d = float(input('Qual o novo valor de dolar:'))
    elif op == 3:
        e = float(input('Qual o novo valor de euro:'))
    elif op == 4:
        break
    else:
        print('Opção inválida, tente novamente!')
