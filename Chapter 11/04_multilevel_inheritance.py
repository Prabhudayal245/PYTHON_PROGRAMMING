class employee:
    name="prabhu"
    def showname(self):
        print(f"the employee name is:{self.name}")

class programmer(employee):
    language="Python"
    def showlanguage(self):
        print(f"the {self.name} work on {self.language}")

class manager(programmer):
    company="Google"
    def manage(self):
        print(f"the {self.name} is a manager of {self.company}")

o1=manager()
o1.showname()
o1.showlanguage()
o1.manage()