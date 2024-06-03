''' 
Ejercicio 5: Suma de Números Pares
 Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
 '''
 
def lista_pares(n): 
    return [i for i in range(n+1) if i % 2 == 0] 
print(lista_pares(100))

x = 0
for total in lista_pares(100):
  x += total
  
  
print(f'la suma de los pares de 1 a 100 es {x}' )