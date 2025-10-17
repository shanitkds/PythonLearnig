def HighOrder(a,b,fun):
    return fun(a,b)

def add(a,b):
    return a+b

def sub(a,b):return a-b

div=lambda a,b:a/b

mul=lambda a,b:a*b


print(HighOrder(1,2,add))