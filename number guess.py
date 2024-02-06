import random

# we guess computers number 
#def guess(x):
#    random_number = random.randint(1,x)
#    guess=0
#    while guess != random_number:
#        guess =int(input(f'Guess a number between 1 and{x}: '))
#        if guess < random_number:
#            print('too low')
#        elif guess> random_number:
 #           print('too high')
#    print (f"congrats, your guess number {random_number} is right.")
# guess(10)



# computer guess our number 
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low,high)
        else: guess = low                                  # it could also be high b/c high=low
        feedback = input (f"is {guess} too high (h), too low(l), or correct(c)")
        if feedback=='h':
            high = guess -1
        elif feedback=='l':
            low=guess +1
    print(f"congrats, your {guess} is correct ")
computer_guess(10)