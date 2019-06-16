metragem = int(input("Insira a metragem da área a ser pintada"))
capacidade = 18
litros = metragem/3
latasTinta = litros / capacidade
precoTotal = latasTinta * 80.0

print (latasTinta,':Latas')
print (precoTotal, ':R$')
