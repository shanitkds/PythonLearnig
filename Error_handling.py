# Exeption 


# print(10/0) #ZeroDivisionError


# dish={
#     "a":10,
#     "b":12
# }

# print(dish["h"])   # KeyError:



# lst=[1,2,3,6,3]
# print(lst[10])   #IndexError



# a=int(5)
# b=str(10)
# print(a+b)  #TypeError


# file=open("sample33.txt","r")
# content=file.read()
# print(content)
# file.close()   #FileNotFoundError


# a=int("hello")
# print(a)  #ValueError
    
    
    
        # HOW TO SET ERROR
        
        
# try:
#     x=10/0
# except ZeroDivisionError:
#     print("it can't divide")
    
    
# # Using else and finally in Exception Handling
# # ------------------------------------------------


# try:
#     num=int(input("Enter a Number"))
#     result=10//num
# except ZeroDivisionError:
#     print("Division by zero is not allowed!")
# else:
#     print(f"the result is {result}")
# finally:
#     print("This will always be printed.")
    
    
# # 5. Raising Exceptions
# # -----------------------

# x=-5
# if x<0:
#     raise ValueError("Negative numbers are not allowed!")  


# 6. Custom Exceptions
# ---------------------


class MyErrorHandling(Exception):
    pass

def check_number(num):
    if num < 0:
        raise MyErrorHandling("Negative Number Not allowed")
    else:
        print(f'result is {num}')

# check_number(-10)
  
try:
    check_number(-2)
except MyErrorHandling as a:
    print(a)
