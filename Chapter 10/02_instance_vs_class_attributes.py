# Note: Instance attributes, take preference over class attributes during assignment & retrival.


#creating a class:
class student:
    #class attributes:
    name="pratik"
    ClassTeacher="XYZ"       
    Branch="COE"
    subject=["maths","FDA","IKS","Physics","Englisg"]
    uniform="Pant Shirt"
    bag="college bag"


prabhu=student()  #object1
prabhu.name="Prabhudayal"    #object/instance attributes 
print(prabhu.name,prabhu.ClassTeacher,prabhu.Branch,prabhu.subject,prabhu.uniform)

krish=student()   #object2
krish.name="krish"   #object/insatance attributes
print(krish.name,prabhu.ClassTeacher,prabhu.Branch,prabhu.subject,prabhu.uniform)




    
   