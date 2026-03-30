from typing import List,Tuple,Union,Dict
# num:int=5
# print(num)

# name:str="prabhu"

numbers:List[int]=[1,2,3,5,6]
print(numbers)

library:Dict[str,int]={"prabhu":3,"radhe":3}
print(library)

data:Tuple[str,int,bool]=("banana",False,389)
print(data)

std:Union[int,str]="std1"
print(std)

def greet(name:str)->str:
    return f"Good Afternoon {name}"

print(greet("prabhu"))