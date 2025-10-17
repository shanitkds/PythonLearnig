# sum of Fibonacci

def fibnoncy(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibnoncy(n-1)+fibnoncy(n-2)
# print(fibnoncy(6))


def sum_fibnoncy(num):
    if num == 0:
        return 0
    else:
        return fibnoncy(num)+sum_fibnoncy(num-1)
    

b=sum_fibnoncy(5)
print(b)