def sueldo(can):
    if can>10:
        x=40000*1.10
        print(str(x))
    elif can<10 and can>=5:
        x=40000*1.07
        print(str(x))
    elif can<5 and can>=3:
        x=40000*1.05
        print(str(x))
    else:
        x=40000*1.03
        print(str(x))

def mayor(num):
    if num>0:
        print("Mayor que cero "+str(num))
    elif num==0:
        print("El cero no es mayor ni menor que el mismo")
    else:
        print("Menor que cero "+str(num))

def suma(a,b):
    x=a+b
    print("La suma es: "+str(x))

def dia(sem):
    sem={}
    sem["1"]="Lunes"
    sem["2"]="Martes"
    sem["3"]="Miercoles"

    print(sem)


if __name__=="__main__":
    a=int(input("Cuanto anios Trabajo: "))
    sueldo(a)
    b=int(input("Numero: "))
    mayor(b)
    c=int(input("Primer numero: "))
    d=int(input("Segundo numero: "))
    suma(c,d)
    p=input("Opciones\n1.- Lunes\n2.- Martes\n3.- Miercoles\n-->")
    dia(p)

