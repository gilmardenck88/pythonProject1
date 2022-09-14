import random

vidas = 3
dado = int(random.uniform(1, 7))

while vidas > 0:
    n = int(input(“Adivinhe
    o
    número: ”))
    if n != dado:
        vidas -= 1
    else:
        break