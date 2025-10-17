# filecreate
# ------------

# file=open("sample.txt","w")
# file.close()

# create in different __path
# ---------------------------

# file=open("C:/Users/HP/Desktop/Softronics/new/softronics/sample.txt","w")
# file.close()


# # filr reade
# # ----------

# # read()
# # -----

# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()

# # redline()
# # -------

# file=open("sample.txt","r")
# line1=file.readline()
# print(line1)
# line2=file.readline()
# print(line2)
# file.close()

# # this using forloop
# # ----------------
# file=open("sample.txt","r")
# for i in file:
#     print(i.strip())  #.strinp() is used to avoid the space
# file.close()




# # 3. readlines() Method 
# # ---------------

# file=open("sample.txt","r")
# line=file.readlines()
# print(line)
# file.close()


# WRITE
# -----

# # 1. write() Method
# # -----------------


# file=open("sample.txt","w")
# file.write("Hello , World!")
# file.close()


# # 2. writelines() Method
# # --------------------------

# file=open("sample.txt","w")
# line=["good ","morning\n","Today is Monday\n"]
# file.writelines(line)
# file.close()


# # 6. Appending Data 

# file=open("sample.txt","a")
# file.write("Appented New one\nit can update new value")
# file.close

# # 7. Using with Statement 

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)
    
    
# # 8. File Positioning (Seek and Tell)

# #  tell(): Returns the current file cursor position. 

# file=open("sample.txt","r")
# content=file.read()
# position=file.tell()
# print(position)
# print(content)
# file.close()

#     #  seek(offset, from_what): Moves the file cursor to a specified 
#     # position.

file = open("sample.txt", "r") 
file.seek(5)  # Move to 5th byte from the start 
print(file.read()) 
file.close()

