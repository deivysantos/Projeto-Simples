import random

print('Bem-vindo ao seu Gerador de Senhas')

caracteres = 'abdcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,?0123456789' # Coloquei essas '' para abrigar letras do alfabeto na forma minuscula e maiuscula, numeros de 0 a 9 e símbolos para forecer uma senha forte e única.

numero = input('Quantidade de senhas a serem geradas: ') # Aqui você digita o quanto de senhas que o computador irá gerar pra você, seja 1,2,3 ou mais senhas.
numero = int(numero)

tamanho = input('Insire o tamanho da sua senha: ') # Aqui é o tamanho da sua senha se você quer 1,2,3,4,5 ou mais cacteres para a sua senha.
tamanho = int (tamanho)

print('\n Aqui estão as suas senhas geradas: ')

for senha in range (numero):
    senhas = ''
    for s in range (tamanho):
     senhas += random.choice(caracteres)
    print(senhas)    