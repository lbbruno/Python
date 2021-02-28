c = ('\033[m',           # 0 - Sem cor
       '\033[0;30;41m',  # 1 - vermelho
       '\033[0;30;42m',  # 2 - verde
       '\033[0;30;43m',  # 3 - amarelo
       '\033[0;30;44m',  # 4 - azul
       '\033[0;30;45m',  # 5 - roxo
       '\033[1;30;107m'  # 6 - branco
     )
def titulo(txt, cor=0):
    moldura = '~'*(len(txt)+4)
    print(c[cor], end='')
    print(f'{moldura}\n  {txt}\n{moldura}')
    print(c[0], end='')


def pyhelp(cmd):
    from time import sleep
    titulo(f'Acessando Manual do Comando [{comando}]', 2)
    sleep(1.5)
    print(c[6], end='')
    help(cmd)


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 4)
    comando = str(input('Função ou Biblioteca >>> ')).strip().lower()
    if comando == 'fim':
        titulo('Programa Finalizado com Sucesso!', 1)
        break
    else:
        pyhelp(comando)
