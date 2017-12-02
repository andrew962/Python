#Clase 4

def mul(a,b):
    return a*b

if __name__=="__main__":
    oper =lambda x,y:x*y  #Funciones anonimas lambda oper
    oper2 =lambda x:x[1:3]#oper2
    oper3 =lambda num: "Positivo" if num > 0 else "Negativo" #oper3
    oper4 =lambda fam: "Familia" if fam in l1 else "Extraño"#oper4
    oper5 =lambda lista: [a1*2 for a1 in l2]#oper5
    oper6 =lambda boom: [palabra for palabra in boom if len(palabra)>5] #oper6 revisa las
    #palabras de la lista y mira si son menores a 4 caracteres si es asi no las imprime"""

    l1 = ['Papa','Mama','Hijo']#oper4
    l2 = [20,25,17,16,1]#oper5
    l3 = ['casa','Papa','Carro','Persona']#oper6
    print(oper6(l3))#oper6
    print(oper5(l2))#oper5
    print(oper3(1))#oper3
    print(oper2([1,2,3,4,5,6,7,8,9]))#oper2
    print(oper(2,3))#oper
    print(mul(2,3))#oper
    #print(mul(oper(2,3),3))