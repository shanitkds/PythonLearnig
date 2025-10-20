# def Merge(arr1,arr2):
#     set1=set(arr1)
#     set2=set(arr2)
#     newSet=set1|set2
#     newList=list(newSet)
#     print(newList)
    
# Merge([1, 3, 5], [2, 3, 6])


# def Add(arr,target):
#     pairs=[]
#     CheckVal=[]
#     for i in arr:
#         num=target-i
#         if num in CheckVal:
#             pairs.append([num,i])
        
#         CheckVal.append(i)
#     print(pairs)
        
        
# Add([1, 2, 3, 4, 5, 6], 7)


def isHappy(n):
        seen=[]
        while n !=1:
            if n in seen:
                return False
            seen.append(n)
            val=0
            for digits in str(n):
                val+=int(digits)**2
            n=val
            print(val)
        return True
print(isHappy(7))