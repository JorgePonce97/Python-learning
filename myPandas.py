import pandas as pd 

serie1 = pd.Series([3,5,6]) # Cada uno de los valores tiene unidentificador delante 

asignaturas = ['mates', 'lengua', 'historia']
notas = [4,5,7]
serie_notas = pd.Series(notas, asignaturas) # Como valores las asignaturas y como indice las notas

print(serie_notas['mates'])

print(serie_notas[serie_notas >=5])

# Tambien se le puedes poner un nombre

serie_notas.name = 'Mis notas'

# Para crear un diccionario a partir de una serie 

diccionario = serie_notas.to_dict()

print(diccionario)

#Tambien se puede crear una serie a partir de un diccionario

serie = pd.Series(diccionario)

# Es posible hacer operaciones entre ellas

asignaturas_tu = ['mates', 'lengua', 'historia']
notas_tu = [8,2,6]
serie_notas_tu =pd.Series(notas_tu, asignaturas_tu)

print((serie_notas + serie_notas_tu)/2)




