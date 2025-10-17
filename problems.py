# a={1,2,3,4}
# b={3,4,5,6}

# find all uniq from both sets

# 1.
# a={1,2,3,4}
# b={3,4,5,6}
# # setNew=a.union(b)
# # print(setNew)
# print(a|b)

# 2.

# a={'Apple','Banana','Chery'}
# b={'Banana','Chery','Dates'}

# # setNew=a.intersection(b)
# # print(setNew)
# print(a&b)


# 3.

# a={10,20,30,40}
# b={30,40,50,60}

# newSet=a.difference(b)
# print(newSet)
# print(a-b)


# 4.
# a={1,2,3,4}
# b={3,4,5,6}

# newSet=a.symmetric_difference(b)
# print(newSet)
# print(a^b)



# 5.

# student1={'Ali','Saara','Ahamadh'}
# student2={'Sara','jhone','Ahamadh','Fathima'}


# bothClass=student1.union(student2)
# print(bothClass)

# onlyInA=student1.difference(student2)
# print(onlyInA)

# onlyInB=student2.difference(student1)
# print(onlyInB)

# eaither=student1.symmetric_difference(student2)
# print(eaither)


# LIST

# 1.
# lst1=[1,2,3,4,5]
# print(lst1[1])

# lst2=[1,2,3]
# lst2.append(10)
# print(lst2)


# lst3=[2,3,4,5]
# lst3.remove(3)
# print(lst3)

# lst4=[5,1,4,2,3]
# lst4.sort()
# print(lst4)

# lst5=[2,4,6,8]
# print(sum(lst5))

# lst6=[1,2,3,4,5]
# lst6.reverse()
# print(lst6)

# lst7=[5,6,7,8]
# lst7[1]=99
# print(lst7)


# lst8=[100,200,300,400,500]
# print(lst8[:3])

# lst9=[1,2,2,3,2,4]
# print(lst9.count (2))



# --------------------------------------------------------------------------


# number={1,2,3,4}
# number.add(5)
# print(number)

# number.remove(2)
# print(number)


# a={1,2,3}
# b={3,4,5}
# newSet=a|b
# print(newSet)

# c={1,2,3}
# d={2,3,4}
# interSet=c&d
# print(interSet)


# list1=[1,2,2,3,4,4]
# SetNew=set(list1)
# print(SetNew)

# e={1, 2, 3, 4}
# f={3, 4, 5}
# diffSet=e-f
# print(diffSet)


# clearSet={10, 20, 30}
# clearSet.clear()
# print(clearSet)


# str='hello'
# strSet=set(str)
# print(strSet)

# ------------------------------------------------------------------------------

# student={
#     'name':'shanith',
#     'age':15
# }
# print(student)


# keyValue={
#     'name':'Sara',
#     'age':22
# }

# print(keyValue['age'])
# keyValue.pop('age')
# print(keyValue)

# ---------

# grade={
#     'name':'Ali'
    
# }

# grade.update({'grade':'A'})

# print(grade)

# ------

# lisrDish={
#     'keys':['a','b'],
#     'value':[1,2]
# }

# print(lisrDish)
# # ---------

# ageUp={"name": "Ali", "age": 20}
# ageUp['age']=25
# print(ageUp)

# # ------------------

# A={"x": 10, "y": 20}
# print(A.keys())
# print(A.values())

# # ---------------------------


# name='Ali'
# age=22
# is_student=True

# print(type(name),type(age),type(is_student))


# sum=5+3*2
# print(sum)


# floor_division=17//3
# division=17/3
# module=17%3
# print('floor_division :',floor_division,'   division :',division,'   module :',module)


# listA=[10, 20, 30, 40]
# listA.append(50)
# print(listA)


# listB=[1, 2, 3, 4]
# print(listB[-1])


# listRemove=[10, 20, 30, 40]
# listRemove.remove(20)
# print(listRemove)


