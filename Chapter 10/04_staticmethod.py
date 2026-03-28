#creating a class:
class student:
    #class attributes:
    ClassTeacher="XYZ"       
    Branch="COE"
    subject=["maths","FDA","IKS","Physics","Englisg"]
    uniform="Pant Shirt"
    bag="college bag"

    @staticmethod   #we don't need to pass object/self in function if in the function do not use object/self then we use @staticmethod to run the function without passing object/self as an parameter in function.
    def greet():
        print("Good Morning")

    def getInfo(self):
        print(f"The ClassTeacher is {self.ClassTeacher} and The subject is{self.subject}")

prabhu=student()  #object1
prabhu.name="Prabhudayal"    #object/instance attributes 
prabhu.greet()  #it convert into student.greet(prabhu)
prabhu.getInfo() 



'''
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")

# Calling the static method
MyClass.my_static_method()  # Works without creating an instance/object

obj = MyClass()
obj.my_static_method()  # Can also be called from an instance/object, but not recommended
'''
