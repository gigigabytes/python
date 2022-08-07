n = int(input())

print(n)

n100 = n//100
n50 = (n%100)//50
n20 = (n%50)//20
n10 = (n%n20)//10
n5 = n%5
n2 = (n%n5)//2
n1 = n2//2


print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")
