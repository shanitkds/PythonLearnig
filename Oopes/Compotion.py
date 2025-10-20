

# class Compeny:
#     def __init__(self,cname):
#         self.cname=cname
        
        
        
# class Employ:
#     def __init__(self,name,age,cname):
#         self.name=name
#         self.age=age
#         self.componey=Compeny(cname)
        
#     def display(self):
#         print(f"my name {self.name} componey is {self.componey.cname}")
 
 
# Employ1=Employ("shanith",21,"ABC")
# Employ1.display()


# # taitly Coupled


# class Engin:
#     def __init__(self,enginName):
#         self.engin=enginName
        
    
# class Car:
#     def __init__(self,name):
#         self.name=Engin(name)
        
# car=Car("V2")
# # print(car.name.engin)

# # del car


# try:
#     print(car.name.engin)
# except NameError as e:
#     print(f"Error:{e}")
    
    
# loosly coupled

class Company:
    def __init__(self,cname,location):
        self.cname=cname
        self.location=location
class Employ:
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.componey=company
    def display(self):
        return f"My name is {self.name} and my compant name is {self.componey.cname} then age {self.age} my company location at {self.componey.location}"
    
del Employ
c1=Company("abc company","pandikkad")
employ=Employ('shanith',34,c1)
print(employ.display())


try:
    print(c1.cname)
except NameError as e:
    print(f"Error:{e}")