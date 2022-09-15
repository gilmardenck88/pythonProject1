 #Faça um programa que seja semelhante ao jogo da forca, mas com uma
#única letra. A letra que o usuário deve adivinhar deve ser definida no
#código do programa. O usuário tem 5 chances de acertar a letra. O
#programa finaliza sua execução quando o usuário acerta a letra ou
#quando acabam suas chances.

import string, random
usuario = ''
cont = 0
vocabulario = ['a' , 'b']
while cont <= 4:
    usuario = str(input(" adivinhe a letra: "))

    computador = random.choice(string.ascii_letters)
    print(f'o computador escolheu:{computador} ')
    cont +=1
    if computador == usuario:
        print('voce acertou ')
    else:
        print('vc errou')



    
