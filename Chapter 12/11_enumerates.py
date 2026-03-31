l=[1,23,34,2,3,2]
# index=0
# for item in l:
#     print(f"the item number at index {index} is{item}")
#     index=index+1

#this can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"the item number at index {index} is {item}")
    