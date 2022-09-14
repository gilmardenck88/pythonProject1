#elabore um programa que faça a leitura de varios numeros inteiro, ate que se digite
#um numero negativo, o programa deve retornar o maior numero lido
maior = 0
menor = 0
num = 0
while num >= 0:
    num = int(input('Digite um numero inteiro: '))
    if num == 0:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
           menor = num

print(f'o maior numero foi {maior} o menor numero foi {menor}')




