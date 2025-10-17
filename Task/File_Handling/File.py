
try:
    file_name=str(input("Enter the file name : "))

    file=open(file_name+".txt","r")
    conent=file.read()
    print(conent)
    file.close()
except FileNotFoundError:
    print( "File not found.")




# file=open("reat.txt","w")
# file.write("Hello shanith")
# file.close()