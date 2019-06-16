
frase =str(input("informe uma frase: "))
print("Ha '%i' espaços na frase.  "%(frase.count(" "))) # estes espaços entre parenteses serve para contar os espaços

s = frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u") # esta contando as vogais que esta na frase 
print("Ha '%i' vogais na frase."%(s))

#foi criado a função count para mostrar a quantidade de elementos neste caso espacos na frase e a quantidade de vogais


