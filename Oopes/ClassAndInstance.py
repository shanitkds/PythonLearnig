class Compeny:
    CompenyName="ABC Compeny"
    def __init__(self,id,name,position):
        self.id=id
        self.name=name
        self.position=position
        
    
    
employ1=Compeny(1,"marvan","python")
employ2=Compeny(2,"sharath","flutter")

print(employ1.name)
print(employ2.name)

print(employ1.CompenyName)
print(employ2.CompenyName)