def num_positivo(num):
    if num>0:
        print("Positivo")
    elif num==0:
        print("Relativamente no tira para ningun lado")
    else:
        print("Negativo")



if __name__ == "__main__":
  n=int(input("Dijite un numero: "))
  num_positivo(n)
