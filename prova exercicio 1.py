#Escreva um programa para ler 3 valores inteiros e escrever o maior
#deles. Considere que o usuário não informará valores iguais.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print(f'o numero maior é {n1}')
else:
    print(f'o numero maior é {n2}')