# # tupleA=(1,2,3)
# # tupleA


# # tupleB=(1, (2, 3), 4)
# # print(tupleB[1][1])

# # setA={1,2,2,3}
# # print(setA)


# # setB={1,2}
# # setC={2,3}
# # setUnion=setB|setC
# # print(setUnion)

# setB={1,2,3}
# setC={2,3,4}
# setB.intersection_update(setC)
# print(setB)

# dish={"name": "Ali", "age": 20}
# dish.update({'grade':"A"})
# print(dish)
# dish.pop('age')
# print(dish)


# a=5
# b=10


# a,b=b,a
# print(a)
# print(b)

# print(15>10 and 10<20)



# listSum=[1, 2, 3, 4, 5]
# print(sum(listSum))

# listRiv=[1, 2, 3, 4]
# listRiv.reverse()
# print(listRiv)




# addTuple=(1, 2, 3)
# list1=list(addTuple)
# list1.append(4)
# print(tuple(list1))

# ------------------------------------------------------------------------------------


#  Check whether a number is even, odd, or divisible by 5**


# a=int(input("Enter The Number : "))

# if a%2==0 and a%5==0:
#     print(f"{a} is even and divisible by 5")
# elif a%2!=0 and a%5==0:
#     print(f"{a} is odd and divisible by 5")
# elif a%2==0 and a%5!=0:
#     print(f"{a} is even and not divisible by 5")
# else:
#     print(f"{a} is odd and not divisible by 5")
    
    
# Check if a number is positive, negative, or zero 
#  number=-3


# num=int(input("Enter The Number : "))

# if num > 0:
#     print("positive")
# elif num< 0:
#     print("Negative")
# else:
#     print("Zero")
    
    
    
#  Traffic light system

# light=input("set light : ")
# if light == 'red':
#     print('Stop')
# elif light == 'yellow':
#     print('Go Slow')
# else :
#     print('Go')
    
    
#  Find the largest among three numbers 
#  a, b, c = 10, 25, 15

# a,b,c=100,25,15


# if c>b and a<c:
#     print(f"{c} is large")
# elif a<b and b>c:
#     print(f"{b} is large")
# else:
#     print(f"{a} is large")


# ----------------------------------------------------------------------------

# problem forloop

# # fint sum

# a=0
# for i in range(1,11):
#     a+=i
    
# print(a)

# -----------------------------

# mult=5
# for i in range(1,11):
#     print(f"{i}X{mult}={mult*i}")
#     # print(i,'x',mult,'=',mult*i)
    
# --------------------------------

# # even numbers


# for i in range(2,21,2):
#     print(i)
    
    
# # ----------------------------------


# # break when number is 7



# for i in range(1,10):
#     if i == 7:
#         break
#     print(i)
    
    
    
# # -----------------------------------

# # continue for skip even number

# for i in range(1,21):
#     if i%2==0:
#         continue
#     print(i)


# ------------------------------------------

# #  Reverse a string using for loop 

# str='python'
# for i in str[::-1]:
#     print(i)
    
    
# Prime number check using loop 

# prime=5
# isPrime=True
# for i in range(2,prime):
#     if prime%i==0:
#         isPrime=False
#         break
    
# if isPrime:
#     print("prime")
# else:
#     print('not prime')
    
# --------------------------------------

# # Factorial of a number

# fact=5
# sum=1
# for i in range(1,fact+1):
#     sum*=i
# print(sum)

# -------------------------------------

#  Print odd numbers from 1 to 20 using while loop

# i=1
# while i<=20:
#     if i%2!=0:
#         print(i)
#     i+=1


# ----------------------------------------------------------------------

# #  3. Write a program that prints "Fizz" if divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.

# n=10
# result=[]
# for i in range(1,n+1):
#             if i%3==0 and i%5==0:
#                 result.append("FizzBuzz")
#             elif i%3==0:
#                 result.append('Fizz')
#             elif i%5==0:
#                 result.append('Buzz')
#             else:
#                 result.append(str(i))

