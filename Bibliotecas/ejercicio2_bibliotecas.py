# importaciones
import functools

# lista de numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filtrar numeros impares

# función para saber si un numero es impar

def func_impar(n):
    return ( n % 2 ) != 0

impares = list(filter(func_impar, numeros))

# sumarlos con la función reduce

sumatoria = functools.reduce(lambda x, y:x+y, impares)

print(f"Lista inicial: {numeros}")
print(f"Solo numeros impares: {impares}")
print(f"Suma de impares : {sumatoria}")