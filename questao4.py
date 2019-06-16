hora=float(input('Quanto voce ganha por hora?'))
mes=float(input('informe o numero de horas trabalhada por mes:'))

salarioBruto = hora*mes
impostoRenda=salarioBruto*0.11
inss=salarioBruto * 0.08
sindicato=salarioBruto*0.05
salarioLiquido=(salarioBruto-impostoRenda-inss-sindicato)

print('seu salario bruto é:',salarioBruto)
print(' Imposto de renda:',impostoRenda)
print('INSS:',inss)
print('Sindicato:',sindicato)
print('Salario liquido:',salarioLiquido)
