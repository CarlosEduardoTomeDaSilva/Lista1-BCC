import math

a = float(input())
b = float(input())
c = float(input())
x = float(input())

def i():
    return (-b + math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    
def ii():
    return (-b - math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    
def iii():
    return a * pow(x, 2) + b * x + c
    
print("raizes: {:.2f} {:.2f}".format(i(), ii()), "resultado para x = {:.2f}: {:.2f}".format(x, iii()))