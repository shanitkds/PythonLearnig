# # a='shanith'
# # b=10
# # c=2.4

# # print(type(a))
# # x=10j  #complex
# # print(type(x))
# # e=1111111111111111111111111
# # print(type(e))
# # n=-200000000000000000000000
# # print(type(n))
# # x=35e3
# # print(type(x))
# # q=3+6j
# # print(type(q))
# # string="it's example"
# # print(string)
# # cotes="""fnejrhfuiheiuofjeiujeriugjei 
# # fjeriojfioj  
# # jojoierji 
# # iojoijiji fer 
# # ijfjeifjeri
# # kerjfiojiojojoijoojo 
# # joiejfoooi 
# # ooij9o9o"""
# # print(cotes)
# # print(len(cotes))
# # -------------------------------------------------------------------
# # a="hello, world"
# # print(a[-5:]) #negative

# # c="it's learning"
# # print(c[-13:])
# # print(c[:12])
# # print(c[-8:])

# # u='hello'
# # print(u.upper()) # to change str in to upppercase
# # l='LOWER'
# # print(l.lower()) # to set str in to lowercase
# # s='    Hell   o'
# # print(s.strip()) #strip

# # r='hello'
# # print(r.replace('h','j')) #replace

# # sp='hello, world'
# # print(sp.split(',')) 


# # q='Hello'
# # r='world'
# # print(q+' '+r)  #concatination of join two or more str

# # age=20
# # text=f"my name is shanith, and age is {age}"  #formate


# # print(text)
# # --------------------------------------------------


# # K='mango'
# # print(K.capitalize())  #for capitalize


# # print(10==10)  #boolean
# # a=200
# # b=33
# # print(a>b)

# # -----------------------------------------------------------------------


# # operatars

# # Arithamatical Operation

# # a=1+2
# # b=33-2
# # c=2*3
# # d=10/5
# # m=10%3
# # p=2**3 #power
# # f=10//3 #flow devition for avoid point part
# # print(a,b,c,d,m,p) 
# # print(f)

# # a=30+23
# # b=90-3
# # c=3*3
# # d=23/3
# # f=23%4
# # e=3**3
# # g=12//4
# # print(a,b,c,d,f,e,g)

# # -------------------------------------------------------------------------------

# # x=20 updates it's value by dividing using divinig

# # x=20
# # print(x//3)


# # fint reminder when 29 is divided by 6

# # print(29%6)

# # a=10

# # # a+=10
# # # a-=2
# # # a*=2
# # # a/=5
# # # a%=3
# # a//=3

# # print(a)

# # ---------------------------------
# # x=7

# # # AND
# # print(x<5 and x<10)
# # print(x<8 and x<10)

# # # OR
# # print(x<20 or x<1)
# # print(x<2 or x<1)

# # # NOT
# # print( not x<1)
# # print(not(x<5 and x<10))

# # a='apple'
# # print('p' in a)
# # print('p' not in a)



# # -------------------------------------------------
# # 27/08/2025


# # Identity

# # x=5
# # y=x

# # z=7

# # print(x is z)

# # -------------------------------------------------------------
# # Bitwaise operators



# # print(5&3)
# # print(7&8)

# # print(5|3)

# # print(~5)

# # print(5^3)

# # print(5<<2)  #left shift
# # print(5>>2) #rigt shift

# # --------------------------------------------------------------

# # # List

# lst=['apple','mango',2,1j,2.03]

# # print(lst[-4:-1])

# # lst[0]='oreng'     #for changing
# # # lst[-2]=23
# lst[0:2]=['oreng','banana','catect']

# # lst.append('grapes')
# # lst.insert(1,'watermelone')

# # print(lst)

# # # print(len(lst))
# # # print(type(lst))

# # lst2=[0,34,5]
# # lst.extend(lst2)
# # print(lst)


# # #REMOVE

# # lst.remove('banana')
# # print(lst)


# # lst.pop(1)
# # print(lst)

# # del lst[5]
# # print(lst)

# # lst.clear()
# # print(lst)

# # # del lst
# # # print(lst)

# # #SORTING

# # lstSort=['banana','grape','apple','watermalone']
# # numSort=[8,3,5,2,6,3]

# # lstSort.sort()
# # print(lstSort)

# # numSort.sort()
# # numSort.reverse()
# # numSort.sort(reverse=True)
# # print(numSort)

# # lst4=['Apple','apple','Banana']
# # lst4.sort()                                #upper then lower
# # lst4.sort(key=str.lower)                    #withou upper and lower
# # print(lst4)

