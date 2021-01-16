#Este programa imprime numeros aleatorios na tela

def tones(number):
    print (number)

def metal(number):
    print (" {}  {} ".format(number,number))

def core(number):
    print ("{}    {}    {}".format(number,number,number))

def note():
    invalue=input()
    print("{}     {}     {}    {}    {}".format(invalue,invalue,invalue,invalue,invalue))

tones(1)
metal(2)
core(3)
note()
