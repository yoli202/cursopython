'''
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
'''
cantidad = float(input("cuanto quieres invertir: "))
interes = float(input("cual es el interes: "))
anio= int(input("cuantos años: "))
print("tienes que pagar: " + str(round(cantidad * interes * anio, 2 )))