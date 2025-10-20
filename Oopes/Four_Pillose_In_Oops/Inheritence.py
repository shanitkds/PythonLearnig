# Single Inheritence

class Animal:
    def __init__(self,name):
        self.name=name
        
    def sound(self):
        print("No sountd")
class Dog(Animal):
    # pass
     def sound(self):
         print(f"{self.name} sound is wwwww")
        
dog=Dog("buddy")
dog.sound()