# # lst3=lst4.copy()   #copy methord
# # print(lst3)

# # lst5=list(lst4)   #copy methord
# # print(lst5)
# # ------------------------------------------------------------------

# #Tupple

# # tup=(1,4,2,'hello',3j,2.34,'welcome')

# # print(tup[3])
# # print(tup[-5:-1])

# # tup=list(tup)                      
# # tup[1]=22
# # tup=tuple(tup)
# # print(tup)

# # tup=list(tup)
# # tup.insert(1,'Hai')
# # tup=tuple(tup)
# # print(tup)


# # unpaking

# # frutes=('Apple',"Banana","Grapes")
# # (red,yellow,green)=frutes

# # print(red,yellow)

# #ASTHERIK

# # frutes=('Apple',"Banana","Grapes","watermelone",'hello','hai')     
# # (red,*yellow,green)=frutes
# # print(yellow)
# # print(red)


# #Faint count

# # duplipcateTup=('Apple',"Banana","Grapes",'Apple,'"watermelone","Banana",'hello','Apple','hai')     
# # print(duplipcateTup.count('Banana'))


# # Multiply Tupple

# # AB=(2,1,4,6)*3
# # print(AB)
# # --------------------------------------------------------------------------

# # 29/08/2025



# #SET


# # a={1,'hello',2,5}
# # print(a)


# du={1,True,'hello',2,3,4,3,3}    #not allow duplicate
# # print(du)
# # print(len(du),type(du))        #len and type
# # print('hello' in du)    #Memborship Operater


# # du.add('hai')    #for add
# # print(du)

# set2={10,11,32}   #update the set
# # du.update(set2)
# # print(du)

# # #Remove

# # du.remove(10)
# # du.discard(11)
# # print(du)


# # du.pop()
# # print(du)
# # print(du.pop())

# # del du
# # print(du)



# #   JOINS
# # ----------

# # UNIONS

# set3={"bro",32,"cat"}

# # setNew=du.union(set2,set3)
# # print(setNew)

# setNew=du|set2|set3
# # print(setNew)

# #INTESECTION

# # set1={'hello',1,2,3,'hai'}
# # set2={10,11,32,'hai',2} 
# # set3={33,'hai',2,3,6,'hello'}
# # lst1=['22','welcome',54,11,'hai']

# # newSet=set1.intersection(set2)
# # print(newSet)

# # print(set1&set2&set3)

# # INTESECTION-UPDATE

# # set1.intersection_update(set2,set3)
# # print(set1)

# # DIFFERENCE


# # newSet=set1.difference(set2,set3)

# # newSet=set1-set2
# # print(newSet)

# # set1.difference_update(set2,set3)
# # print(set1)


# #SYMMETRIC DIFFERENCE

# set1={'hello',1,2,3,'hai'}
# set2={10,11,32,'hai',2} 
# set3={33,'hai',2,3,6,'hello'}


# # newSet=set1.symmetric_difference(set2)
# newSet=set1^set2
# print(newSet)

# # set1.symmetric_difference_update(set2)
# # print(set1)


# # --------------------------------------------------------------------------
# # 02/09/2025

# #DISHNERY

# a={
#     # 'name':'shanith',
#     'age':22,
#     'place':'kodassheri',
#     'name':'farsana'
# }

# # print(a['name'])
# # print(a['age'])

# # print(len(a))
# # print(type(a))

# # print(a.get("name"))
# # print(a.keys())

# # a['salary']=200
# # print(a)

# # print(a.keys())
# # print(a.values())

# # a['name']='shanith'
# # print(a)

# # print(a.items())
# # print(a)

# # print('name' in a)
# # # print('shanith' in a)

# # a.update({'class':'10th'})
# # print(a)
# a.pop('place')
# # print(a)

# # -------

# b={
#    'id': 1, 
#    'name': "Laptop", 
#    'price': 50000,
#    'disccount':'50%'
# }

# # print(b)
# # b.update({'image':'lap'})
# # # b.pop('disccount')                      //it is the only remove methord in dishnery
# # print(b)

# # b.popitem()   #remove last item in dishnery
# # print(b)

# # del b['name']
# # print(b)
# # # del b
# # b.clear()
# # print(b)

# # # print(b)

# # ------------

# frute={
#     'name':['apple','banana','mango'],
#     'color':['red','yellow','green'],
#     'print':[130,50,]
# }


# # print(frute['name'][1])
# # # frute.pop(['name'][1])
# # print(frute)
# # frute['name'].append("hi") 
# # print(frute)

# # fruteCopy=frute.copy()
# # print(fruteCopy)

