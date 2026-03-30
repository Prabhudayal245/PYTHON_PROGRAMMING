#jab try block execute hoga tabhi else block bhi execute hoga

#Sometimes we want to run a piece of code when try was successful. 


try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    print(f"the addition of {a} and {b} is {a+b}")
except Exception as e:
    print(e)

else:
    print("addition is succesfull")
