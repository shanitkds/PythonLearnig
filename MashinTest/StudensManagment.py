store=[]



def Choice():
    ch=int(input("Enter Your Choise: "))
    if ch == 1:
        AddStudent()
    elif ch==2:
        Display()
    elif ch==3:
        Topper()
    elif ch==4:
        print("Exiting...")
    else:
        print("\ninvalid number")
        Choice()
        

def Home():
    str="""
    --- Student Marks Analysis ---
    
    1. Add Student
    2. Display All Students
    3. Find Topper
    4. Exit

    """
    Choice()
    


def AddStudent():
    lst=[]
    name=input("Enter the Sudent Name: ")
    mark=input("Enter the Marks: ")
    for i in mark.split(","):
        lst.append(i)
    store.append({"name":name,"mark":lst})
    print(f"{name} added successfully!\n ")
    Choice()


# ---------------------------------------------
# Display Students

def Average(mark):
    total=0
    for i in mark:
        total+=float(i)
    return total//len(mark)
     
def Display():
    for i in store:
        avg=Average(i['mark'])
        print(f"Name: {i['name']}|Mark: {i['mark']}|Average: {avg}")
    print("\n")
    Choice()
    
# ---------------------------------------------------------
# Faint Topper
def Topper():
    tav=0
    topper=''
    for i in store:
        avg=Average(i["mark"])
        if avg > tav:
            tav=avg
            topper=f"{i['name']} (Average: {avg})"
            
    print(f"Topper: {topper}")
Home() 