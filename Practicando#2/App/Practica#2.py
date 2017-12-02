def vocal(letra):
    if letra== 'a'or letra=='A'or letra== 'e'or letra=='E'or letra=='I' or letra== 'i'\
            or letra=='O' or letra== 'o'or letra== 'u'or letra=='U':
        print("Es una vocal")
    else:
        print("No es vocal")

if __name__ == "__main__":
    ob=input("Dijite una letra: ")
    vocal(ob)
