#!/usr/bin/env python
# coding: utf-8

# In[44]:


#AUTOMATIC ROCK, PAPER, SCISSORS
import random

global enemy_move
global player_move

player_score = 0
enemy_score = 0
ties = 0

def automatic_get_moves():
    player_move = random.randint(0,2)
    if player_move == 0:
        player_move = "rock"
    elif player_move == 1:
        player_move = "paper"
    elif player_move == 2:
        player_move = "scissors"
    
    enemy_move = random.randint(0,2)
    if enemy_move == 0:
        enemy_move = "rock"
    elif enemy_move == 1:
        enemy_move = "paper"
    elif enemy_move == 2:
        enemy_move = "scissors"
    return player_move, enemy_move
        

def automatic_compare_moves(player, enemy):
    global player_score
    global enemy_score
    global ties
    #print("yes I got here")
    #print(player, enemy)
    if player == enemy:
        ties +=1
        #print("It's a tie!")
    elif player == "rock" and enemy == "scissors":
            #print("You win!")
            player_score += 1
    elif player == "paper" and enemy == "rock":
            #print("You win!")
            player_score += 1
    elif player == "scissors" and enemy == "paper":
          #  print("You win!")
            player_score += 1        
    else:
        #print("You lose!")
        enemy_score += 1
    return player_score, enemy_score, ties


def automatic_main():
    plays = int(input("how many times would you like to play?"))
    for i in range(plays):
        moves = automatic_get_moves()
        #print(moves)
        player_move, enemy_move = moves[0], moves[1]
        scores = automatic_compare_moves(player_move, enemy_move)
        #print(scores)
        player_score, enemy_score, ties = scores[0], scores[1], scores[2]
        print("Score:",player_score,"-",enemy_score, "with",ties,"ties")

automatic_main()

#USER INPUT ROCK, PAPER, SCISSORS
import random
player_score = 0
enemy_score = 0
ties = 0

def user_get_moves():
    player_move = input("Pick your weapon ")
    #print(player_move)
    while player_move != "rock" and player_move != "paper" and player_move != "scissors":
        player_move = input("What? Try again please: ")
        if player_move == "rock" or player_move == "paper" or player_move == "scissors":
            break
        else:
            continue
    enemy_move = random.randint(0,2)
    if enemy_move == 0:
        enemy_move = "rock"
    elif enemy_move == 1:
        enemy_move = "paper"
    elif enemy_move == 2:
        enemy_move = "scissors"
    return player_move, enemy_move
        

def user_compare_moves(player, enemy):
    global player_score
    global enemy_score
    global ties
    if player == enemy:
        ties +=1
        print("It's a tie!")
    elif player == "rock" and enemy == "scissors":
            print("You win!")
            player_score += 1
    elif player == "paper" and enemy == "rock":
            print("You win!")
            player_score += 1
    elif player == "scissors" and enemy == "paper":
            print("You win!")
            player_score += 1        
    else:
        print("You lose!")
        enemy_score += 1
    return player_score, enemy_score, ties


def user_main():
    ties = 0
    start = input("Would you like to play?: ")
    while start != "no" and start != "yes":                
        start = input("What? Try again please: ")
        if start == "yes" or "no":
            break
        else:
            continue
    while start == "yes":
        moves = user_get_moves()
        #print(moves)
        player_move, enemy_move = moves[0], moves[1]
        scores = user_compare_moves(player_move, enemy_move)
        #print(scores)
        player_score, enemy_score, ties = scores[0], scores[1], scores[2]
        print("Score:",player_score,"-",enemy_score, "with",ties,"ties")
        start = input("Play again? ")
        if start == "no":
            print("Cya!")
            break
        elif start != "yes":
            while start != "no" and start != "yes":                
                start = input("What? Try again please: ")
                if start == "yes" or "no":
                    break
                else:
                    continue

#user_main()
# %%
