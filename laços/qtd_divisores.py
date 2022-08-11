#Contador

#Divisores de um número

n = int(input())

qtd = 0 

for d in range(1,n+1):
    if (n%d==0):
        qtd = qtd+1

print("{:d} possui {:d} divisores".format(n,qtd) )
