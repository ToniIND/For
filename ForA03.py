#Coding: UTF8

Valors=input("Indiqueu el numero de valors: ")

while Valors<=0:
	print "impossible"
	valors=input("Torneu a indicar el numero de valors: ")
x=input("Escriu un numero: ")
for i in range (1,Valors+1):
	sup=input("Indiqueu un numero superior a "+str(x)+":")
	if (sup<=x):
		print "impossible"
print "Programa finalitzat"
