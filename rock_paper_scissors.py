import random

while True :  # for the end game asking to play again 
    choices = ['rock','paper','scissors' ]
    player = None
    computer = random.choice(choices)   




    while player not in choices :
        player =input('rock , paper or scissors ? :').lower()  # FOR INPUT YOUR CHOISE 


    if player ==computer :
        print("you : ", player)
        print("computer : ", computer)    # IN THE IF STATEMENT AND ELIF STATEMENTS  YOU CAN SEE DIFFERENT SITUATIONS 
        print("  tie  ")

    elif computer == 'rock' and player == 'paper' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you win ")
    elif computer == 'rock' and player == 'scissors' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you lose ")
    elif computer == 'paper' and player == 'scissors' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you win ")
    elif computer == 'paper' and player == 'rock' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you lose ")
    elif computer == 'scissors' and player == 'rock' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you win ")
    elif computer == 'scissors' and player == 'paper' :
        print("you : ", player)
        print("computer : ", computer)
        print(" you lose ")
    yes_no = ['yes', 'no']
    play_again = None
    while play_again not in yes_no : # FOR YES NO  
        play_again = input("do you want play again ? (yes /no)  ").lower()

    if play_again == 'no':
        print("by")
        break
    elif play_again =="yes" :
        continue 
