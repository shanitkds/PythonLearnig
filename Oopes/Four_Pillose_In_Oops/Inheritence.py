# Single Inheritence

# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def sound(self):
#         print("No sountd")
# class Dog(Animal):
#     # pass
#      def sound(self):
#          print(f"{self.name} sound is wwwww")
        
# dog=Dog("buddy")
# dog.sound()




# # Multiple Inheritence

# class Engine:
#     def start_engin():
#         print("engin started")

# class Weel:
#     def rotating():
#         print("weel is rotating")
# class Car(Engine,Weel):
#     def moving():
#         print("car is moving")
    
# car=Car
# car.start_engin()
# car.rotating()
# car.moving()




# # Mmultilevel inheritence

# class Granparent:
#     def dance(self):
#         print("granparent dancing")
        
# class Parent(Granparent):
#     def swim(self):
#         print("parent Swiming")
# class Chaild(Parent):
#     def sing(self-):
#         print("chaild singing")
        
# chaild1=Chaild
# chaild1.dance()
# chaild1.swim()
# chaild1.sing()


# # Haigherarchical  inheritence

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print(f"{self.name} no sound")
# class Cat(Animal):
#     def sound(self):
#         print(f"{self.name} cccccc")
# class Dog(Animal):
#     def sound(self):
#         print(f"{self.name} dddddddddd")

# dog=Dog("dogs")
# dog.sound()

# cat=Cat("cat")
# cat.sound()


# hghibrid inheritence

class A:
    def mehord_A(self):
        print("mehord from class A")

class B(A):
    def methrd_B(self):
        print("mehord from class B")
        
class C(A):
    def methrd_C(self):
        print("mehord from class C")
        
class D(B,C):
    def methrd_D(self):
        print("mehord from class D")
        
d=D()
d.mehord_A()
d.methrd_B()
d.methrd_C()
d.methrd_D()