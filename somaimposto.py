# Este programa utiliza uma funcao que permite o calculo do preco total de uma mecadoria com base no valor do imposto

def somaImposto():
    print('Digite por favor o valor do produto sem o imposto:')
    Custo = int(input ())
    print('digite a porcentagem do imposto a ser cobrada, para saber o valor total do produto no final:')
    TaxaImposto = int(input ())
    CalculoPorcentagem = Custo / 100
    CalculoValorImposto = CalculoPorcentagem * TaxaImposto
    ValorRealMercadoria = CalculoValorImposto + Custo
    print('O valor real da sua mercadoria, já somando o imposto é de  {}'  .format(ValorRealMercadoria))


# call to function above defined

somaImposto()
        
