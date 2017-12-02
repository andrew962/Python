"""Listas"""
"""listas son mutable, y las tuplas no son mutables"""
"""Diccionarios"""
"""listas y tuplas arrancan desde 0 hasta el rango que tenga las listas."""
"""eliminar es una sentencia, insertar es una funcion"""

"""Tupla"""
print("Tuplas")

mese =('Enero','Febrero','Marzo','Abril','Mayo','Junio',
       'Julio','Agosto','Septembre','Octubre','Novienbre','Diciembre')

#Las tuplas son con parentises


"""Lista"""
print(".-..---.-.-.-.-.-..-.-.-.-.-.-.")
print("Listas")
gatos = ["Tom","Kitty","Misifu"]

#Las listas son con corchete
print(mese[9])
print(mese[1:12])
print(gatos[2])

#Agregando nuevo gato
gatos.append("Micho")
#Insertando en una posision espesifica
gatos.insert(1,"Sam")
print(gatos)
#Para eliminar un items
del gatos[3]
print("Mis gatos: " +str(gatos))


print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("Diccionario")
"""Diccionario"""
#Los diccionarios se manejan entre llaves
directorio = {'Antonio Perez' :2329222,
              'Juana De Circulo' :4534233,
              'Miguel Jordanio' :7778909}

print("Antonio Perez: "+ str(directorio['Antonio Perez']))

print(directorio['Antonio Perez'])

#Agregando valor a directorio
directorio["Petra Pietro"] = 67890670
del directorio["Juana De Circulo"]

print(directorio)



