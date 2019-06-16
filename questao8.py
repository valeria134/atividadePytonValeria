a=str(input('telefonou para a vitima(s-sim ou n-não)?'))
b=str(input('estve no local do crime?'))
c=str(input('mora perto da vitima?'))
d=str(input('devia para a vitima?'))
e=str(input('Ja trabalhou com a vitima?'))

pessoa=0 # conta o numero de respostas positivas
if a=='s' or a=='S':
    pessoa=pessoa+1

if b=='s'or b=='S':
     pessoa=pessoa+1

if c=='s' or c=='S':
     pessoa=pessoa+1
    
if d=='s' or d=='S':
    pessoa=pessoa+1

if e=='s' or e=='S':
    pessoa=pessoa+1

if pessoa==2:
    print('Suspeita')
    
if pessoa >2 and pessoa<=4:
    print('Cumplice')

if pessoa ==5:
    print('Assassino')

if pessoa <2:
    print('Inocente')
    
