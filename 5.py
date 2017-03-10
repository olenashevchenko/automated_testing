def tre(a, b, c):
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        d = "True"
    else:
        d = "False"
    return d
a = input("a = ")
a = int(a)
b = input("b = ")
b = int(b)
c = input("c = ")
c = int(c)
print(tre(a, b, c))