#Usando numpy

import numpy as np

A = np.zeros(4) #crea un array de ceros

print(A)

B = np.ones(4) #crea un array de unos

print(B)

C = np.arange(4) # crea un array de 0 a 3

print(C)

D = np.arange(3,9,2) # De 3 a 9 (sin incluirlo) de 3 en 2

 
print(D)

#Con listas

lista1 = [1, 2, 3, 4]
arr1 = np.array(lista1)

print(lista1)
lista2 = [5,6,7,8]

listasuma = (lista1,lista2)

arraysuma = np.array(listasuma)

print(listasuma)

print(arraysuma.shape) #muestra el tamanyo

print(arraysuma.dtype) #muestra el tipo de datos



#operaciones

array1 = np.array([1,2,3,4])
array1 = array1 + 4
print(array1)


#Indexacion 
array = np.arange(1,10)

print(array[0:3]) #Solo toma los valores de la posicion 0 a la 3

arraycopia = array.copy() #creamos una copia

arraycopia += 2
print(array) #No se ha modificado el array original

#Matrices 

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))

print(array2)

#El primer indice  designa la dimension de fila, si hubiera una tercera dimension se referiria ella

#Trasponer Matrices 
 
array = np.arange(15).reshape((3,5)) #3 filas 5 columnas

print(array)

print(array[1][1]) # Seria el valor 6

#Para hacer la traspuesta

array_tras = array.T 

print(array_tras)


#Entradsa y salida con arrays

array1 = np.arange(6)
np.save('array1',array1)#Guardo el array1 como un archivo

np.load('array1.npy') #Es necesaria la extension 

array2 = np.arange(8)

#Para guardar mas de un array a la vez

np.savez('arrays',x=array1,y=array2)

#Para recuperarlos 

array_recuperado = np.load('arrays.npz')

print(array_recuperado['x'])
print(array_recuperado['y'])


#Para guardar en un fichero de texto

np.savetxt('mificheroarray.txt', array2, delimiter =',')

#Para recuperarlo

array_rec = np.loadtxt('mificheroarray.txt', delimiter = ',')
print(array_rec)

#Funciones a uyn array

array = np.arange(5)

array_sqrt = np.sqrt(array)

print(array_sqrt)


#array_add = np.add(array1, array2) #No se pueden sumar arrays  de diferentes tamanyos

#print(array_add)

array_maximum = np.maximum(array_sqrt, array)

print(array_maximum)











array_random = np.random.rand(5)


