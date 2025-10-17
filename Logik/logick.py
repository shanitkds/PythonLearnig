n=5
for i in range(n):
    for j in range(i):
        print(j+1,end=" ")
    print()
    
    
    
str="the cat and the dog"
words=str.split(" ")
dish={}
for word in words:
    dish[word]=words.count(word)
print(dish)
# print(str.count())