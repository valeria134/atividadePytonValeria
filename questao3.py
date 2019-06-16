
g=str(input('infome seu genero F ou M:'))
h=float(input('informe sua altura?'))
if g == 'M':
    a=(72.7 * h)-58
    print('seu peso ideal para um corpo masculino é:',a)
if g == 'F':
    b=(62.1 * h)-44.7
    print('seu peso ideal para um corpo feminino é:',b)
