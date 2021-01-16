# def div42by(divideby):
#     try:
#         return 42 / divideby
#     except ZeroDivisionError:
#         print('Error: You tried to divide by zero.')


# print('digite o valor pelo qual gostaria de dividir o numero 42: ')
# # (int(div42by(2)))
# print(div42by(2))
# print(div42by(4))
# print(div42by(0))
# print(div42by(1))

try:
    print('Quantos gatos vc tem ? ')
    numgatos = input()
    if int(numgatos) >= 4:
        print( 'Voce tem muitos gatos' )
    else:
        print ('voce nao tem muitos gatos')
except KeyboardInterrupt:
    print('Voce interrompeu a execucao do script')
except ValueError:
    print ('Digite um numero inteiro, nao digite o nome do numero por extenso')
except: 
    print ('Algo deu errado por aqui')
else:
    print('Deu bom')