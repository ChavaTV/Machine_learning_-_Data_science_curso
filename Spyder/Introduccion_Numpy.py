# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:58:46 2023

@author: Chava TV
"""

#IMPORTAMOS LA LIBRERIA NUMPY,
# instalar en caso de no tenerla
import numpy as np

# Array cuyos valores son todos 0
a = np.zeros((2, 4))

# imprime la lista de dimensiones con su longitud
print(a.shape)

# imprime el numero de dimensiones
print(a.ndim)

# imprime la longitud total de elementos
# multiplica la longitud por las dimensiones
print(a.size)

# CREACION DE ARRAYS

# Array cuyos valores son todos 0
b = np.zeros((2, 3, 4))

# Array cuyos valores son todos 1
c = np.ones((2, 3, 4))

# Array cuyos valores son todos el valor indicado como segundo parámetro de la función
d = np.full((2, 3, 4), 8)

# El resultado de np.empty no es predecible 
# Inicializa los valores del array con lo que haya en memoria en ese momento
e = np.empty((2, 3, 9))

# Inicializacion del array utilizando un array de Python
f = np.array([[1, 2, 3], [4, 5, 6]])

# Creación del array utilizando una función basada en rangos
# (minimo, maximo, número elementos del array)
print(np.linspace(0, 6, 10))

# Inicialización del array con valores aleatorios
g = np.random.rand(2, 3, 4)

# Inicialización del array con valores aleatorios conforme a una distribución normal
h = np.random.randn(2, 4)

# EJEMPLO DE UNA DISTRIBUCION NORMAL
import matplotlib.pyplot as plt

arreglo_2 = np.random.randn(1000000)

plt.hist(arreglo_2, bins=200)
plt.show()

# Inicialización del Array utilizando una función personalizada

def func(x, y):
    return x + 2 * y

arreglo_1 = np.fromfunction(func, (3, 5))

# ACCESO A LOS ELEMENTOS DE UN ARRAY

# Creación de un Array unidimensional
array_uni = np.array([1, 3, 5, 7, 9, 11])
print("Shape:", array_uni.shape)
print("Array_uni:", array_uni)

# Accediendo al quinto elemento del Array
print("quinto elemnto de un array: ",array_uni[4])

# Accediendo a los elementos 0, 3 y 5 del Array
print("elemnots 0 y salto de 3: ",array_uni[0::3])

# Creación de un Array multidimensional
array_multi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape:", array_multi.shape)
print("Array_multi:\n", array_multi)

# Accediendo al cuarto elemento del Array
print("acceso a un elemnto de un array multidimensional: ",array_multi[0, 3])

# Accediendo a la segunda fila del Array
print("Segunda fila: ",array_multi[1, :])

# Accediendo al tercer elemento de las dos primeras filas del Array
print("Tercer elemento de las primeras dos filas: ",array_multi[0:2, 2])

# MODIFICACION DE UN ARRAY

# Creación de un Array unidimensional inicializado con el rango de elementos 0-27
array1 = np.arange(28)
print("Shape:", array1.shape)
print("Array 1:", array1)

# Cambiar las dimensiones del Array y sus longitudes
array1.shape = (7, 4)
print("Shape:", array1.shape)
print("Array 1:\n", array1)

# El ejemplo anterior devuelve un nuevo Array que apunta a los mismos datos. 
# Importante: Modificaciones en un Array, modificaran el otro Array
array2 = array1.reshape(4, 7)
print("Shape:", array2.shape)
print("Array 2:\n", array2)

# Modificación del nuevo Array devuelto
array2[0, 3] = 20
print("Array 2:\n", array2)

print("Array 1:\n", array1)

# Desenvuelve el Array, devolviendo un nuevo Array de una sola dimension
# Importante: El nuevo array apunta a los mismos datos
print("Array 1:", array1.ravel())

# OPERACIONES ARITMETICAS CON ARRAYS

# Creación de dos Arrays unidimensionales
array1 = np.arange(2, 18, 2)
array2 = np.arange(8)
print("Array 1:", array1)
print("Array 2:", array2)

# Suma
print(array1 + array2)

# Resta
print(array1 - array2)

# Multiplicacion
# Importante: No es una multiplicación de matrices
print(array1 * array2)

# Broadcasting

# Creación de dos Arrays unidimensionales
array1 = np.arange(5)
array2 = np.array([3])
print("Shape Array 1:", array1.shape)
print("Array 1:", array1)
print()
print("Shape Array 2:", array2.shape)
print("Array 2:", array2)

# Suma de ambos Arrays
print(array1 + array2)

# Creación de dos Arrays multidimensional y unidimensional
array1 = np.arange(6)
array1.shape = (2, 3)
array2 = np.arange(6, 18, 4)
print("Shape Array 1:", array1.shape)
print("Array 1:\n", array1)
print()
print("Shape Array 2:", array2.shape)
print("Array 2:", array2)

# Suma de ambos Arrays
print(array1 + array2)

# FUNCIONES DE ESTADISTICA SOBRE ARRAYS

# Creación de un Array unidimensional
array1 = np.arange(1, 20, 2)
print("Array 1:", array1)

# Media de los elementos del Array
print("Media: ",array1.mean())

# Suma de los elementos del Array
print("Suma: ",array1.sum())

# Cuadrado de los elementos del Array
print("Cuadrado de los elementos: ",np.square(array1))

# Raiz cuadrada de los elementos del Array
print("Raiz de los elementos: ",np.sqrt(array1))

# Exponencial de los elementos del Array
print("Exponencial de los elementos: ",np.exp(array1))

# log de los elementos del Array
print("Logaritmo de los elementos: ",np.log(array1))

















