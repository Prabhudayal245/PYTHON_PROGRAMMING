#creating a class:
class student:
    
    #Constructor
    def __init__(self,name,branch,teacher):   #dunder function
        print("I am creating a object")
        # creating instance attribute
        self.name=name   
        self.branch=branch
        self.teacher=teacher
        # print(self.name,self.branch)
        
        
#object1
prabhu=student("prabhudayal","COE","XYZ")
print(prabhu.name,prabhu.branch,prabhu.teacher)

#object2
krish=student("krish","COE","XYZ")
print(krish.name,krish.branch,krish.teacher)
