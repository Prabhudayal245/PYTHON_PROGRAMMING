f=open("file.txt")
# readlines() Function:
# lines=f.readlines()
# print(lines,type(lines))

# readline() Function:
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
# line4=f.readline()
# print(line4)

line=f.readline()
while(line!=""):
    print(line,end="")
    line=f.readline()
   
f.close()