# print(result)


# ------------------------------------------------------------------------------
# # 5. Write a program that prints all numbers from 1 to 50 but **skips multiples of 3**. 

# input=50
# for i in range(1,input+1):
#     if i==3:
#         continue
#     print(i)
    
# -------------------------------------------------------------------
# # 6. Write a program to reverse a string using a loop. 

# str='shanith'
# for i in str[::-1]:
#     print(i)
    
    
# ---------------------------------------------------------------------------------

# #  7. Use a `while` loop to print numbers from 1 to 10.

# i=1
# while i<=10:
#     print(i)
#     i+=1

# ------------------------------------------------------------------------------

# # 8. Write a program to count the number of vowels in a string. 

# vowel="aeiouAEIOU"
# str='caaaaatei'
# count=0

# for i in str:
#     for j in vowel:
#         if i==j:
#             count+=1
# print(count)
# -----------------------------------------------------------------------------------

# #  10. Take a list of numbers and print only the positive numbers. 

# list=[1,2,3,4,5,6]
# for i in list:
#     if i%2==0:
#         print(i)

# ----------------------------------------------------------------------------------

# #  12. Print the Fibonacci series up to `n` terms.

# num=10
# a,b=0,1
# for i in range(num):
#     print(a)
#     a,b=b,b+a

# ---------------------------------------------------------------------------------------
# 13. Write a program that asks the user for numbers until they enter 0, then 

# num=int(input("Enter a number"))
# sum=0
# while num!=0:
#     sum+=num
#     num=int(input("Enter a number"))
# print(sum)

# --------------------------------------------------------------------------------------
#  Write a program that asks for a username and password. If correct, print “Login successful”, else “Invalid credentials” (hardcode username and password).

# userName="shanith"
# passWord="123"

# user=str(input("Enter The User Name : "))
# pas=str(input("Enter The PassWord : "))

# if userName==user and passWord==pas:
#     print("Login successful")
# else:
#     print("Invalid credentials")
    
    
# -----------------------------------------------------------------------------------------
#   A shop gives discounts: 
  
#  5000 → 20% off 
  
#  3000 → 10% off 
  
#  otherwise → 5% off 
#  Write a program to calculate final price.


# amount=int(input("Enter the amout : "))

# if amount>=5000:
#     discount=(20/100)*amount
# elif amount>=3000:
#     discount=(10/100)*amount
# else:
#     discount=(5/100)*amount

# print(f"the amount is {amount-discount}")

# -------------------------------------------------------------------------------

# 20/19/2025

# Function


# def green():
#     print("Hello World")
    
    
# green()
# # -------
# def green_user(name):
#     print(f"Hello {name}")
    
# green_user("shanith")
# # --------
# def square(n):
#     return n**2
# print(square(5))
# # --------
# def add(a,b):
#     return a+b
# print(add(3,6))
# # --------
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
    
# print(is_even(4))
# # ---------

# def fibnonky(n):
#     a,b=0,1
#     result=[]
#     for i in range(n):
#         result.append(a)
#         a,b=b,a+b
#     return result
# print(fibnonky(10))  
# # -------------------------
# def largest(a,b,c):
#     if c>b and a<c:
#      print(f"{c} is large")
#     elif a<b and b>c:
#      print(f"{b} is large")
#     else:
#      print(f"{a} is large")

# largest(10,110,300)
# # --------------------------------

# def prime(number):
#     pre=True
#     for i in range(2,number):
#         if number%i==0:
#             pre=False
#             break
#     if pre:
#         print("it is prime")
#     else:
#         print("it is not prime")
        
        
# prime(12)
# # ----------------------------------

# def reverse(str):
#     newStr=str[::-1]
#     return newStr

# s=reverse("hello")
# print(s)
# # -------------------------------

# def sumOf(lst):
#     sum=0
#     for i in lst:
#         sum+=i
#     return sum

