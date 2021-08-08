# Guess the Fruit name in the List using if/else and for loop


import random

Name = input("Enter the name : ")

list =[ 'BANANA','RICE','WHEAT','SUGAR','APPLE','LEMON','TOMATO']

Guess = random.choice(list)

   

count =0 
result=''
while True:
    
    fails =0
    
    for i in Guess:
        if i in result:
            print(i)
            
        else:
            print('*')
            fails +=1

    if fails==0:
        print("Congraluations!")
        break
    
    Alphabet = input("Guess any Alphabet  : ")
    result = result+Alphabet.upper()
    count+=1

    if(count>11):
        print('You reached the Limit')
        break

print(Guess,"this is the guessed word .")