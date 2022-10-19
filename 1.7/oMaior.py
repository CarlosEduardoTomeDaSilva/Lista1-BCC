x = int(input())
y = int(input())
z = int(input())

def maxNum():
    a = (x + y) / 2 + (abs(y - x)) / 2
    b = (y + z) / 2 + (abs(z - y)) / 2
    c = (a + b) / 2 + (abs(b - a)) / 2
    return c
    
num = int(maxNum())

print("O maior inteiro: ", repr(num))