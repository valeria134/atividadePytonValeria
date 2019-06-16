def vendagem():

    salarios = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999]]
    vendedores = [0,0,0,0,0,0,0,0,0]

    print('Digite 100 para terminar com a repetição')
    vendagem= float(input('Informe  o valor das vendas adquirida: '))

    while(vendagem != 100):
        pagamento= (vendagem*0.09)+200
        if pagamento < 1000:
            for i in range(8):
                if pagamento > salarios[i][0] and pagamento< salarios[i][1]:
                    vendedores[i] += 1
        else:
            vendedores[8] += 1
            
        vendagem = float(input("informe o valor das vendas adquiridas:"))

    for i in range(8):
        print(' Portanto temos entre  R$', salarios[i][0], 'e R$', salarios[i][1], ':', vendedores[i], 'vendedore(s)')
        
    print(' Agora nos maiores R$1000 temos: ', vendedores[8], 'vendedore(s)')


vendagem()
