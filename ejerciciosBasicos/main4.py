'''
Escribir un programa que pregunte al usuario por el número de horas 
trabajadas y el coste por hora. Después debe mostrar por pantalla la paga 
que le corresponde.

'''
horas = int(input(" Introduce el numero de horas: "))
coste = int(input (" Introduce el coste de las horas : "))
paga = round( horas * coste , 3)
print(" Salario :" + str(paga) )
