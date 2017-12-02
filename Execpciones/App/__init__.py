
if __name__=="__main__":
    a=True
    while a:#El while hace que se mantenga en un ciclo hasta que se teclee la imformacion correcta
        try:
            a=int(input("Introducir un numero: "))
            print(str(a))
            a=False
        except ValueError as ve:
            #Se obvia en esta parte el True ya que el python sabe que es True
            print("Necio preste atencion")
            print(ve)
        finally:#El finally simpre imprime
            print("Hola")
            """Solamente se puede tener una execepcion general y un finally."""
            """puedes usar "raise definiendo tu error Ejem:
             if a<0:
                raise TypeError"."""


    #if a==-9999:
    #   print("Hasta luego, necio")
    #else:
    #    print("Hasta luego, "+str(a)+"!")