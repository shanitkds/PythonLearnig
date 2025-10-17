

# file=open("ReadOnly.txt","r")
# content=file.read()
# print(content)
# file.close()

try:
    file=open("ReadOnly.txt","w")
    file.write("Hello World")
    file.close()
except PermissionError:
    print("Permission denied!") 