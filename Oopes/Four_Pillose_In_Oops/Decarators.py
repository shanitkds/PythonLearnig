# def abcdd(func):
#     def wappa():
#         print("Before calling the function")
#         result=func()
#         print(result)
#         print("After calling the function")
#     return wappa


# @abcdd
# def greet():
#     return 'Hello World'

# greet()



# Class Methord



# class Company:
#     company_name="Teck_solution"
    
#     @classmethod
#     def change_componey_name(cls,new_name):
#         cls.company_name=new_name
        
# Company.change_componey_name("Softronics")
# print(Company.company_name)






# class Company:
#     company_name="Teck_solution"
    
#     @classmethod
#     def change_componey_name(cls,new_name):
#         cls.company_name=new_name
        
# print(Company.company_name)  #Not Change in this

      
        
# class ChangeCompany(Company):
#     pass

# ChangeCompany.change_componey_name("ABC Componey")            #Only Change in this 
# print(ChangeCompany.company_name)



# Static Methord

class MathOperation:
    @staticmethod
    def Add(a,b):
        return a+b
    
obj1=MathOperation()
print(obj1.Add(2,2))




