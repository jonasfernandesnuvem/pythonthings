def div(dividendo):
    try:
        return 30 / dividendo
    except ZeroDivisionError:
        print ('Gentileza nao tentar dividir por zero')
numero = input(div())