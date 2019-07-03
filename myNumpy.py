import numpy as np

np.zeros(4) # Array de 1 fila y 4 columnas de 0

np.ones(4) # Array de 1 fila y 4 columnas de 1

np.arange(10) # Array que posee los valores ordenados de 0 a 9

np.arange(3,20, 5) # Array que comienza en el 3 hasta el 19 de 5 en 5.

lista1 = [1,2,3,4]

array1 = np.array(lista1)  # A partir de la lista creamos un array

lista2 = [5,6,7,8]
lista2D = (lista1, lista2)

array2D = np.array(lista2D) # Creando un array de varias dimensiones a partir de una lista

array2D.shape  # Devuelve las dimensiones (filas, columnas)

# Las operaciones posibles entre array y escalar son:
#Suma +
#Resta -
#Multiplicacion *
#Division /
#Resto %
#Cociente entero //
#Exponenciacion **


#Indices

array = array1[1:2] # Se toman solo los valores de la posicion 1 a la 2
array = array1[:]  # Devuelve todo el array

array_copia = array.copy() # Se copia un array

array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Con array3[2][1] Devolvemos un array de un vector de 2 dimensiones

array = np.arange(15).reshape(3,5)
print(array) # Reajustamos a los valores especificados en el reshape
print(array.T) # Array traspuesto

np.save('array', array) #Se guarda array 
np.load('array.npy') # Es necesaria poner la extension para recuperarlo

# Es posible guardar en un mismo archivos varios arrays

np.savez('arrays', x = array, y = array.T)
array_cargado = np.load('arrays.npz')
print(array_cargado['x'])

# Y guardarlo en un archivo de texto

np.savetxt('mi_fichero_array.txt', array, delimiter = ',')
np.loadtxt('mi_fichero_array.txt', delimiter = ',')

# Funciones

array_sqrt = np.sqrt(array)

array_rand = np.random.rand(5) # Valores aleatorios de 0 a 1. Tamanyo 5

array_add = np.add(array, array)

array_max_value = np.maximum(array, array_add)

print(array_max_value)
array2D.dtype # Indica el tipo de datoas dentro del array.

