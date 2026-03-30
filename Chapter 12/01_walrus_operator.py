a=False
print(a)

print(a:=True)   # := is a walrus operator

# foods=[]
# while True:
#     food=input("What fruit you would like to?:")
#     if(food=="quit"):
#         break
#     foods.append(food)
# print(foods)

#instead of using above example we can use walrus operator 

foods=[]
while((food:=input("What food whould you like?:"))!="quit"):
    foods.append(food)

print(foods)