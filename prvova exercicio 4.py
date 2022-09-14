 #Escreva um programa que apresente quatro opções: (1) consulta saldo,
#(2) saque e (3) depósito e (4) sair. O saldo deve iniciar em R$ 0,00. A
#cada saque ou depósito o valor do saldo deve ser atualizado.

n = int(input(' escolha uma opçao; [1] saldo  [2] saque [3] deposito [4} sair'))
saldo = 0
soma = 0
sacar= 0
deposito = 0



if n == 1:

    soma += deposito
    soma -= sacar
    print(f'seu saldo {soma} ')
elif n == 3:
    deposito += deposito


    deposito = int(input('digite o valorque deseja depositar: '))
    print(f'seu novo saldo {soma} ')
elif n == 2:
    deposito += deposito
    soma -= sacar
    sacar = int(input(' digite o valor que deseja sacar: '))
    print(f'seu saldo {soma} ')
    if soma == 0:
        print('voce nao possui valores disponiveis')



print(f'seu saldo {soma} ')
