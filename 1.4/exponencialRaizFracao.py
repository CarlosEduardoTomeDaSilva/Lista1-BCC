import math

a = int(input())
b = int(input())
x = float(input())
y = float(input())

expressao = a + (pow(b, x)) - (math.sqrt(b)) + (a + b) / (x - y)

print("expressão: {:.2f}".format(expressao))