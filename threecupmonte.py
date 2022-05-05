#Code in python for the game of 3 cup monte :

from random import shuffle
mylist=['','o','']   #storing the ball in the middle cup initially
def shuffle_list(mylist):
    shuffle(mylist)  #shuffling the cups
    return mylist

def player_guess():
    guess = int(input("pick a number from 0, 1 or 2 : ")) #player will guess that which cup contains the ball
    return guess

def check_guess(mylist,guess):
    if mylist[guess]=='o':   #check if the ball is stored inside the cup which player has guessed
        print('correct')
        print(mylist)
    else:
        print('wrong')
        print(mylist)
        default_calls()

def default_calls():
    shuffled_list = shuffle_list(mylist)
    user_choice = player_guess()
    check_guess(shuffled_list, user_choice)

default_calls()
