# class Car:
#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price
        
#     def display(self):
#         return f"{self.make} {self.model} {self.year} - {self.price}"
    
# car1=Car("Toyota","cammery",2020,24000)
# print(car1.display())



# iphone objects


class Iphone:
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
   
    
    def display(self):
        
        print(f"This is an {self.color} color {self.model} it's price is {self.price}")


iphone11=Iphone("Iphone11","Green",30000)
iphone12=Iphone("Iphone12","Yelllow",40000)
iphone14=Iphone("Iphone14","Blue",45000)
iphone15=Iphone("Iphone15","Pinck",50000)
iphone16=Iphone("Iphone16","Grey",55000)

iphone14.model="iphone20"
print(iphone14.model)

iphone11.display()
iphone14.display()
iphone12.display()
iphone15.display()
iphone16.display()




# The __str__() Method
# --------------------

class Fruet:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def __str__(self):
        return f"{self.name} price is {self.price}"
        
        
fruet1=Fruet("Apple",50)
print(fruet1)



print(type(fruet1))

print("Hello World")