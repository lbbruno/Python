print('#'*60)
r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))
print('#'*60)
triang = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
if triang:
    print('\033[036mPode ser formado um triângulo | {}'.format(triang))
else:
    print('\033[031mNão pode ser formado um triângulo | {}'.format(triang))