# # # ---------------------------------------------------------------------------------------------
# # # 2/09/2025


# # list1=[1,2,3,4]
# # a=frozenset(list1)
# # print(a)


# # setA={2,3,4,5}
# # setFrozen=frozenset(setA)
# # print(setFrozen)


# # a='apple'                  #reverse a string
# # print(a[::-1])


# # b='abcdefghijklmnop'
# # print(b[::-2])






# # nextDish={
# #     'studentA':{
# #         'name':'Afnan',
# #         'age':22
# #     },
    
# #     'studentB':{
# #         'name':"Shanib",
# #         'age':23
# #     }
# # }



# # print(nextDish['studentA']['name'])


# # ------------------------------------------------------------------------------------------
# # 08/09/2025

# # # IF



# # a=5
# # b=33
# # if a>b:
# #     print(a,'>',b)
# #     print(f'{a} > {b}')            #fStri
    
# # else:
# #     print(f'{a} not > {b}')
    
    
    
# # # elif

# # a=10
# # b=11

# # if a>b:
# #     print(f"{a} > {b}")
# # elif a<b:
# #     print(f'{a}<{b}')
# # else:
# #     print(f"{a}=={b}")



# # b=input('enter your name ')
# # print(type(b))




# # a=int(input("enter the marke : "))
# # if a>50:
# #     print('pass')
# # else:
# #     print('fail')
    

# # Shorthand if
# # ---------------

# # if a>50:print("pass")    #shorthand if

# # print("pass") if a>50 else print('fail')  #shorthand if else

# # multiple cundition


    
# # print("A grade") if a>90 else print("B grade") if a>80 else print('C grade') if a>70 else print('D grade')



# # if with logical operater
# # -------------------------


# # a=200
# # b=33
# # c=500


# # if a>b and  b<c :
# #     print('both are true')
# # if a>b or b>c:
# #     print('one is true')
# # if not a<b:
# #     print("not a>b")
    
    
    
# # ---------------------------------------------------------------------------------

# # question)


# # item = input('Enter The Item :')

# # if item == "pizza":
# #     print("$120")
# # elif item == 'burger':
# #     print('$50')
# # elif item == 'pastha':
# #     print('$90')
# # else:
# #     print('$40')
    
    
    
    
# # # nested if
# # # ----------



# # a=91
# # if a>90:
# #     if a>100:
# #         print(f"{a} is greater than 100")
# #     else:
# #         print(f"{a} is greater than 90 and less than 100")
        
# # else:
# #     print(f"{a} is less than 90")




# # for loop
# # -------------

# # a='shanith'         #from text
# # for i in a:
# #     print(i)


# # for i in range(2,12,2):     #range
# #     print(i)

# # a='shanith'
# # for i in a[1:]:
# #     print(i)
    
    
# for i in range(10,1,-1):
#     print(i)
    
# # list1=[1,2,3,4,4,5]
# # for i in list1:
# #     print(i)
    
    
# # for i in range(5):
# #     if i==3:
# #         pass
# #     else:
# #         print(i)
        
    
    
    
# # while loop

# # a=1
# # while a<=5:
# #     print(a)
# #     a+=1
    
    
# # a=10
# # while a>0:
# #     print(a)
# #     a-=1


# # for loop using else
# # -----------------------


# # for i in range(1,11):
# #     print(i)
# # else:
# #     print("loop complited")
    
    
# # loop control statments
# # -------------------------



# # for i in range(1,11):             #break
# #     if i==5:
# #         break
    
# #     print(i)
    
    
    
    
# # for i in range(1,11):              #continue
# #     if i==5:
# #         continue
    
# #     print(i)
    
    
    
    
# # for i in range(1,11):          #pass
# #   pass


# # for i in range(1,7):
# #     if i==3:
# #         pass
# #     print(i)
    
    
    
# # nexted loop
# # -------------


# # for i in range(1,11):
# #     for j in range(1,3):
# #         print(i,j)

# # --------------------------------------------------------------
# #  17/09/2025

# # pattarn printing


# # for i in range(5):
# #     print("  "*(5-i)+"* "*(2*i+1))
# # for i in range(5,-1,-1):
# #     print("  "*(5-i)+"* "*(2*i+1))
    
    

# # for i in range(5):
# #     for j in range((i*2)-1):
# #       print("*",end=" ")
# #     print()
    
# # sum=0
# # for i in range(3):
# #     sum+=i
# # print(sum)



# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()
    
    
    
