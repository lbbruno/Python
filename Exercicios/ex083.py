expressao = list(input('Digite uma expressão: '))
abre = expressao.count('(')
fecha = expressao.count(')')
print('Esta ecpressão está correta.' if abre == fecha else 'Esta expressão está errada.')