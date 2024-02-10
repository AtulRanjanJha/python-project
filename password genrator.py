import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [ 1 , 2 , 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['{', '}', '(', ')','[',']','.',',',':',';','+','-','*','/','&','|','<','>','=','~']

print("welcome to the password genrator.")
letter=int(input("Enter the number of alphabets you would like in your password:"))
number=int(input("Enter the number of number you would like in your password:"))
symbol=int(input("Enter the number of symbol you would like in your password:"))



random_letter= random.sample(alphabets,letter)
random_num= random.sample(numbers,number)
random_sym= random.sample(symbols,symbol)
password = random_letter + random_num + random_sym

def list_to_string(password):
    str1=""
    
    for ele in password:
        str1 += str(ele)
    return str1
    
print(list_to_string(password))
