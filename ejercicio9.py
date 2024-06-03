''' Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 
1 dólar es igual a 0.85 euros.'''

valor_dolar = 1
valor_euro = 0.85

dolares_a_cambiar = 97
euros_a_emtregar = dolares_a_cambiar * (valor_euro / valor_dolar)

print(f'{dolares_a_cambiar} dolares al cambio son {euros_a_emtregar} euros')

