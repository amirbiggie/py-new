# 2 ta  vorodi az user 
# 5 bar try va check mikone 
# 3 ta shart barqarar  kon 

import random

try:
    num1 = int(input("enter low number: \n"))
    num2 = int(input("enter high number: \n "))
except:
     print("please enter a valid number")    


r = random.randint(num1,num2)  

    

guess_try = 5

while guess_try > 0:
     
     try:
         user_guess = int(input("enter your guess: \n"))
        
        
         if r == user_guess:
              print("good job, your win")
              break;
         elif r > user_guess:
              print("your guess is lower than selectd number")
         else: 
              print("your guess is higher than selectd number")

         guess_try -=1      
    
     except:
         print("please enter a valid number")  

     
   
      