print("Welcome to the game")
playing = input("Do you want to play? ")

if playing !="yes":
    quit()

print("Then let's play")
score = 0

answer = input("what does cpu stands for? ")
print(answer) 
if answer.lower()=="central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect.")

answer = input("WHat does gpu stands for ? ")
if answer.lower()=="Graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect.")

answer = input("what does RAM stands for? ")
if answer.lower=="Random Acess memory":
    print("correct")
    score+=1
else:
    print("incorrect.")

answer = input("what does Psu stands for? ")
if answer.lower()=="Power Supply Unit":
    print("correct")
    score+=1
else:
    print("incorrect.")


print(f"THANK YOU FOR PLAYING. YOUR HAVE SCORED {score} OR {score/4*100}%.")

