"""Simple game of rock paper scissors
   Author: Emanuel Ruiz
   Date: 7/19/23"""
import my_module
import random





choices = [my_module.rock, my_module.paper, my_module.scissors]

play = input("Would you like to play rock paper scissors: \n")

while (int(play) == 1):

    player_choice = input("Rock, paper, scissors. What's your choice: "
                        + " type 0 for rock, 1 for paper finally 2 for scissors: \n")

    while(int(player_choice)<0 or int(player_choice)>2):
        player_choice = input("Please enter a valid choice: "
                        + " type 0 for rock, 1 for paper finally 2 for scissors: \n")

    cc_num = random.randint(0,2)

    #computer_choice = random.choice(choices)
    computer_choice = choices[cc_num]
    player = choices[int(player_choice)]


    print("Player's Choice: \n")
    print(player)
    print("\n\nComputer chooses: ")
    print(computer_choice)

    if(int(player_choice) == cc_num):
        print("Tie Game")
    elif (player_choice == '0' and cc_num == 1):
        print("Sorry you lose")
    elif(player_choice == '1' and cc_num == 2):
        print("Sorry you lose")
    elif(player_choice == '2' and cc_num == 0):
        print("Sorry you lose")
    else:
        print("Congrats you win")

    play = input("Would you like to play rock paper scissors: \n")

