#Uso do comando de repetição for do Python para percorrer os elementos de uma lista.

#l = list(map(int,input().split())

#qtd = len(l)

#for i in range(qtd):
    #print(l[i])



#pode ser feito dessa outra forma a seguir
l = list(map(int,input().split()))
soma = 0
for i in range(len(l)):
    soma = soma + l[i]

print(soma)
print(sum(l))