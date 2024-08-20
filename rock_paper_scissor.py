import random
Scissor = '''
 __      __
( _\    /_ )
 \ _\  /_ /
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | === |
    
   
   
   '''
paper= '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''
your_choice= input("What do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissor :\n ")
if your_choice == "0":
    print (Scissor)
elif your_choice == "1":
    print(paper)
elif your_choice == "2":
    print(rock)
    
    
computer_choice = random.randint(0,2)
print("Computer Choice:")
if computer_choice == 0:
    print (Scissor)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(rock)
    
    
    
if (computer_choice == 2) and (your_choice =="2"):
    print("Tie")
elif (computer_choice == 1) and (your_choice =="1"):
    print("Tie")
elif (computer_choice == 0) and (your_choice =="0"):
    print("Tie")
elif (computer_choice == 2) and (your_choice =="0"):
    print("You lose")
elif (computer_choice == 2) and (your_choice == "1"):
    print("You won")
elif (computer_choice == 1) and (your_choice =="2"):
    print("You lose")
elif (computer_choice == 1) and (your_choice == "0"):
    print("You won")
elif (computer_choice == 0) and (your_choice =="2"):
    print("You won")
elif (computer_choice == 0) and (your_choice == "1"):
    print("You Loose")

    
