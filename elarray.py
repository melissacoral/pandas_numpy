import numpy as np

# Crear una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista:", lista)

# Convertir la lista a un array de NumPy
arr = np.array(lista)
print("Array:", arr)

# Verificar el tipo de datos del array
print("Tipo del array:", type(arr))

# Crear una matriz a partir de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
print("Matriz:\n", matriz)

# Acceder a elementos del array
print("Elemento en la posición 1 del array:", arr[1])
print("Suma de los elementos en la posición 0 y 5 del array:", arr[0] + arr[5])

# Acceder a elementos de la matriz
print("Primera fila de la matriz:", matriz[0])
print("Segunda fila de la matriz:", matriz[1])
print("Tercera fila de la matriz:", matriz[2])

# Acceder a un elemento específico de la matriz
print("Elemento en la posición (0, 2) de la matriz:", matriz[0, 2])

# Acceso a subarrays y segmentos
print("Subarray hasta la posición 6:", arr[:6])
print("Subarray desde la posición 2:", arr[2:])
print("Array completo:", arr[:])
print("Array con pasos de 3:", arr[::3])
print("Último elemento del array:", arr[-1])
print("Últimos tres elementos del array:", arr[-3:])

# Submatrices
print("Submatriz desde la segunda fila:\n", matriz[1:])
print("Submatriz de la segunda fila y las dos primeras columnas:\n", matriz[1:, 0:2])

