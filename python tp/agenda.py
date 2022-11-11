agenda={"Andrea":"85734895", "Juan":"5873489543","Julieta":"53248759"}

########################### CONSULTAR ##############################################################
def consultar():
    print("----- CONSULTAR INFORMACIÓN -----\n")
    
    while True:
        nombre=input("Ingrese nombre de la persona\n:")
        if nombre in agenda.keys():
            print(agenda[nombre])
            print("---¿Desea continuar con la consulta?---\n")
            print("""
                1. Si
                2. No
                """)
            respuesta=input("...")
            if respuesta == "1":
                continue
            else:
                break
        else:
            print("Dicho contacto no existe. Ingrese otro nombre.")

########################### AGREGAR ##############################################################

def agregar():
    print("----- AGREGAR INFORMACIÓN -----\n")
    while True:
            nombre=input("ingrese nombre: ")
            if nombre.isalpha() != True:
                print("Ingrese solo letras")
            elif nombre not in agenda.keys():
                print("Este contacto no existe. ¿Desea agregarlo?")
                print("""
                1. Si
                2. No
                0. Salir
                """)
                add=input("...")
                if add == "1":
                    nombre=input("ingrese nombre: ")
                    numero=input("ingrese numero: ")
                    agenda[nombre]=numero
                    print("-----Contacto agregado con éxito.-----")
                    print(agenda)
                elif add == "2" or "0":
                    break
            else:
                print("Este contacto ya existe. Ingrese otro nombre")

########################### MODIFICAR ##############################################################

def modificar():
    print("----- MODIFICAR INFORMACIÓN -----\n")
    while True:
        nombre=input("ingrese nombre: ")
        if nombre in agenda.keys():
            print("Este contacto existe. ¿Desea modificar el número?")
            print("""
            1. Si
            2. No
            0. Salir
            """)
            mod=input("...")
            if mod == "1":
                numero=input("ingrese numero: ")
                if numero.isdigit() == True:
                    agenda[nombre]=numero
                    print("AVISO: Has cambiado el número de este contacto.")
                    print(agenda,"\n")
                    print("¿DESEA CONTINUAR?")
                    print("""
                    1. Si
                    2. No
                    """)
                    respuesta=input("...")
                    if respuesta == "1":
                        continue
                    elif respuesta == "2":
                        break
                else:
                    print("Dato incorrecto.")
            elif mod == "2" or "0":
                break
            else:
                print("Dato incorrecto.")
        else:
            print("Este contacto no existe.")

########################### BORRAR ##############################################################

def borrar():
    print("----- BORRAR INFORMACIÓN ----- \n")
    while True:
        nombre=input("ingrese nombre: ")
        if nombre in agenda.keys():
            print("Este contacto existe. ¿Desea eliminar este contacto?")
            print("""
            1. Si
            2. No
            0. Salir
            """)
            opc=input("...")
            if opc == "1":
                del(agenda[nombre])
                print("El contacto se eliminó con éxito.")
                print(agenda)
            elif opc == "2":
                continue
            elif opc == "0":
                break
            else:
                print("Dato incorrecto.")
        else:
            print("Dato incorrecto.")
    else:
        print("Este contacto no existe.")

########################### MENÚ DE OPCIONES ##############################################################

opc = None

while opc != "0":
    print("\nMENU DE OPCIONES")
    print("""
    ************************************************************************
    1. CONSULTAR
    2. AGREGAR
    3. MODIFICAR
    4. BORRAR

    0. Salir
    ************************************************************************
    """)

    opc=input("Seleccione una opcion: ")
    print("\n")
    if opc == "1":
        consultar()
    elif opc == "2":
        agregar()
        print(agenda)
    elif opc == "3":
        modificar()
    elif opc == "4":
        borrar()
    elif opc == "0":
        print("Usted eligió salir")
    else:
        print("Dato incorrecto")