# sum=sumOf([1,2,3,10])
# print(sum)
# # -----------------------------------
# def multiply(m):
#     mult=1
#     for i in m:
#         mult*=i
#     print(mult)
    
# multiply([2,3,4])
# # ---------------------------------------
# # 1, Write a function that defines a local variable x = 10 and prints it. 
# # Outside the function, define another variable x = 20 and print it. 👉 What will be the output?

# x=20
# def Local():
#     x=30
#     print(x)
# print(x)

# Local()
# # -------------------------------------------------
# #  2, Write a function that prints a global variable name = "Python" without redefining it inside the function.

# name="python"
# def globel():
#     print(name)
# globel()
# # ------------------------------------------------------
# #  3, Write a program that modifies two global variables a = 2, b = 3 inside a function. Update them as a = a * 2, b = b + 5.

# a,b=10,10
# def ab():
#     global a,b
#     a=a*2
#     b=b+5
# ab()
# print(a,b)
# # ----------------------------------------------------------

# # 25/09/2025

# # LAMDA FUNCTION

# multiply=lambda a,b:a*b
# print(multiply(2,3))


# max_num=lambda a,b:a if a>b else b
# print(max_num(10,22))


# # Sorting

# pairs=[(1,5),(3,1),(2,4)]
# pairs.sort(key=lambda x:x[1])


# # Lampbda

# #  Create a lambda function to add 10 to a number. Test it with 5. 


# add=lambda a:a+10
# print(add(5))

# #  Write a lambda function to multiply two numbers. Test it with 3 and 4. 

# mult=lambda a,b:a*b
# print(mult(2,3))

# #  Write a lambda function to return the maximum of two numbers. Test it with 10 and 25.

# maxNum=lambda a,b:a if a>b else b
# print(maxNum(20,10))

# #  Given a list [1, 2, 3, 4, 5], use map() and a lambda to create a new list of squares. 

# listA=[1,2,3,4,5]
# listSq=list(map(lambda a:a**2,listA))
# print(listSq)

# # From the list [10, 15, 20, 25, 30], use filter() with a lambda to keep only even numbers. 

# listB=[10,15,20,25,30]
# listEven=list(filter(lambda a:a%2==0,listB))
# print(listEven)

# # Using reduce() and a lambda, find the product of [1, 2, 3, 4].
# from functools import reduce

# listC=[1, 2, 3, 4]
# listSum=reduce(lambda a,b:a+b,listC)
# print(listSum)

# # Sort the list ["apple", "kiwi", "banana", "cherry"] based on word length using a lambda function. 

# frute=["apple", "kiwi", "banana", "cherry"]
# frute.sort(key=lambda a:len(a))
# print(frute)

# #  Given a list of tuples [(1, 5), (2, 1), (3, 8)], use map() and a lambda to extract the second elements [5, 1, 8]. 


# listExtract=[(1, 5), (2, 1), (3, 8)]
# listUpdate=list(map(lambda a:a[1],listExtract))
# print(listUpdate)

# #  Use a lambda and filter() to get only positive numbers from [-5, 3, -2, 7, -1, 0, 4]. 

# listAB=[-5, 3, -2, 7, -1, 0, 4]
# listPsitive=list(filter(lambda a:a>0,listAB))
# print(listPsitive)

# # Write a lambda function that checks if a string is a palindrome. Test it with "madam".
# # str="madam"
# palidrom=lambda a:a[::-1]==a
# print(palidrom("mada"))

# ----------------------------------------------------------------------------------------------

# # 27/09/2025

# # Write a program to find the second largest element in a list. 

# def secont_largest(ls):
#     largest=0
#     secont=0
#     for i in ls:
#         if i>largest:
#             secont=largest
#             largest=i
#         elif i>secont and i !=largest:
#             secont=i
#     return secont
# print(secont_largest([1,2,4,6,2,8,5]))