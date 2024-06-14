import random

user_input = int(input("Enter a number 0 for heads and 1 for tails: "))\
random_side = random.randint(0,1)
winner = random.randint(0,1)
toss = ["tails", "heads"]


if (random_side == user_input):
    print ("draw")
elif (random_side == winner) and (user_input != winner):
    print (f"computer got {toss[random_side]} and you got {toss[user_input]}. You lose.")
elif (random_side != winner) and (user_input == winner):
    print (f"computer got {toss[random_side]} and you got {toss[user_input]}. You win!")
