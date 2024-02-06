import random

names= input(" Enter the name of the people seprated by a comma:  ")
name = names.split(",")
name_len= (len(name))
print(name)
print(name_len)
random_num = random.randint(0,name_len)
print(random_num)
random_name= name[random_num]
print(random_name)
print(f" Thank you for coming. {random_name} is the one choosen today to pay")