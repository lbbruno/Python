res = 0
div = '-' * 40
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print(div)
    if num < 0:
        break
    for tab in range(1, 11):
        res = tab * num
        print(f'{num} X {tab} = {res}')
    print(div)
print('Programa Finalizado com Sucesso!')