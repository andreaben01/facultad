#JUEGO AL AZAR
#EJERCICIO HECHO POR ARAUJO LUCIANO Y BENITEZ ANDREA
from random import randrange
import random as r

sorteados=[]
def sorteador():
    for i in range(21):
        g = str(randrange(0,100))
        if int(g) < 10:
            g = "0" + g
        sorteados.append(g)
    return sorteados


boleta=[]
def generadorBoletas():
    c = 0
    while c != 8:
        g = str(randrange(0,100))
        if int(g) < 10:
            g = "0" + g
        if g not in boleta:
            c+= 1
            boleta.append(g)
    return boleta


def resultado(bol,sorteo):
    aciertos =0
    c = 0
    for num in bol:
        c+= 1
        for num2 in sorteo:
            if num == num2:
                aciertos+=1
    return aciertos


c5 = 0
c6 = 0
c7 = 0
c8 = 0

x = int(input("Ingrese la cantidad de boletas a generar: "))
c = 0
s = sorteador()
while c  <= x:
    b = generadorBoletas()
    if resultado(b,s) == 5:
        c5 += 1
    elif resultado(b,s) == 6:
        c6 += 1
    elif resultado(b,s) == 7:
        c7 += 1
    elif resultado(b,s) == 8:
        c8 += 1
    c+= 1


print("La cantidad de boletas con 5 aciertos es de: ",c5)
print("La cantidad de boletas con 6 aciertos es de: ",c6)
print("La cantidad de boletas con 7 aciertos es de: ",c7)
print("La cantidad de boletas con 8 aciertos es de: ",c8)