print("Welcome to the pizza hut!")
order=input(f"What type of pizza you would like.\n 1.Chicago style\n 2.Italian style\n 3.New York style\n")
order=int(order)
if order==1:
    print(f"you have ordered chicago style pizza.")
elif order==2:
    print ("you have ordered italian style pizza.")
elif order==3:
    print ("you have ordered new york style pizza.")
else:
    print("Invalid order.")

size= input(f"Enter the size of pizza you would like S,M,L: ")
size=str(size)
if size=="S":
    print(f"You want a small size {order} pizza ")
elif size=="M":
    print(f"You want a medium size {order} pizza " )
elif size=="L":
    Print(f"You want a large size {order} pizza ")
else:
    print("If you want a coustomized size please talk to manager.")

