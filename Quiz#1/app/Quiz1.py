print("Veremos la temperatura")
temperatura = int(input("Ponga la temperatura: "))
tem = (((temperatura-32)*5)/9)
print(tem)
if tem >= 100:
    print("caliente")
elif tem < 0:
     print("frio")

