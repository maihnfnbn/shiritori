class player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

open_dict = open("C:\python\shiritori\word.txt", "r").read()
dict = open_dict.split('\n')

def welcome():
    name_1 = input('First player please enter your name: ')
    name_2 = input('Second player please enter your name: ')
    player_1 = player(name_1)
    player_2 = player(name_2)

    print('Hi {} and {}! Welcome to Shiritori!'.format(player_1.name, player_2.name))
    print('Players are required to say a word which begins with the final kana of the previous word.')
    print('Enter "OK" when you are ready to play! Computer will choose the first player and first letter')

import os
def check_word(last_letter, word, player):
    if word[0] == last_letter:
        if word in dict:
            print('correct')
    else: print('not correct')
