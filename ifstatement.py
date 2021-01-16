print('Por favor digite sua idade')
idade = int(input ())
if idade > 35:
    print('Voce deve ser o Jonas')
elif (idade > 29) and (idade < 33):
    print('Voce deve ser a Maryane')
elif idade < 12:
    print('Voce deve ser a Yasmim')
else:
    print('nao sei quem e vc')
print('Agora me diga o seu nome')
name = input ()
print('Ola ' + name + ' o seu nome possui ' + str(len(name)) + ' letras')