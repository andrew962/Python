def mayor(num):
    if num>100:
        print("Numero mayor a 100")
    else:
        print("Menor a 100")

if __name__ =="__main__":
    n=int(input("Dijiste numero: "))
    mayor(n)