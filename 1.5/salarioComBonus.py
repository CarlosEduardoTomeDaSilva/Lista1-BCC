nome = input()
salario = float(input())
vendas = float(input())

print(nome, "deve receber", "R$", "{:.2f}".format(vendas*.05 + salario))