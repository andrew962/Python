if __name__=="__main__":
    """
    r #la r sobre esribe lo escrito
    r+ #esta forma lee y escribe
    w #Modo escritura solamente
    w+ #Esta forma lee y escribe
    a #Esta forma no sobre escribe
    a+ #esta forma lee, escribe y no sobre escribe
    """
    try:
        archivo=open('clase4.txt','w+')
        print(archivo.read())

        #for x in archivo:
        #    print(x)
        archivo.write("Este es el ejemplo.\n")
        archivo.close()
    except FileNotFoundError:
        print("No existe archivo")