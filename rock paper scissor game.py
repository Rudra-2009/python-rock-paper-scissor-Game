#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     06/03/2024
# Copyright:   (c) HP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import time
while True :
    print("This is a Rock , Paper , Scissor game")
    print("")
    time.sleep(1)
    print("The game is very easy to play")
    print("")
    time.sleep(1)
    print("Rock - Paper --> Paper wins")
    time.sleep(1)
    print("Rock - Scissor --> Rock wins")
    time.sleep(1)
    print("Paper -  Scissor --> Scissor wins")
    print("")
    time.sleep(2)
    print("Enter the following number to play the game")
    print("")
    print("Rock --> 1")
    print("Paper --> 2")
    print("Scissor --> 3")
    print("")

    player_no = int(input("Please enter your number : "))
    computer_no = random.randint(1,3)

    if player_no == 1 and computer_no == 1 :
        print("You have chosen rock")
        print("Now its the computer's turn")
        print("the computer chooses Rock")
        time.sleep(3)
        print ("Its a DRAW")

    elif player_no == 1 and computer_no == 2 :
        print("You have chosen rock")
        print("Now its the computer's turn")
        print("the computer chooses Paper")
        time.sleep(3)
        print ("Computer Wins")

    elif player_no == 1 and computer_no == 3 :
        print("You have chosen rock")
        print("Now its the computer's turn")
        print("the computer chooses Scissor")
        time.sleep(3)
        print ("You Win!!")

    elif player_no == 2 and computer_no == 1 :
        print("You have chosen Paper")
        print("Now its the computer's turn")
        print("the computer chooses Rock")
        time.sleep(3)
        print ("You Win!!")

    elif player_no == 2 and computer_no == 2 :
        print("You have chosen paper")
        print("Now its the computer's turn")
        print("the computer chooses paper")
        time.sleep(3)
        print ("Its a DRAW")

    elif player_no == 2 and computer_no == 3 :
        print("You have chosen paper")
        print("Now its the computer's turn")
        print("the computer chooses scissor")
        time.sleep(3)
        print ("Computer Wins!!")

    elif player_no == 3 and computer_no == 1 :
       print("You have chosen scissor")
       print("Now its the computer's turn")
       print("the computer chooses rock")
       time.sleep(3)
       print ("Computer wins!!")

    elif player_no == 3 and computer_no == 2 :
       print("You have chosen scissor")
       print("Now its the computer's turn")
       print("the computer chooses paper")
       time.sleep(3)
       print ("You Win!!")

    elif player_no == 3 and computer_no == 3 :
       print("You have chosen scissor")
       print("Now its the computer's turn")
       print("the computer chooses scissor")
       time.sleep(3)
       print ("Its a DRAW")

    else :
       print("you might have entered something wrong")

    status = input("Do you want to play again? (yes/no) : ")

    if status != "yes" :
        print("thanks for playing!!")
        break









