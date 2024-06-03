'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

tortilla = 100
macarrones = 20
cocacola = 30
cerveza = 40

cuenta = [tortilla, macarrones, cocacola, cerveza]

total_con_propina = 0
propina = 1.15
for producto in cuenta:
  total_con_propina += producto*propina
  
print (total_con_propina)

  
