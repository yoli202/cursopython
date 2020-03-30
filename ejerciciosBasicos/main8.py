'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día 
tiene un descuento del 60%. Escribir un programa que comience leyendo 
el número de barras vendidas que no son del día. Después el programa debe 
mostrar el precio habitual de una barra de pan, el descuento que se le hace 
por no ser fresca y el coste final total.
@author: Experis IT
'''
barras = 3.49
dto= 0.6
barras_dto = float(input("cuantas barras te llevas: "))
total_barras = float(barras - dto) * barras_dto
print("El precio habitual es: " + str(barras) + " el dto es: " + str(dto)
   + " y el total es: "  + str(total_barras))
