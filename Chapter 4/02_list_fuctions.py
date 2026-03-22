list_items=["apple","onion",3,93.23,False,None,"harsh"]
print(list_items)

list_items.append("prabhu") #This function add data at the end of list.
print(list_items)

list_items.insert(3,True) #This function insert data at given index. here 3 is a index and True is insert at 3 index of list
print(list_items)

delete=list_items.pop(3) #pop function remove the element at the given index and it cannot return value
print(delete)

list_items.remove(3)
print(list_items)

new_list=[1,2,7,8,15,21]

new_list.sort()  #This function sort the data and update it.
print(new_list)

new_list.reverse() #This function reverse the element of list.
print(new_list)

print(sum(new_list))  #sum  is a functio that is used to sum of element in the data.