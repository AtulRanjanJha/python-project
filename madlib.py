# madlib 

#-------------->>>>>> #string concatination (aka how to put the strings together)

# suppose we want to create a string that says "subscribe to"

youtuber = "atul jha " # some string variable

#a few ways to do that is following

print("subscribe to "+ youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")


adj= input("adjective: ")
verb1= input("verb1 : ")
verb2= input("verb2 : ")
madlib = f"computer programing is so {adj}. i like it so much that i {verb1}. it make me do various works like {verb2}."


print(madlib)