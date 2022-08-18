#Para ao encontrar elemento ao percorrar os elementos da lista


def busca_list(l,x):
    res = 0 
    while (res!=len(l) and l[res]!=x):
        res = res+1
    if (res==len(l)):
        return -1
    else:
        return res



l = list(map(int, input().split()))
x = int(input())
indice = busca_list(l,x)
print(indice)