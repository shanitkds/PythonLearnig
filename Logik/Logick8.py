# def commen(lst1,lst2):
#     set1=set(lst1)
#     set2=set(lst2)
    
#     new=set1&set2
#     print(list(new))
    
# commen( [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100])



def star(num):
    for i in range(num, 0, -1):
        print(" " * (num - i) + "*" * (2 * i - 1))
    
        
star(4)

