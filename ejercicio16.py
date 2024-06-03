'''Ejercicio 16: Contador de Números Pares e Impares
 Crea un programa que cuente y muestre la cantidad de números pares e impares en 
una lista ingresada por el usuario.'''

lista = [12, 20, 18, 33, 27, 100, 4]
pares = 0
impares = 0
for numero in lista:
  if numero%2 == 0:
    pares +=1
  else:
    impares +=1
    
print (f'en la lista hay {pares} numeros pares y {impares} numeros impares')
