soma = 0 
x = int(input())
while (x!=0):
    soma = soma+x
    x = int(input())
print(soma)

#Para de ler ao digitar zero 

#Final do arquivo 

soma = 0 
fim_de_arquivo = False
while (not fim_de_arquivo):
    try:
        x = int(input())
        soma = soma+x
    except:
        fim_de_arquivo=True
print(soma)