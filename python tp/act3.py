#NUMEROS PRIMOS
print("DETECTOR DE NÚMEROS PRIMOS")
num=int(input("ingrese un número: "))

def esPrimo(num):
	for i in range(2,num):
		if num%i==0:
			return False
	return True


for i in range(1, num+1): #range(0,21)
	if esPrimo(i) == True: #if esPrimo(i)
		print(i,end=" ")	