# # num=1
# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(num,end=" ")
# #         num+=1
# #     print()
    
    
# # n=5
# # number=1
# # for i in range(n):
# #     for j in range(n):
# #         if j==0 or j==n-1 or i==0 or i==n-1:
# #             print(number,end=" ")
# #             number+=1
# #         else:
# #             print(" ",end=" ")
# #     print()
    
    
# #     for i in range(1,6):
# #         print(str(i+' ')*i)
    
#     # -----------------------------------------------------------------------    
#     # appent squer of values into list
    
    
# # squer=[]
# # for i in range(1,6):
# #     squer.append(i**2)
# # print(squer)


# # # list comperhension

# # squer=[i**2 for i in range(1,6)]
# # print(squer)

# # squer=[i for i in range(1,7)]
# # print(squer)

# # squer=[i for i in range(1,11) if i%2==0]
# # print(squer)

# # words=["python","data","science"]
# # words=[i.upper() for i in words]
# # print(words)

# # lst1=[1,2]
# # lst2=[3,4]
# # pairLst=[(i,j) for i in lst1 for j in lst2]
# # print(pairLst)

# # lstQuebs=[i**3 for i in range(1,11)]
# # print(lstQuebs)

# # # vowels
# # vowel="aeiouAEIOU"
# # str="Python Programing"
# # vowelLst=[i for i in str for j in vowel if i==j]
# # print(vowelLst)

# # number=[10,60,45,70,30,100]
# # numberLst=[i for i in number if i>=50]
# # print(numberLst)

# # wordLsrt=["Apple","Banana","cheri"]
# # worLeng=[ len(i) for i in wordLsrt]
# # print(worLeng)

# # evenNumberLst=[i for i in range(1,51) if i%5==0]
# # print(evenNumberLst)

# # -----------------------------------------------------------------------------------------

# # dishnery comprention

# # squer={
# #     x: x**2 for x in range(1,6) if x%2==0
# # }
# # print(squer)

# # # -------------------------------------------------------------------
# # # set comprention

# # lst=[5,10,11,12,8]
# # squerSet={i**2 for i in lst}
# # print(squerSet)


# # ---------------------------------------------------------------------------

# # 20/09/2015

# # FUNCTION


# # def my_function():
# #     print("hello function")
    
# # my_function()


# # # argument and perameter

# # def childrens(name,last_name):
# #     print(f"{name} {last_name}")
    
    
# # childrens("mohammed","afnan")
# # childrens("ahammed","shan")
# # # childrens("ma")


# # # Arbitrary Arguments (*args)

# # def chailds(*chaild):
# #     print(f"the yungest chaild is {chaild[2]} ")

# # chailds("afnan","shanib","anshif")


# # # KeyWord arguments


# # def childs(chaild1,chaild2,chaild3):
# #     print("chailds name is ",chaild1,",",chaild2,",",chaild3)
    
# # childs(chaild1="afnan",chaild2="Amal",chaild3="muhsin")


# # # Aebitrary Keyword Arguments

# # def frut(**name):
# #     print(name["frut1"])
    
# # frut(frut1="Apple",frut2="oreng",frut3="painapple")


# # # Defalt Perameter

# # def country(coun_name="india"):
# #     print(coun_name)
    
# # country()   
# # country("pakisthan")   


# # passing list as a argument

# # def my_fun(food):
# #     for i in food:
# #         print(i,end=" ")
        
# # frunt=['apple','chery','orenge']
# # my_fun(frunt)


# # def add(num1,num2):
# #     return num1+num2


# # print(add(1,2))
# # print(add(2,5))


# # def add(num1,num2):
# #     print( num1+num2)
    
    
# # print(add(1,2))
# # print(add(2,5))


# # # Pass 


# # def pass1():
# #    pass
   

# # pass1()
    
    
# # # Positional Argument

# # def position_only(hai,/):   #only i can pass as a position argument
# #     print(hai)
    
# # position_only("hello")


# # # Keyword Arguments

# # def Keyword_only(*,name):
# #     print(name)
    
# # Keyword_only(name="hello")



# # def position_keyword_arguments(a,b,/,*,c,d):
# #     print(a+b+c+d)

# # position_keyword_arguments(1,2,c=3,d=4)


# # # Recurtion

# # def fact(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #         return n*fact(n-1)

# # factoriyal=fact(5)
# # print(f" factoriyal = {factoriyal}")
# # # -----------------------------------------------------------------------------
# # # 23/09/2025

# # # eskape carectors

# # print("hello\nworld") #for new line
# # print("hello\tworld") #for space
# # print('he is good boy \'good boy\'')#for give como into a string

