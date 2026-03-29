class employee:
    name="prabhu"
    def __init__(self):
        print(f"the eployee is {self.name}")

class programmer(employee):
    language="Python"
    def showlanguage(self):
        print(f"His favourite language is {self.language}")


o1=programmer()
o1.showlanguage()