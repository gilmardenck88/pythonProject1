#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
#pode ou não se aposentar. As condições para aposentadoria são:
#a. Ter pelo menos 65 anos;
#b. Ou ter trabalhado pelo menos 30 anos;
# c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Digite sua idade: '))
servico = int(input('digite o tempo de serviço: '))
if idade >= 65:
    print('voce está apto para aponsentar-se')
elif servico >= 30:
    print('voce esta apto a aponsertar-se')
elif idade >= 60 and servico >= 25:
    print('voce esta apto a aponsertar-se')
else:
    print('Ainda não pode  aposentar-se')

