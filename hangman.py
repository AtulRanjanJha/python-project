import random
word_list = [ "ardvark", "baboon", "camel" ]
chosen_word = random.choice(word_list)

guess = input("enter the letter of your guess? \n").lower()
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[postion]= letter
        
print(display)
    
