#Coding: UTF8

Valors=input("Indiqueu el numero de valors: ")
aux=0

while Valors<=0:
	print "impossible"
	valors=input("Torneu a indicar el numero de valors: ")
for i in range (1,Valors+1):
	sup=input("Indiqueu el numero "+str(i)+":")
	if (sup<0):
		aux+=1
print "Has escrit ",aux,"numeros negatius"
