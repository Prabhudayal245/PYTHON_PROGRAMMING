class employee:
    name="prabhu"
    def eminfo(self):
        print(f"the eployee is {self.name}")

class coder:
    language="Python"
    def showlanguage(self):
        print(f"His favouirte languge is {self.language}")

class programmer(employee,coder):
    company="AMAZON"
    def showcompany(self):
        print(f"He got palced in {self.company} and he used {self.language} laguage" )

o1=programmer()
o1.eminfo()
o1.showlanguage()
o1.showcompany()