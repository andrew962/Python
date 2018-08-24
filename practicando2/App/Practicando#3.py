def numero(a,b,c):
    if a>b and a>c:
        print(str(a)+" Es mayor")
    elif b>c:
        print(str(b)+" Es mayor")
    else:
        print(str(c)+" Es mayor")

if __name__ == "__main__":
    z=int(input("primer numero: "))
    x=int(input("segundo numero: "))
    c=int(input("tercero numero: "))
    numero(z,x,c)