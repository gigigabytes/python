x = float(input())
y = float(input())
if x==0:
    if y==0:
        print("Origem")
    else:
        print("Eixo Y")
else:
    if y==0:
        print("Eixo X")
    else:
        if y>0:
            if x>0:
                print("Primeiro quadrante")
            else:
                print("Segundo quadrante")
        else:
            if x<0:
                print("Terceiro quadrante")
            else:
                print("Quarto quadrante")