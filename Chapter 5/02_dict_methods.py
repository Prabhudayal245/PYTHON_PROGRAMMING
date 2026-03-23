new_dict={}  #empty dictionary

dict={
    "Name":"Prabhu",
    "Marks":95,
    "Roll_no":45,
    "Branch":"COE",
    "friends":["manish","saurabh","abhishek","arun"]
    }

print(dict.items())  #this function return the key and values  pairs.

print(dict.keys())  #this function returns the keys of dictionary.

dict.update({"Marks":96,"room no":616}) # this function upadate previous data as well as we add new data in the dictionary. 
print(dict)  

print(dict.get("Marks"))  #this function  returns values of specified keys.eg. "96" is return here.
print(dict.get("fruits"))  # If the key does not exist, it returns the default value "None".


print((dict.pop("room no"))) #it Removes and Returns the values of specified keys.if keys is not found it by default return None.
print(dict)

dict.popitem() #Removes and returns a random (key, value) pair from the dictionary. Raises a KeyError if the dictionary is empty.
print(dict)

dict.clear()  # it remove all items from dictionary.
print(dict)