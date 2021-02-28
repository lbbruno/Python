print('Gerador de PA - v3.0')
print('=-==-==-==-==-==-==-==-==-==-=')
n = int(input('Primriro termo: '))
termo = n
r = int(input('Razão: '))
c = 0
t = 10
totvezes = 0
sair = 1
while sair > 0:
    if n > 0:
        while c < t:
            print('{}'.format(termo), end=' -> ')
            termo = termo + r
            c += 1
        print('PAUSA')
        totvezes = totvezes + c
        c = 0
        n = t = int(input('Quantos termos você quer mostrar mais? '))
    else:
        sair = 0
print('Progressão finalizada com {} termos exibidos.'.format(totvezes))