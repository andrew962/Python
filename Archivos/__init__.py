sal = True
while sal:
    nombre = input("Nombre: ")
    notafinal = int(input("Nota final: "))
    if 91 <= notafinal <= 100:
        print(nombre+ ", sacaste una A " + str(notafinal) + ":D")
    elif notafinal >=81:
        print(nombre+ ", sacaste una B "+ str(notafinal) + "!")
    elif notafinal >=71:
        print(nombre+ ", sacaste una C "+ str(notafinal) + "!")
    else:
        if notafinal < 0:
            print("Nota final invalida")
        else:
            print("Sacaste una F "+ str(notafinal) + "!")
    opc = input("Deceas continuar (S/N) -->").upper()
    if opc == "N":
        sal = False
        print("Hasta luego")
    elif opc == "S":
        sal = True
    else:
        sal = True
        print("No colocaste algo valido, pero te mantendre en el ciclo")