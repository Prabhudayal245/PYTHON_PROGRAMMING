a=int(input("Enter the number:"))
b=int(input("Enter the number:"))

if(b==0):
    raise ZeroDivisionError("hey the program cannot divide any number by zero")
else:
    print(f"the division is {a/b}")