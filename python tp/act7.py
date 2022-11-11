#AHORCADO
#EJERCICIO HECHO POR ARAUJO LUCIANO Y BENITEZ ANDREA

import random as r

def ganador(x):
    c = 0
    for i in completo:
        if i in elegido:
            c += 1
    return c

palabras=["humanidad","abandonar", "abominar", "abril", "aceite","acelga","acero","biombo", 
"bisiesto","bledo","Brasil","broquel","bruma","camarón","cameo","camisa","camorra","camuflaje"]

aleatorio = r.choice(palabras)

print("----------- AHORCADO -----------")


elegido=aleatorio

aciertos=0
intentos=5
completo = ""

while True:
    elegido
    palabra = elegido.split()
    letra = input("Ingrese letra: ")
    if letra.isalpha() != True:
        print("INGRESE SOLO LETRAS")
    else:
        if letra not in elegido:
            intentos-=1
            print(f"LETRAS ACERTADAS: {aciertos}\nINTENTOS: {intentos}")
            if intentos == 0:
                print("SE ACABARON TUS INTENTOS ):")
                break
            
        else:
            print(f"La cantidad de veces que aparece la letra es de : {elegido.count(letra)}\nINTENTOS: {intentos}")
            if letra not in completo:
                completo += letra
                if ganador(completo) == len(elegido):
                    print("ganaste")
                    break