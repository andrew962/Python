def impuesto(a):
    if a>15000:
        x=a*1.16
        print(str(x))
    else:
        x=a*1.10
        print(str(x))


if __name__=="__main__":
    b=float(input("Importe bruto: "))
    impuesto(b)
