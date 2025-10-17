# def Anagrams(str1,str2):
#     a=sorted(str1)
#     b=sorted(str2)
#     # print(a)
#     if a==b:
#         print("Strings are Anagrams")
#     else:
#         print("Strings are not Anagrams")
   
    
    
# Anagrams("LISTEN","SILENT")


def DB(num):
    answer=''
    while num>0:
        a=num%2
        answer=str(a)+answer
        num=num//2
        
    return answer

print(DB(7))