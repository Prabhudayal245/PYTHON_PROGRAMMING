class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"the employee email is {self.fname}{self.lname}@gmail.com"

    def name(self):
        return f"the employee name is {self.fname} {self.lname}"
    
    @property
    def email(self):
        return f"the employee email is {self.fname}{self.lname}@gmail.com"
    



o1=employee("prabhu","dayal")
print(o1.name())
o1.fname="guru"
print(o1.email)
# o1.email="hello@gmail.com"
