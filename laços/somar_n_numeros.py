n = int(input())

soma = 0
for i in range(1, n+1):
    x = int(input())
    soma = soma + x
    #Num exemplo onde a entrada é 4, o código roda da maneira a seguir:
    #0 = 0+4 => 4
    #4 = 4+3 => 7
    #7 = 7+2 => 9
    #9 = 9+8 => 17
    #17

print(soma)