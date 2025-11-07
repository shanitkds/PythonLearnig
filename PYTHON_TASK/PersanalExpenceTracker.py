
store=[]
def Home():
    str="""
    1. Add Expense
    2.View All Expense
    3.Search Expence
    4.Show Total Spent
    5.Exit
    """
    print("\n===========Personal Expence Tracker==============")    
    print(str)
    choice=int(input("Enter The Choise : "))
    if choice==1:
        Add()
    elif choice==2:
        View()
    elif choice==3:
        Search()
    elif choice==4:
        TotalSpent()
    elif choice==5:
        print('\nExit.........')
    else:
        print("Invalid Choise")
        Home()
    
def Add():
    amount=int(input("\nEnter The Amount : "))
    catecory=input("Enter the catecory (Food/Travel/Shopping/Other) : ")
    date=input("Enter the date (YYYY-MM-DD) : ")
    store.append({'amount':amount,'catecory':catecory,'date':date})
    print("\nAdd Sussesfully")
    
    Home()


def View():
    
    print("\n---------- All Expenses -----------")
    print('Amount     Catedory     Date')
    print("------------------------------ ")
    list(map(lambda x:print(f"{x['amount']:<10} {x['catecory']:<15} {x['date']}"),store))
    print("\n")
    Home()
    
def Search():
    t=input("\nSearch by catecory or date? (c/d): ")
    if t=='c':
        ser=input("Enter the category : ")
        ans=list(filter(lambda x:x['catecory']==ser,store))
    elif t=="d":
        ser=input("Enter the date : ")
        ans=list(filter(lambda x:x['date']==ser,store))
    else:
        print("Invalid Try Again")
        Search()
    print("\n---------- Search Expenses --------------")
    print('Amount     Catedory     Date')
    print("------------------------------ ")
    list(map(lambda x:print(f"{x['amount']:<10} {x['catecory']:<15} {x['date']}"),ans))
    print("\n")
    Home()
    
def TotalSpent():
    total= sum(x['amount'] for x in store)
    print(f"\n💰 Total Spent : {total}")
    Home()
    
Home()

