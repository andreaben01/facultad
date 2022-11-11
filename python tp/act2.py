#PRIÁMIDE DE BLOQUES
bloq=int(input("Ingrese la cantidad de bloques que desea:"))

altura = 0
while bloq > altura:
    altura += 1
    bloq -= altura 

print("La altura de la pirámide es:", altura)
print("Sobraron", bloq, "bloques")