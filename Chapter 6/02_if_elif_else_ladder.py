a=int(input("Enetr your age:"))

#if elif else ladder
if(a>=18):     #if condition is true.
    print("You are the age of 18")
    print("You are eligible to vote")

elif(a==0):     #if condition is true.
    print("You enter a zero age which is invalid age.")

elif(a<0):  #if condition is true.
    print("You enter a negative age which is invalid.")

else:       #otherwise
    print("you are below the age of 18\nyou are not eligible to vote")

print("end of the programme")