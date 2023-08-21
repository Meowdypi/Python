#Rock Paper Scissors game that keeps track of how many times the user or computer win or tie
import random

rps = ['r','p','s']
compwins, userwins, ties = 0

while True:
    score = "Computer wins = {} \nUser wins = {} \nTies = {}".format(compwins, userwins, ties)
    userinput = input("Rock (R), Paper (P), Scissors (s), or Quit Game (Q)?: ").lower()
    
    #Quit game
    if userinput == 'q':
        break
    
    #User enters incompatible input
    if userinput not in rps:
        print("Choose again: ")
        continue
    compinput = random.choice(rps)
    
    #User and Comp have the same choice:
    if  userinput == compinput:
        print("Both players selected " + compinput.upper() + ". Tie!")
        ties=+1
        print(score)
    
    #User chooses rock [0]:
    elif userinput == rps[0]: 
        if compinput == rps[1]:
            print("Paper beats Rock! Computer wins!")
            compwins+=1
            print(score)
        else:
            print("Rock beats Scissors! User wins!")
            userwins+=1
            print(score)
    
    #User chooses paper [1]:
    elif userinput == rps [1]:
        if compinput == rps[0]:
            print("Paper beats Rock! Computer wins!")
            compwins+=1
            print(score)
        else:
            print("Scissors beats Paper! User wins!")
            userwins+=1
            print(score)
    
    #User chooses scissors [2]:
    else:
        if compinput == rps[0]:
            print("Rock beats Scissors! Computer wins!")
            compwins+=1
            print(score)
        else:
            print("Scissors beats Paper! User wins")
            userwins+=1
            print(score)

print("Goodbye.")