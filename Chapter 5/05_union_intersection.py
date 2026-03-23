s1={1,5,9,3}  #set1
s2={2,3,6,8}  #set2

print(s1.union(s2)) # returns both set each other 
print(s1.intersection(s2)) # return common values from both sets


print({5,3}.issubset(s1))  #subset
print(s1.issuperset({1,9})) #superset
