numero = int(input())
# PAR   :  n = 2*x+0 ---->>> (n-0)/2 = x
# IMPAR :  n = 2*x+1 ---->>> (n-1)/2 = x


if (numero%2==0):
    tipo="par"
else:
    tipo="impar"
print("O número", numero, "é", tipo)