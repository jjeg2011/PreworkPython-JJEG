'''Ejercicio 15: Conversor de Tiempo
 Escribe un programa que convierta un número de minutos en horas y minutos. Por 
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

dato = int(input("Ingrese los minutos: "))
hora = dato // 60
minutos = dato - (hora * 60)
print(f'{hora} horas y  {minutos} minutos')