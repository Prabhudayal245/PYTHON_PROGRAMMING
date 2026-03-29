class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class attribute is {cls.a}")

o1=employee()
o1.a=30
o1.show()