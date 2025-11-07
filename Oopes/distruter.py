class Boy:
    def __init__(self,name):
        self.name=name
        print(f"my name {self.name} created")
    def __del__(self):
        print(f"{self.name} destroyde")
        
        
b1=Boy("shanith")