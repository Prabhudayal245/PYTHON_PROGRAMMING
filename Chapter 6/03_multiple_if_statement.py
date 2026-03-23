a=int(input("Enetr your age:"))

#if statement no:01
if(a%2==0):
    print("a is even")
#end of if statement no:01


#if statement no:02
if(a>=18):     #if condition is true.
    print("You are the age of 18")
    print("You are eligible to vote")

elif(a<0):  #if condition is true.
    print("You enter a negative age which is invalid.")

else:       #otherwise
    print("you are below the age of 18\nyou are not eligible to vote")
#end of if statement no:02

print("End of progamme")