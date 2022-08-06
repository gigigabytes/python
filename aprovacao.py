n1 = float(input())
n2 = float(input())

media = (n1*2+n2*3)/5

print("{:.1f}".format(media), end=": ")
if(media>=6.0):
    print("Aluno aprovado")
else:
    print("Aluno não aprovado")