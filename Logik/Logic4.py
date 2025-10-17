

def most(s):
    a = sorted(s)
    count = 1
    dish = {}
    
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            count += 1
        else:
            dish[a[i - 1]] = count
            count = 1
    dish[a[-1]] = count 
    
    sorted_dish = sorted(dish.items(), key=lambda x:-x[1])
    
    for i,a in sorted_dish[:3]:
        print(i,a)
    
    
    
most("aabbbllllllccccl")


