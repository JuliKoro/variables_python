# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice una calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print("Ingrese dos números reales, por favor.")

#Ingreso de la primer variable flotante
print("Número 1: ")
numero_1 = float(input())

#Ingreso de la segunda variable flotante
print("Número 2: ")
numero_2 = float(input())

#A) Suma
suma = numero_1 + numero_2
print("El resultado de la suma entre ", numero_1, " y ", numero_2, " es ", suma)

#B) Resta
resta_1 = numero_1 - numero_2
print("El resultado de la resta entre ", numero_1, " y ", numero_2, " es ", resta_1)
resta_2 = numero_2 - numero_1
print("El resultado de la resta entre ", numero_2, " y ", numero_1, " es ", resta_2)

#C) Multiplicación
mult = numero_1 * numero_2
print("El resultado de la multiplicación entre ", numero_1, " y ", numero_2, " es ", mult)

#D) División
div_1 = numero_1 / numero_2
print("El resultado de la división entre ", numero_1, " y ", numero_2, " es ", div_1)
div_2 = numero_2 / numero_1
print("El resultado de la división entre ", numero_2, " y ", numero_1, " es ", div_2)

#E) Exponente/Potencia

pot_1 = numero_1 ** numero_2
print("El resultado de hacer ", numero_1, " elevado a la ", numero_2, " es ", pot_1)
pot_2 = numero_2 ** numero_1
print("El resultado de hacer ", numero_2, " elevado a la ", numero_1, " es ", pot_2)