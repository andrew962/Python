def opc(p):
    if p == "2":
        try:
            archivo = open('clase4.txt', 'a+')
            archivo.write("Hola.\n")
        except FileNotFoundError:
            print("No existe archivo")
    elif p == "1":
        print("Hola")
    else:
        print("Adios")


if __name__=="__main__":
    x = True
    while x!="3":
        print("1.Escribe Hola\n2.Guarda Hola\n3.Salir")
        try:
            x=input("Introduce una opcion: ")
            opc(x)
        except:
            print("error")

