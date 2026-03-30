#Due to exception handling the program cannot crash if any issue in program.
try:
    a=int(input("Enter a number:"))
    print(a)
except Exception as e:
    print(e)

print("thank you")