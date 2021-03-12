# Este programa imprime o nome digitado com informacoes ao contrario com letras maiusculas

def imprimereverso():
    print('Por favor digite seu nome, para que eu  possa imprimir seu nome ao contrario e com letrsa maiusculas')
    nomeusuario = input()
    print(nomeusuario.upper()[::-1])

# chama a funcao imprimereverso declarada acima

imprimereverso()


