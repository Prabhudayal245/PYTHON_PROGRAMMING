class student:
    def __init__(self,name):
        self.name=name

o1=student("Prabhu")
print(o1.name)
del o1.name
del o1