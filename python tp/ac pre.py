import string

apellido=None
num=string.digits
apellidosi=0
nombresi=0
def estexto(a):
    for i in a:
        if i in num:
            if apellidosi==0:
                print("ingrese apellido con letras.")
                return False
            else:
                print("ingrese nombre con letras.")
                return False
    return True
    
def dni(a):
    if len(str(a))<=8 and len(str(a)) >= 7:
        return True
    else: 
        return False
        
while apellido!="":
    if apellidosi==0:
        apellido=input("Ingrese apellido ")
    if estexto(apellido)==True:
        apellidosi=1
        if nombresi==0:
            nombre=input("ingrese nombre: ")
        if estexto(nombre) == True:
            nombresi=1
            docu= int(input("dni: "))
            if dni(docu) == True:
                sexo=input("ingrese sexo ")






