print('Gerador de PA')
print('=-==-==-==-==-==-==-==-==-==-=')
n = int(input('Qual o primriro termo: '))
r = int(input('Qual a razão: '))
c = 0
while c < 10:
    print('{}'.format(n), end=' -> ')
    n = n + r
    c += 1
print('FIM')