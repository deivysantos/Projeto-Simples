# PROJETO ADVINHE O NÚMERO (USUÁRIO) IREMOS ADIVINHAR O NÚMERO DO COMPUTADOR

import random

def convidado (x):
    random_number = random.randint(1, x)
    computador = 0
    while computador != random_number:
        computador = int (input(f'Adivinhe um numero entre 1 e {x}: '))
        if computador < random_number:
            print ('Desculpe, adivinhe de novo. Muito baixo')
        elif computador > random_number:
            print ('Desculpe, adivinhe de novo. Muito alto')  


convidado(10)

print(f'Parabéns humano!!! Você conseguiu adivinhar o meu número\n')


# PROJETO ADVINHE O NÚMERO (COMPUTADOR) O COMPUTADOR IRÁ ADIVINHAR O NOSSO NÚMERO  
def computador_sabio(x):
    #DEFININDO UM VALOR ALTO E BAIXO PARA COMEÇAR QUE O COMPUTADOR ADIVINHE O NOSSO NÚMERO

    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c': # A letra 'c'(é de c de Correto) é quando o computador consiga adivinhar o número
        if baixo != alto:
          convidado = random.randint(baixo, alto)
        else:
         convidado = baixo  
        feedback = input(f'É {convidado} muito alto (A), muito baixo (B) ou está correto (C)? ').lower()
        if feedback == 'a':
          alto = convidado - 1
        elif feedback == 'b':
         baixo = convidado + 1

computador_sabio(10)

print(f'HA HA HA!!! eu consegui adivinhar o seu número humano.')
