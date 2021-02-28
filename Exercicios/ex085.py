num = [[], []]
for c in range(1,8):
    t = int(input(f'Digite o {c}º valor:'))
    if t % 2 == 0:
        num[0].append(t)
    else:
        num[1].append(t)
num[0].sort()
num[1].sort()
print(f'Os números pares são {num[0]}')
print(f'Os números ímpares são {num[1]}')
