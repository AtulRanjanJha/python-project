name1= input("Enter your name: ")
name2= input("Enter their name: ")

combined_name = str (name1 + name2)
lower_combined_name = combined_name.lower()


t= lower_combined_name.count("t")
r= lower_combined_name.count("r")
u= lower_combined_name.count("u")
e= lower_combined_name.count("e")

true = t + r + u + e



l= lower_combined_name.count("l")
o= lower_combined_name.count("o")
v= lower_combined_name.count("v")
e= lower_combined_name.count("e")

love = l + o + v + e

True_Love= true +love
print(f"Your True Love Score is {True_Love}")