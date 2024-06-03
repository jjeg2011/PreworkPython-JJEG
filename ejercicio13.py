'''
Ejercicio 13: Verificación de Número Primo
 Escribe un programa que determine si un número ingresado por el usuario es primo 
o no.

'''
def es_primo(n):
  for i in range(2,n-1):
    if (n%i) == 0:
      return False
  return True
print(es_primo (11927))
