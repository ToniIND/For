#Coding: UTF

print "DIVISIONS"

x=int(input("Escrigui un numero mes gran a 0: "))

while x<=0:
	print ("No es mayor que 0")
	x=int(input("Inenta-ho de nou: "))

for i in range (1, x + 1):
	if x % i == 0:
		print (i) 



