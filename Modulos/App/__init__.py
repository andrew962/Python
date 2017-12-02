#import finanzas.operaciones as a
#otra forma es importa exactamente lo que necesitas
from finanzas.operaciones import impuesto


if __name__=="__main__":
    x = float(input("Sub-Total: $"))
    y = impuesto(x)
    print("El total es $%.2f"%y)
    #el ( "%.2f" % y ) Es para poner a dos decimales