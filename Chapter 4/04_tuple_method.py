a=("hello world",2333,30,443,30,True,39.84,"mango")

count_element=a.count(30) #this function count the given element in the tuple.
print(count_element)

i=a.index(443) # this function return the index number of fist occurence of given element in tuple.
print(i)

#concatenation of two tuples.
tuple1=(1,2)
tuple2=(3,4)
combined=tuple1+tuple2
print(combined)

#repetition of tuple
my_tuple=(1,2,3,4)
repeat=my_tuple*2
print(repeat)

print(len(a)) #lenth of tuple