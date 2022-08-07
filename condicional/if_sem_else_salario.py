salario_base = float(input())
vendas = float(input())
meta = float(input())
salario = salario_base + vendas*0.05 
if(vendas >= meta):
    salario = salario + ((vendas-meta)*0.10)
print("{:.2f}".format(salario))