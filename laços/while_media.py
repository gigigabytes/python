#While permite que um trecho de códigos se repita uma quantidade indeterminada de vezes, essa quantidade de repetições vai depender de uma condição assim como a condição do comando if.

#É necessário uma condição de parada

#Ler nota válida

n1 = float(input())

while (n1<0 or n1>100):
    print("Nota inválida, digite novamente")
    n1 = float(input())


n2 = float(input())
while (n2<0 or n2>100):
    print("Nota inválida, digite novamente")
    n2 = float(input())
    
media = (n1*2+n2*3)/5
print("{:.1f}".format(media))
