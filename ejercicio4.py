'''Ejercicio 4: Contador de Vocales
 Crea un programa que cuente el número de vocales en una palabra ingresada por el 
usuario.
'''

texto = "cocodrilo" 
vocales = "aeiouAEIOU"

numero_vocales = 0

for letra in texto:
  if letra in vocales:
    numero_vocales += 1
    
print(numero_vocales)