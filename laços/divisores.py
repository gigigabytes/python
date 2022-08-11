#Mostrar quais são os divisores de um número

n = int(input())

divisores = []

for d in range(1,n+1):
    if (n%d==0):
        divisores.append(d)

# O append insere um registro após o último elemento, ou seja, ele é útil quando é preciso colocar o novo registro na última posição da tabela.
print("{:d} possui {:d} divisores:".format(n,len(divisores)), *divisores)