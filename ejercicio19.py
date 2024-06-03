'''Ejercicio 19: Verificación de Año Bisiesto
 Escribe un programa que determine si un año ingresado por el usuario es bisiesto o 
no.'''

año = int(input("Ingrese año: "))

if año%4 == 0:
  print (f'El año {año} es bisiesto')
else:
  print (f'El año {año} no es bisiesto')