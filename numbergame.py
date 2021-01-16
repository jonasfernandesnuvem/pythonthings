# Esse e um jogo de adivinhacoes
import random

print ('Ola, qual o seu nome ?')
jogadornome = input()

print ('Bem,' + jogadornome + ' estou pensando em um nome de 1 a 20')
numero = random.randint(1, 20)

for tentativas in range(1, 7):
    print ('tente adivinhar qual numero estou pensando!.')
    vez = int(input())
    if vez < numero:
        print('Tente um numero maior')
    elif vez > numero:
        print('Tente um numero menor')

    else:
        break # essa correcao e para a tentativa correta

if vez == numero:
    print('Bom trabalho ' + jogadornome + ' Voce acertou! o numero que eu escolhi foi ' + str(numero) + ' Voce conseguiu com ' + str(tentativas) + ' tentativas!')
else:
    print('Voce esgotou o numero de tentativas e nao conseguiu adivinhar. O numero que eu escolhi foi ' + str(numero))