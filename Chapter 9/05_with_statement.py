# f=open("file.txt","r")  #Open a file.
# data=f.read()   #Taking content of file.
# print(data)
# f.close()

# the same part we also do as with statement. 
# Open the file in read mode using 'with', which automatically closes the file 

with open("file.txt", "r") as f: 
    # Read the contents of the file 
    text = f.read() 

# Print the contents 
print(text)