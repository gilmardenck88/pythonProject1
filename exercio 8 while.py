

soma = 0
cont = 0
maior = 0
menor = 0
media = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma += num
    cont += 1
    if cont == 1:
        menor = num
        maior = num

    elif num < maior:
        num = maior
    elif num > menor:
        num = menor




print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')
print(f'o numero de valores digitados é {cont}')
print(f'a soma de todos os numero digitados é {soma}')
print(f' a media dos numeros didgitados é {soma / cont}')






