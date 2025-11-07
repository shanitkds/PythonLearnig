def largest(lst):
    lst.sort()
    dif=0
    for i in range(0,len(lst)-1):
        val=lst[i+1]-lst[i]
        if dif < val:
            dif=val
            
    print(dif)
    
largest([2, 5, 9, 1])