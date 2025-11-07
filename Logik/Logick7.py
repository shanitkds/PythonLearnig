# Store=[]
# def Home():
#     str="""
#     1.Add
#     2.Total
#     3.Average mark list
#     4.Topper
#     """
#     print(str)
#     a=int(input("Enter Your Choice : "))
#     if a==1:
#         Student()
#     elif a==2:
#         Total()
#     elif a==3:
#         Average()
#     else:
#         Topper()
# def Student():
#     no=int(input("Enter No : "))
#     maths=int(input("enter maths mark : "))
#     english=int(input("enter english mark : "))
#     it=int(input("enter it mark"))
#     Store.append({'no':no,'maths':maths,'english':english,'it':it})
#     Home()
    
# def Average():
#     for i in Store:
#         total=i["maths"]+i["english"]+i["it"]
#         Average=total/3
#         print(f"{i["no"]} : {Average}\n")
        
# def Total():
#     for i in Store:
#         total=i["maths"]+i["english"]+i["it"]
#         print(f"{i["no"]} : {total}\n")
#     Home()
        
# def Topper():
#     top=0
#     topNo=0
#     for i in Store:
#         total=i["maths"]+i["english"]+i["it"]
#         if top<total:
#             top=total
#             topNo=i["no"]
#     print(f"Topper is : {topNo}")
#     Home()
            
# Home()




# def num(a):
#     for i in range(a):
#         for k in range(a-i-1):
#             print(" ",end="")
#         for j in range(1,i+2):
#             print(j,end="")
#         for l in range(i,0,-1):
#             print(l,end="")
            
#         print() 
#     for i in range(a-1,0,-1):
#         for k in range(a-i):
#             print(" ",end="")
#         for j in range(1,i+1):
#             print(j,end="")
#         for l in range(i-1,0,-1):
#             print(l,end="")
            
#         print()   
            
            
# num(5)


#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1