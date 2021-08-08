# Number guessing game
# A and B were user selected a range and both are integers.
import math
import random
A = int(input("Enter the value for the range starting : "))
B = int(input("Enter the value for the range Ending  : "))

count = 0

Number = random.randint(A,B) # to get random number between the range
Max_step = math.floor(math.log((B-A+1),2)) # Formula used to get, minimum number number of guesses
# print(Max_step)
# print(Number)
while True:

    
    if (Max_step>count):
        user_number = int(input("Enter the number you guessed : "))

        if(user_number > Number):
            print("Try Again! You guessed high!")
            
            count+=1
            
        elif(user_number<Number):
            print("Try Again! You guessed low")
            count+=1
            
        else:
            print("Congratulations!")
            print("You gave gussed the number in ",count," guesses.")
            print("Thanks for playing the game!!!")
            break
    else:
        print("The random slected number is ",Number)
        print("You have reached maximum gusses...")
        break