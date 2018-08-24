import random
f = open('yoyo.txt','w')

pala = input('Palabra: ')

for x in pala:
    #a
    if x == 'a':
        x = 'p'
    #B
    elif x == 'b':
        x = 'r'
    #C
    elif x == 'c':
        x = 'f'
    #D
    elif x == 'd':
        x = 'h'
    #E
    elif x == 'e':
        x = 'a'
    #F
    elif x == 'f':
        x = 'c'
    #G
    elif x == 'g':
        x = 'n'
    #H
    elif x == 'h':
        x = 'o'
    #I
    elif x == 'i':
        x = 'y'
    #J
    elif x == 'j':
        x = 'd'
    #K
    elif x == 'k':
        x = 'q'
    #L
    elif x == 'l':
        x = 'u'
    #M
    elif x == 'm':
        x = 's'
    #N
    elif x == 'n':
        x = 'z'
    #Ñ
    elif x == 'ñ':
        x = 'i'
    #O
    elif x == 'o':
        x = 'l'
    #P
    elif x == 'p':
        x = 't'
    #Q
    elif x == 'q':
        x = 'x'
    #R
    elif x == 'r':
        x = 'j'
    #S
    elif x == 's':
        x = 'v'
    #T
    elif x == 't':
        x = 'k'
    #U
    elif x == 'u':
        x = 'e'
    #V
    elif x == 'v':
        x = 'm'
    #W
    elif x == 'w':
        x = 'b'
    #X
    elif x == 'x':
        x = 'g'
    #Y
    elif x == 'y':
        x = 'ñ'
    #Z
    elif x == 'z':
        x = 'w'
    elif x == ' ':
        lista = ['.','_','/','"','!','#','$','%','&','(','=','?','¿',']','*','+']
        x = random.choice(lista)
    f.write(x)