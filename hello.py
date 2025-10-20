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


def romanToInt(s):
    rs={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900
    }
    
    sum=0
    i=0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in rs:
            sum+=rs[s[i:i+2]]
            i+=2
        else:
            sum+=rs[s[i]]
            i+=1
        
    return sum
        
 
        
        
print(romanToInt("MCMXCIV"))