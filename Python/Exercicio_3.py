#Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar


nota1 = float( input('Primeira Nota: '))
nota2 = float( input('Segunda Nota: '))

soma = (nota1 + nota2)
print ("O resultado é:", soma)
soma = (soma % 2)
if soma == 0:
    print('Número par')
else:
    print ('O número é ímpar')