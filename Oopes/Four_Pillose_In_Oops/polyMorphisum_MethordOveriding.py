
# # Polymorphism
# # It allows the same function or method to behave differently depending on the object or data type it is working with


# class Animal:
#     def speak(self):
#         return "The animal makes a sound"

# class Dog(Animal):
#     def speak(self):
#         return "wwwwwww"

# class Cat(Animal):
#     def speak(self):
#         return "ccccccccccccc"

# cat = Cat()
# print(cat.speak())

# dog = Dog()
# print(dog.speak())



# # Method Overriding in Python
# # a child class (subclass) has a method with the same name as a method in the parent class (superclass),
# # but the child’s version replaces (overrides) the parent’s version when called.



# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):       
#         print("Dog barks")


# a = [Animal(),Dog()]

# for i in a:
#     i.sound()





# # Duck Type


# class Cat():
#     def __init__(self,name):
#         self.name=name
#     def speack(self):
#         print(f"ccccc ")
        
# class Dog():
#     def __init__(self,name):
#         self.name=name
#     def speack(self):
#         print(f"dddddddd ")
        
# class Duck():
#     def __init__(self,name):
#         self.name=name
#     def speack(self):
#         print(f"dudududududu ")
        

# def animal_sound(animal):
#     print(f"{animal.name}")
#     animal.speack()
    
# dog=Dog("dog")
# cat=Cat("cat")
# duck=Duck("duck")

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(duck)





# # question


# class Bird():
#     def sound(self):
#         print("bird make sount")
        

# class Pareot():
#     def sound(self):
#         print("paret say hello")
        
# class Sparrow():
#     def sound(self):
#         print("sparrow say hai")
    
# def bird_sound(bird):
#     bird.sound()
    
# paret=Pareot()
# sparrow=Sparrow()

# bird_sound(paret)
# bird_sound(sparrow)





# # question 2

# class Student():
#     def __init__(self,name,**marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         total=0
#         for i in self.marks:
#             total+=self.marks[i]
#         count=len(self.marks)
#         avg=total//count
#         return avg
        
#     def grade(self):
#         avg=self.average()
#         grade=''
#         if avg>=90:
#             grade="A"
#         elif avg>=75:
#             grade="B"
#         elif avg>=50:
#             grade="C"
#         else:
#             grade="Fail"
#         print(f"{self.name}'s Average : {avg} | Grade:{grade}")
# s1=Student("Shanith",english=20,maths=70,it=90)
# s2=Student("Afna",english=100,maths=80,it=90)
# s1.grade()
# s2.grade()


# lst = [10, 8, 6, 7, 9, 11, 12]
# is_consecutive = len(lst) == len(set(lst)) and max(lst) - min(lst) + 1 == len(lst)
# print(is_consecutive)



# # question 3 Laibarery Managment


# class Book:
#     def __init__(self,title,auther,copies):
#         self.title=title
#         self.auther=auther
#         self.copies=copies
#     def display(self):
#         print(f"Title:{self.title}|Auther:{self.auther}|copies:{self.copies}")
    
        
        
# store=[]
# for i in range(2):
#     print("Enter Book Info")
#     title=input("Enter Title: ")
#     auther=input("Enter Auther: ")
#     copies=input("Number of Copies: ")
#     store.append(Book(title,auther,copies))


# def search(name):
#     found=False
#     for i in store:
#         if i.title==name:
#             i.display()
#             fount=True
#             return
        
#     if not found:
#         print("Book not available")
       
# name=input("Enter Search Name")     
# search(name)


# Question 4 Employ Bouns Systrem

# class Employ:
#     def __init__(self,name,postion,salary):
#         self.name=name
#         self.postion=postion
#         self.salary=salary
#     def display_info(self):
#         print(f"Name: {self.name} | Position: {self.postion} | Salary: {self.salary}")
    

# def update(salary,per):
#     amount=(per/100)*salary
#     salary+=amount
#     return salary




# Store=[]
# for i in range(2):
#     print("Enter employ info")
#     name=input("Enter The Name : ")
#     postion=input("Enter The position : ")
#     salary=int(input("Enter The Salary : "))
#     bouns=int(input("Enter Bouns : "))
#     update_salary=update(salary,bouns)
#     Store.append(Employ(name,postion,update_salary))
    
# for i in Store:
#     i.display_info()
    
    
# # Question 5 ,Shoping Cart

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
        
# class Cart:
#     def __init__(self):
#         self.pro=[]
#     def add(self,product):
#         self.pro.append(product)
#     def total(self):
#         return sum(map(lambda i:i.price,self.pro))
# cart=Cart()
# for i in range(2):
#     name=input("Enter Name : ")
#     price=int(input("Enter The Price"))
#     product=Product(name,price)
#     cart.add(product)
    
# print(f"Total Price : {cart.total()}")



# # Question 6,Movie Ticket Booking

# class Movie:
#     def __init__(self,title,av_seats):
#         self.title=title
#         self.av_seats=av_seats
#     def book_tickets(self,seats):
#         if seats<=self.av_seats:
#             self.av_seats-=seats
#             print(f"{seats} seats booked")
#             return True
#         else:
#             print("Not Enough Seats")
#             return False
            
            
# name=input("Enter Move Title")
# seats=int(input("Enter seats number"))
# movie1=Movie(name,seats)
# while True:
#     book=int(input("Enter Seats to Booke"))
#     if not movie1.book_tickets(book):
#         break
    
    
    
# # Question 8,Loan Eligibility

# class Customer:
#     def __init__(self,name,incom,creadit_score):
#         self.name=name
#         self.incom=incom
#         self.creadit_score=creadit_score
#     def check_eligible(self):
#         if self.incom>=25000 and self.creadit_score>=650:
#             print(f"{self.name} is eligible")
#         else:
#             print(f"{self.name} is not eligible")
            
            
# name=input("Enter your name")
# incom=int(input("enter your incom"))
# creadit=int(input("Enter Your incom"))
# custamer1=Customer(name,incom,creadit)
# custamer1.check_eligible()


# Question 9,Order Traker

store=[]
class Order:
    def __init__(self,id,name,status):
        self.order_id=id
        self.product_name=name
        self.status=status
        
    def display(self):
        print(f"{self.order_id}-{self.product_name}-{self.status}")
        
    def update(self,status):
        self.status=status
        
    
    
for i in range(1):
    id=int(input("Enter The Id: "))
    name=input("enter the product name: ")
    status=input("enter the status: ")
    store.append(Order(id,name,status))
    
    
def Ask():
    str=input("Do you want to update?(yes/no)")
    if str=="yes":
        Update()
    elif str=="no":
        print("Update Orders")
        for i in store:
            i.display()
    else:
        print("invalid")
    
def Update():
    id=int(input("enter the id: "))
    faint=False
    for i in store:
        if i.order_id==id:
            status=input('enter the new status: ')
            i.update(status)
            faint=True
            print("Updated")
            break
    if not faint:
        print( "invalid ID")
    Ask()
            


def Current():
    print("Current Order")
    for i in store:
        i.display()
    Ask()
        
        
Current()