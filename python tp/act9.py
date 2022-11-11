'''
- Ingresar, actualizar y eliminar información de contacto,
- ubicar las direcciones con coordenadas en un mapa (investigar folium),
- mandar whatsapp a un determinado contacto (investigar cómo se puede hacer),
- cualquier otra función que considere o necesite.
'''
from tkinter import *
import pywhatkit
import mysql.connector
'''
conexion1= mysql.connector.connect(host="192.168.10.200", user="beniteza", passwd="123")
cursor1= conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()
'''
libreta={}

def agregar():
    print("\n DECIDISTE AGREGAR INFORMACIÓN\n")
    nombre=input("Ingrese nombre: ")
    numero=int(input("\nIngrese numero: "))
    libreta[nombre]:numero
    print(libreta)


def actualziar():
    print("\nModificar registro\n")
def eliminar():
    print("\nEliminar registro\n")


opcion = None

while opcion != "0":
    print("LIBRETA DE DIRECCIONES")
    print("""
    ************************************************************************
    1. AGREGAR
    2. ACTUALIZAR
    3. ELIMINAR

    0. Salir
    ************************************************************************
    """)
    opcion=input("Seleccione una opcion: ")

    if opcion == "1":
        agregar()
        
    elif opcion == "2":
        actualziar()
        
    elif opcion == "3":
        eliminar()
    elif opcion == "0":
        print("Usted eligió salir")
    else:
        print("Dato incorrecto")




'''
ventana= Tk()
ventana.geometry("400x280")

numero = Label(ventana, text= "Teléfono").grid(column=0, row=1)



ventana.mainloop()
'''