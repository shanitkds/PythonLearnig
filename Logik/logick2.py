def automorphic(num):
    square=str(num**2)
    length=len(str(num))
    
    # if square.endswith(str(num)):
    if square[-length:]==str(num):
        print("it is a automorphic")
    else:
        print("it is not a automorphic")
        
automorphic(5)


# -----------------------------------------------------------------------------------

def game(str):
    
    vowels='AEIOU'
    Stuart=0
    Kevin=0
    length=len(str)
    
    for i in range(length):
        if str[i] in vowels:
            Kevin+=length-i
        else:
            Stuart+=length-i
    
    if Stuart>Kevin:
        print('Stuart :',Stuart)
    elif Kevin>Stuart:
        print('Kevin :',Kevin)
    else:
        print('Draw')
        
game('BANANA')