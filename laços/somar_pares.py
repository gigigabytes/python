#Construção de filtros para escolher quais elementos processar em um conjunto de elementos.

#Somar elementos pares de uma lista

lista = list(map(int,input().split()))

soma = 0

for i in range(len(lista)):
    #Vai pegar de 0 a n-1
    if (lista[i]%2==0):
        soma = soma + lista[i]

print("Soma dos elementos pares da lista = {:d}".format(soma))



#Outra forma de trabalhar com os próprios elementos da lista
lista = list(map(int,input().split()))

soma = 0

for i in lista:
    if (i%2==0):
        soma = soma + i
print("Soma dos elementos pares da lista = {:d}".format(soma))
