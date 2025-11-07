from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
     
    def area(self):
       return self.width*self.height

class Circle(Shape):
    def __init__(self,radious):
        self.radious=radious
    
    def area(self):
        return 3.14*self.radious*self.radious
    
R1=Rectangle(10,2)
print(R1.area())

C1=Circle(20)
print(C1.area())