# Esse e um jogo de adivinhacoes
import random

print ('Ola, qual o seu nome ?')
jogadornome = input()

print ('Bem,' + jogadornome + ' tente adivinhar qual filha foi sorteada... para incrementar')
ran = ['Maira', 'Nayara', 'Lenimara', 'Maryane']
irma = random.choice(ran)
for tentativas in range(1,3):
    print ('tente adivinhar qual delas é!')
    vez = input()
    # print = (irma)
    if vez != irma:
        print('Voce errou! tem mais uma tentativa' )
    else:
        break  
if vez == irma:
    print('Bom trabalho ' + jogadornome + ' Voce acertou! A filha foi a ' + irma + ' Voce conseguiu com ' + str(tentativas) + ' tentativas!')
else:
    print('Voce esgotou o numero de tentativas e nao conseguiu adivinhar. A filha sorteada foi a ' + irma )