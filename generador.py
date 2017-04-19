#Generador
import random
import os
try:
	s2 = "." + os.sep + "archivos"
	os.mkdir(s2)
except:
	print("La carpeta 'archivos' ya fue creada... Continuando")

dicc = {}
s2 = "." + os.sep + "archivos" + os.sep + "productos" + ".txt"
f2 = open(s2,'w+')

for i in range(1,31):
	s = "." + os.sep + "archivos" + os.sep + "ventas" + str(i) + ".txt"
	print ("Generando archivo: " + str(i))
	f = open(s,'w+')
	randomValue = random.randint(0,50)
	minimo = -1
	lista = []
	for cant in range(1,randomValue):
		cod = random.randint(1,10000)
		while cod < minimo:
			cod = random.randint(minimo,10000)
		minimo = cod
		ventas = random.randint(1,100)
		if cod in dicc:
			dicc[cod] += ventas
		else:
			dicc[cod] = ventas
		f.write(str(cod) +" "+ str(ventas) + "\n")
keys = dicc.keys()
keys.sort()
for key in keys:
	stock_actual = dicc[key] + random.randint(0,25)
	stock_minimo = random.randint(1,30)
	nombre_comercial = "nombre comercial " + str(key)
	precio  = random.uniform(0.5,100.0)
	f2.write(str(key) + " " +   str(stock_actual) + " " + str(stock_minimo) + " " + str(precio) + " " + nombre_comercial + "\n")



f.close()
f2.close()
