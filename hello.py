# print('hello')
# x=100
# y='apple'
# print(y,x)

# z=int(25.5)
# print(z)
# print(type(z))
# q,w=10,11
# print(q,w)
# x=y=z=112
# print(x,y,z)
# a='Mohammed '
# b='Shanith'
# print(a+b)



# list1=[1,3,4,6,2]



# for i in list1:
#     print(i)
    
    
    
# a=sum(2+4)
# print(a)


def convert(num):
    result=''
    while num >0:
        num-=1
        remainder=num%26
        result=chr(65+remainder)+result
        num //=26
        print(num)
    print(result)  
        
convert(701)