# # a="python programing"
# # print(len(a))
# # print(a.capitalize())
# # print(a.title())

# # cap="HELLO"
# # sma="World"

# # print(cap.swapcase())
# # print(sma.swapcase())

# # # find

# # print(cap.find("L"))
# # print(a.index("python"))
# # print(a.index("t"))

# # # starts/ends with
# # b="Good Morning"
# # print(b.startswith("Go"))
# # print(b.endswith("ng"))

# # # isDigit

# # print("123".isdigit())
# # print("abcd".isalpha())

# isalnum
# print("abc123".isalnum())

# # # isspace
# # print(" ".isspace())

# # name="shanith"
# # # print(f"my name is {name}")

# # print("my name is {}".format(name))  #this is another f stirng methird
# # -----------------------------------------------------------------------

# # Python Range

# b="Mohammed shanith"
# print(b[7:1:-1])
# print(b[2:8])
# # a=list(range(11,0,-1))
# c=range(1,11)
# # print(a)
# print(c[-4:-1])
# # print(type(c))
# # print(len(c))
# # print(2 in c) #membership


# # Globel variable and Local variable

# # a=10
# # def funvar():
# #     local=33
# #     print(a,'\t',local)
    
# # funvar()
# # # print(local)


# x=20
# def myFunction():
#     global x #define x as a globel
#     x=10
#     print("inside function",x)
    
# myFunction()

# print("outside function",x)

# a,b=10,20
# def globelFunction():
#     global a,b
#     a=a+5
#     b=b+27
# globelFunction()
# print(a,b)


# x=10

# def addFive(x):
#     x=x+5
#     return x
# print(addFive(x))


# ---------------------------------------------------------

import array

# arr=array.array("i",[1,2,3,4,5])
# print(type(arr))
# # print(len(arr))
# arr.remove(2)
# print(arr)



# # # arry program

# arr=array.array("i",[2,4,6,8,10])
# # print(arr)

# arr.append(12)
# print("after appent:",arr)

# arr.insert(2,5)
# print("after insert",arr)

# arr.remove(8)
# print("after remove",arr)

# arr.pop()
# print("after pop",arr)

# print("looping:",end=" ")
# for i in arr:
#     print(i,end=" ")
    
    
# # ---------------------------------------------------------------------------
# 25/09/2025

# # Doc string

# def add(b,c):
#     '''it is adding two functions'''
#     a=b+c 
#     return a  

# print(add(2,3))
# print(add.__doc__)  #for commeant access
# print(help(add))


# # LAMDA FUNCTION

# add=lambda a,b:a+b
# print(add(2,3))

# # MAP

# list1=[2,5,3,8,6,4,7]
# listSquer=list(map(lambda a:a**2,list1))
# print(listSquer)


# # FILTTER

# listEvent=list(filter(lambda a:a%2==0,list1))
# print(listEvent)

# # Reduse

# from functools import reduce   #for import


# q=reduce(lambda x,y:x*y,list1)
# print(q)

# # sorted

# words=["apple","banaba","chery","watermelone"]
# sorWords=sorted(words,key=lambda a:len(a))
# print(sorWords)


# #sort

pairs=[(1,5),(3,1),(2,4)]
pairs.sort(key=lambda x:x[1])
print(pairs)


# studence=[("Alice",85),("Bob",72),("Charlie",90)]  #thihs is map
# marks=list(map(lambda a:a[1],studence))
# print(marks)




# # # Enclosed Scop

# # def outer():
# #     x = "outer variable"
    
# #     def inner():
# #         print("Accessing from inner:",x)
# #     inner()
    
# # outer()



# #Non local

# def outer():
#     x="outer"
    
#     def inner():
#         nonlocal x
#         x="change in outter"
#         print("inner:",x)
#     inner()
#     print("outer:",x)
# outer()

# ---------------------------------------------------------------------------

# # Tail factoriyal


# def tail_fact(n,accumalate=1):
#     if n==0 or n==1:
#         return accumalate
#     else:
#         return  tail_fact(n-1,accumalate*n)
        
# print(tail_fact(5))


# # fibnoncy


# def fibnoncy(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibnoncy(n-1)+fibnoncy(n-2)
    
# print(fibnoncy(6))





# def sum(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+sum(lst[1:])
    
    
# print(sum([1,2,3]))




# ----------------------------------------------------------------------------

# # for study

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)  

# print(factorial(2))



# def tail_factorial(n, result=1):
#     if n == 0:
#         return result
#     return tail_factorial(n - 1, n * result)

# print(tail_factorial(2))