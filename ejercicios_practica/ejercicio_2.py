# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número decimal a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número decimal a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)

print("Usted ha ingresado los números ", numero_1, " y ", numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
suma = numero_1 + numero_2

print("El resultado de sumar ", numero_1, " y ", numero_2, " es ", suma)

# Resta
resta_1 = numero_1 - numero_2
resta_2 = numero_2 - numero_1

print("El resultado de restar ", numero_1, " y ", numero_2, " es ", resta_1)
print("El resultado de restar ", numero_2, " y ", numero_1, " es ", resta_2)

# División
div_1 = numero_1 / numero_2
div_2 = numero_2 / numero_1

print("El resultado de dividir ", numero_1, " por ", numero_2, " es ", div_1)
print("El resultado de dividir ", numero_2, " por ", numero_1, " es ", div_2)

# Multiplicación
mult = numero_1 * numero_2

print("El resultado de multiplicar ", numero_1, " por ", numero_2, " es ", mult)
