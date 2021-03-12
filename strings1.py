# Este programa recebe o valor de duas strings, informa o seu conteudo seguindo do cumprimento, e realiza comparacoes.

def avaliastring():
    print('digite o valor da primeira string')
    string1 = input()
    print('Digite o valor da segunda string')
    string2 = input()
    print('Tamanho de ' + string1 + ' e de ' + str(len(string1)) + ' caracteres')
    print('Tamanho de ' + string2 + ' e de ' + str(len(string2)) + ' caracteres')

# condicoes que testam semelhanca de conteudo e tamanho de string
    if len(string1) == len(string2):
        print('As 2 strings possuem o mesmo numero de caracteres')
    else:
        print('As 2 strings possuem numeros de caracters diferentes')

    if string1 == string2:
        print('As 2 strings possuem o mesmo conteudo')
    else:
        print('As 2 strings possuem conteudos diferentes')
    

#Chama a funcao avaiastring definada acima

avaliastring()
