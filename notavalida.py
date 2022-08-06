nota01=float(input())
nota02=float(input())
if ((nota01 < 0.0) or (nota01 > 10.0)):
    print("Nota não é válida:", nota01)
    quit()
if(nota02<0.0 or nota02>10.0):
    print("Nota não é válda:", nota02)
    quit()
media=(nota01*2+nota02*3)/5
print("{:.1f".format(media))