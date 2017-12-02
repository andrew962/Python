#Diccionario
edad = {}
edad["Juan"] = 32
edad["Ricardo"] = 26
edad["Antonio"] = 18
edad["Carla"] = 23

nombre = input("Busqueda: ")
if nombre in edad.keys(): #
    print(nombre+ " esta en el diccionario. Tiene "+ str(edad[nombre])+ " años")
else:
    print(nombre+ " no esta en el diccionario.")

print("Las siguientes personas estan en el diccionario: " + str(edad.keys()))
print("EStas personas tienen estas edades: "+str(edad.values()))
#len genera un numero entero que dice el numero de contenido
print("El diccionario tiene "+str(len(edad))+ " elemnetos")
