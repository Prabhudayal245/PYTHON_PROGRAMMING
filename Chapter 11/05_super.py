class employee:
    name="prabhu"
    def __init__(self):
        print("constructor of emplyee class")
    
class programmer(employee):
    language="Python"
    def __init__(self):
        print("constructor of programmer class")

class manager(programmer):
    company="Google"
    def __init__(self):
        super().__init__()   #super method use to take parent __init__() function
        print("constructor of mananager class")

o1=manager()
print(o1.name,o1.language,o1.company)
