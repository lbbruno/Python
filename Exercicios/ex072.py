extenso = ('Zero', 'Um', 'Dois', 'Três', 'Qatro', 'Cinco')
while True:
    num = int(input('Digite um valor entre 0 e 5: '))
    if num > len(extenso) - 1:
        print('Tente novamente...')
    else:
        print(f'Você digitou o número {extenso[num]}')
        break

