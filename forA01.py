#Coding: UTF

print "Pars e impars"

x=int(input("Escrigui un numero enter: "))
y=int(input("Escrigui un numero enter major que "+str(x)+": "))

while x>y:
	print ("No es mayor que ",x)
	y=int(input("Inenta-ho de nou: "))

for i in range (x,y):
	if i % 2 == 0:
		print "El numero "+str(i)+" es un numero par"
	if i % 2 != 0:
		print "El numero "+str(i)+" es un numero impar" 


