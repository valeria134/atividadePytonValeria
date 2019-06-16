salario = float(input('Digite seu salário:'))

#Se o salario for maior que 280

if salario <= 280:
      aumento = salario*0.2
      total = salario + aumento
      print('Seu salário antes do reajuste: R$',salario)
      print('Percentual aumentado: %',20)
      print('O valor do aumento é: R$',aumento)
      print('Com o reajuste, o seu salário é: R$',total)

elif salario > 280 and salario <= 700:
      aumento=salario*0.15
      total = salario + aumento
      print('Seu salário antes do reajuste: R$',salario)
      print('Percentual aumentado: %',15)
      print('O valor do aumento é: R$',aumento)
      print('Com o reajuste, o seu salário é: R$',total)



elif salario > 700 and salario <= 1500:
        aumento = salario*0.1
        total = salario +aumento
        print('Seu salário antes do reajuste: R$',salario)
        print('Percentual aumentado: %',10)
        print('O valor do aumento é: R$',aumento)
        print('Com o reajuste, o seu salário é: R$',total)



elif salario > 1500:
      aumento= salario*0.05
      total= salario + por
      print('Seu salário antes do reajuste: R$',salario)
      print('Percentual aumentado: %',5)
      print('O valor do aumento é: R$',aumento)
      print('Com o reajuste, o seu salário é: R$',total)

