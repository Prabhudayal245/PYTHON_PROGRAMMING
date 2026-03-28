#creating a class:
class student:
    #class attributes:
    ClassTeacher="XYZ"       
    Branch="COE"
    subject=["maths","FDA","IKS","Physics","English"]
    uniform="Pant Shirt"
    bag="college bag"

    def greet(self):
        print(f"Good Morning! {self.name}")

    def getInfo(self):
        print(f"The ClassTeacher is {self.ClassTeacher} and The subject is{self.subject}")

prabhu=student()  #object1
prabhu.name="Prabhudayal"    #object/instance attributes 
prabhu.greet()  #it convert into student.greet(prabhu)
prabhu.getInfo() #it convert into student.getInfo(prabhu)

krish=student()  #object2
krish.name="krish"    #object/instance attributes 
krish.greet()  #it convert into student.greet(krish)
krish.getInfo() #it convert into student.getInfo(krish)
