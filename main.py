# PROJECT 1: SNAKE, WATER, GUN GAME
'''
1 for snake
-1 for  water 
0 for gun 

'''
import random 
computer = random.randint(-1, 1)
key = ["water", "gun", "snake"]
you = key.index(input("your choice: ")) - 1
print(f"You choose {key[you + 1]} \n Computer chose {key[computer + 1]}")



if computer == you:
    print ("Draw")

else:

    if(computer==-1 and you == 1):
        print("You win")    
    elif (computer==-1 and you==0):
        print("You Win")
    elif (computer==0 and you==-1):
        print("You Win")
    elif (computer==1 and you==0):
        print("You Win")
    else:
        print("You loose")

         # We can replace the ladder by the following logic ..   


    #  if computer - you == -1 or computer - you == 2 :
    #      print("You win ")
    #  else:
    #      print("You loose")   
