

notas = []
soma = 0
media = 0
notasM = 0
total=0
for cont in range(10):
    media = 0
    soma = 0
    for cont1 in range(4):
	    nota = float(input("Digite a nota: "))
	    soma += nota
    media = soma / 4
    notas.append(media)
    print(notas)
    if media>=7:
        total=total+1
        
print('Há', total, 'aluno(s)com média igual ou acima de 7') 
