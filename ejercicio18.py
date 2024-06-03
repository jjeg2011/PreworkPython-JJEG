''' Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por 
el usuario'''

def contador_de_palabras(texto):
  texto_limpio = texto.replace(',','')
  palabras = texto_limpio.split()
  cantidad_de_palabras = len(palabras)
  return cantidad_de_palabras

texto_ingresado = input('Ingresa texto para contar palabras:')
resultado = contador_de_palabras(texto_ingresado)

print(f'la cantidad de palabras es: {resultado}')