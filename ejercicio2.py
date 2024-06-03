'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

plato_1 = 2
plato_2 = 0.3
bebida_1 = 0.4
bebida_2 = 0.1
total_sin_propina = plato_1 + plato_2 + bebida_1 + bebida_2
total_con_propina = total_sin_propina * 1.15
print(total_con_propina)
