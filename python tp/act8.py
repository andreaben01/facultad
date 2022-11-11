#ANALIZADOR DE TEXTO
import string

def no_letras(letra):
    if letra.isalpha() != True:
        return False
    else:
        return True

texto_orig= input("Ingrese texto: ").lower() #REVISAR LAS LETRAS CON TILDE

text_sin_punt= texto_orig.translate(str.maketrans('', '', string.punctuation))

text_limpio= text_sin_punt.split()

pal_elim = set(text_limpio)



while True:
    letra1=input("ingrese una letra: ").lower()
    letra2=input("ingrese una letra: ").lower()
    letra3=input("ingrese una letra: ") .lower()
    if no_letras(letra1) == False or no_letras(letra2) == False or no_letras(letra3) == False:
        print("INGRESE SOLO LETRAS")
    else:
        break

print("\n")
#1
print(f"la letra '{letra1}' aparece '{texto_orig.count(letra1)}' veces")
print(f"la letra '{letra2}' aparece '{texto_orig.count(letra2)}' veces")
print(f"la letra '{letra3}' aparece '{texto_orig.count(letra3)}' veces\n")

#2

print(f"la cantidad de palabras en el texto: {len(text_limpio)}\n")

for pal in pal_elim:
    if pal in text_limpio:
        print(f"La palabra {pal} aparece {text_limpio.count(pal)} {'veces' if len(pal)>1 else 'vez'}\n")

#3

simb=string.punctuation
for i in simb:
    if texto_orig.endswith(i):
        print(f"el texto empieza con '{texto_orig[0:1]}' y termina con '{texto_orig[-2:-3:-1]}'\n")
        break
    else:
        print(f"el texto empieza con '{texto_orig[0:1]}' y termina con '{texto_orig[-1:-2:-1]}'\n")
        break



#4
print(f"texto invertido: {texto_orig[::-1]}\n")

#5
while True:
    pal_ingresada= input("Ingrese palabra: ")
    if pal_ingresada.isalpha() == True:
        if pal_ingresada in text_limpio:
            print(f"la palabra {pal_ingresada} que ingresó, se encuentra en el texto\n")
            break
        else:
            print(f"UPS! la palabra que ingresó no se encuentra en el texto")
            break
    else:
        print("¡Ingrese solo letras!")


#6
for pal in pal_elim:
    if pal in text_limpio:
        if len(pal) in range(1,len(pal)+1):
            print(f"la palabra '{pal}' de '{len(pal)}' letras, aparece '{text_limpio.count(pal)}' veces")
