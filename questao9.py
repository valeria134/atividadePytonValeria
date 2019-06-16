morango=float(input('Informe quantidade de morango em kg:'))
maca=float(input('Informe quantidade de morango em kg:'))
 
if morango <= 5:
    totalMorango=morango*2.50
    
if maca <= 5:
    totalMaca=maca*1.80

if morango>5:
    totalMorango=morango*2.20

if maca>5:
    totalMaca=maca*1.50
    
total= totalMorango+totalMaca

if (total > 25) or(morango+maca > 8):
    total=total*0.1



print('valor a ser pago pelos morangos',totalMorango)
print('valor a ser pago pelas macas',totalMaca)
print('o toal sera',total)
