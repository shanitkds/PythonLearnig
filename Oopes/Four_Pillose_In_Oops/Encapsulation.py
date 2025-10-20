# class Employ:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def display(self):
#         print (f"name is {self.name} and slary {self.__salary}")
#     def update(self,salary):
#         self.__salary=salary
        
# e1=Employ("midun",2000)
# e1.display()
# # print(e1.name)
# # print(e1.__salary)

# # e1.name="Afnan"
# # print(e1.name)
# # e1.__salary=3000  #it is not uodating in this methird
# # print(e1.__salary)
# # e1.display()


# # for uodate

# e1.update(3000)
# e1.display()





# QUESTION

# # 1

# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def displayGrade(self):
#         if self.mark >90:
#             grade="A"
#         elif self.mark >70:
#             grade="B"
#         elif self.mark >60:
#             grade="C"
#         elif self.mark >50:
#             grade="D"
#         else:
#             grade="Faild"
        
#         print(f"{self.name}:{self.mark}")
        

# s1=Student("Midun",70)
# s2=Student("Arun",91)

# s1.displayGrade()
# s2.displayGrade()

# 2

class Bank:
    def __init__(self,orner,balance):
        self.owner=orner
        self.__balance=balance
    def depocit(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.__balance+=amount
            print("sussecfully added")
    def widrow(self,amount):
        if self.__balance < amount:
            print("No balence")
        else:
            self.__balance-=amount
            print(f"Your available balance is {self.__balance} ")
            
    def bal(self):
        print(f"Balense is {self.__balance}")


c1=Bank("shanib",200)
c1.bal()
c1.depocit(0)
c1.bal()
c1.widrow(0)
c1.bal()

