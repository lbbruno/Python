def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')


def linha():
    print('-'*40)


def notas(*notas, sit=False):
    """
    -> Função para analisar as notas de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita vparias).
    :param sit: (opcional) indicando se deve ou não ser adicionar a situação.
    :param return: dicionários com várias informações sobre os alunos.
    """
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['média'] = sum(notas)/4
    if sit == True:
        if aluno['média'] < 5:
            aluno['sit'] = 'Reprovado'
        elif aluno['média'] < 7:
            aluno['sit'] = 'Recuperação'
        else:
            aluno['sit'] = 'Aprovado'
    return aluno

# MAIN PROGRAM
titulo('Situação do Aluno')

resp = notas(5, 4, 6, 3, 4, 7)
print(resp)
linha()
print(help(notas))
