def linha(txt):
    print(f'\033[034m{"-"*40}\n{txt:^40}\n{"-"*40}')


linha('Editando Texto através de funções')


def titulo(tit):
    separador = '~'*(len(tit)+4)
    print(f'{separador}\n  {tit}\n{separador}')

titulo('Bruno Sehn Bonotto de Lima')