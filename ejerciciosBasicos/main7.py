'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso 
de cada paquete así que deben calcular el peso de los payasos y muñecas que 
saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado.
'''
cantidad_p = int(input(" Cantidad de payasos: "))
cantidad_m = int(input(" Cantidad de las muñecas: "))
payasos = 112
muñecas = 75
print(" El peso de los payasos es : " + str(cantidad_p * payasos)) 
print(" El peso de las muñecas es : " + str(cantidad_m * muñecas))