nome = str(input('Digite seu nome Completo: ')).strip()
fn = nome.split()
print('primeiro nome: {}\nÚltimo nome: {}'.format(fn[0], fn[-1]))
print(fn)
