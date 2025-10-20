class Employ:
    class Componey:
        
        def __init__(self,cname,location):
            self.cname=cname
            self.location=location
            
    def __init__(self,name,age,cname,location):
       self.name=name
       self.age=age
       self.componey=Employ.Componey(cname,location)
       
    def display(self):
        print(f" my self {self.name} then my age is {self.age} and  i am working in {self.componey.cname} and it's location at {self.componey.location}")
        
        
        
employ1=Employ("shanith",22,"softronics","perithalmanna")
employ1.display()
employ1.componey.cname="ABC compeny"
employ1.display()