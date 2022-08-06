n1 = float(input())
n2 = float(input())

media = (n1*2+n2*3)/5

if(media>=6.0):
    situacao = "Aprovado" 
else:
    situacao = "Não aprovado" 
print("{:.1f}:".format(media), situacao )
