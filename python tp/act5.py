#TA TE TI - EJERCICIO HECHO POR BENITEZ ANDREA Y ARAUJO LUCIANO

from random import randrange  



tablero = f"""┌───┬───┬───┐
│ 1 │ 2 │ 3 │                      
├───┼───┼───┤                       
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘ """

c1 = 0          

#JUGADOR X
def ponerX():               
    pos = randrange(1,10)   
    c = 0  
    global tablero
    global c1
    while c < 1:      
        for i in tablero: 
            if str(pos) == i : 
                tablero = tablero.replace(i,"X")
                c += 1
                c1 = c1 + 1 
        pos = randrange(1,10) 
        if c1 >= 5:  
            c += 1  
            return True

#JUGADOR O
def ponerO():  
    us= int(input("Ingrese numero: ")) 
    c = 0  
    while us < 0 or us > 9 :    
        us= int(input("Ingrese numero: "))
    while c < 1:                
        for i in tablero:       
            if str(us) == i:    
                c += 1
                return tablero.replace(i,"O") 
        if str(us) not in tablero:
            us= int(input("OOPS! Casilla ocupada :( \nVuelva a ingresar un numero: "))

def estado(h): 
    if tablero[16:25:4] == str(h):          
        return True
    elif tablero[16:81:32] == str(h):       
        return True                          
    elif tablero[16:73:28] == str(h):         
        return True
    elif tablero[44:53:4] == str(h):
        return True
    elif tablero[72:81:4] == str(h):
        return True
    elif tablero[20:77:28] == str(h):
        return True
    elif tablero[24:81:28] == str(h):
        return True
    elif tablero[24:73:24] == str(h):
        return True
    elif c1 >= 5:                               
        return False
    

c = 0  
while c < 1:
    ponerX()                        
    print(tablero)                  
    if estado("XXX") == True :      
        print("Gana X")             
        break
    elif estado("XXX") == False:    
        print("El juego terminó en empate")
        break
    tablero = ponerO()              
    print(tablero)                  
    if estado("OOO") == True:       
        print("Gana O")
        break
    elif estado("OOO") == False:
        print("El juego terminó en empate")
        break