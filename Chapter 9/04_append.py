# append:it add the content in existing file.
character=" \nyou are a good person"

f=open("myfile.txt","a")
f.write(character)
f.close()