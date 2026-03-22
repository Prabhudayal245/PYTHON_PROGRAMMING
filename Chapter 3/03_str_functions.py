#Strings are immutable. which means that you cannot change them by running functions on them.
a="prabhu is a good boy"

length=len(a)  #it gives length of character in string
print(length)

end_string=a.endswith("boy") #if the string charcter is end with boy then  it returns True otherwise False.
print(end_string)

start_with=a.startswith("pra") #if the string charcter is start with pra then  it returns True otherwise False.
print(start_with)

capital=a.capitalize() #it capitalize the first character of string.
print(capital)

count_character=a.count("b") #counts the total number of occurrences of any character.
print(count_character)

find_word=a.find("good")  #this function find a word and returns the index of first occurence of that word in the string.
print(find_word)

replace_word=a.replace("good","bad") #this function replace the old word with new word in the entire string.
print(replace_word)

upper_string=a.upper() #it change string into upper case.
print(upper_string)

lower_string=a.lower() #it change string into lower case.
print(lower_string)

inde=a.index('is')
print(inde)