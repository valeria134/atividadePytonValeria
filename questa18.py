dia = int (input('Insira o dia do seu nascimento'))
mes = int (input('Insira o mês do seu nascimento'))
ano = int (input('Insira o ano do seu nascimento')) 
def funcao (a, b, c):
    m = 'Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro'
    m2 = m.split()
    if(a > 31):
        print('Data inválida!')
    if(a < 0):
        print('Data inválida!')
    if(b < 0):
        print('Data inválida!')
    if(b > 12):
        print('Data inválida!')
    if(c < 0):
        print('Data inválida!')
    else:
        print('Data de nascimento:', a, '/', b, '/', c)
        print('Voce nasceu em', a, 'de', m2[b-1], 'de', c)
funcao (dia, mes, ano)
