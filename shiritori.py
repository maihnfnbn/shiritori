class player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

open_dict = open("C:\python\shiritori\word.txt", "r").read()
dict = open_dict.split('\n')

from random import randint
from datetime import datetime, timedelta
from threading import Timer
last_letter = ''
difficult_letters = ['q','j','z','x','v','k','w','y','f']
play_word = ''
players = []
current_player_num = randint(1,2)
current_player = {}
deadline_minutes = 3
played_word = {}

def welcome():
    global play_word, players
    global current_player_num, current_player
    
    #random first word
    play_word = dict[randint(0,len(dict) - 1)]
    last_letter = play_word[-1]
    dict.remove(play_word)
    
    #get players name
    name_1 = input('First player please enter your name: ')
    name_2 = input('Second player please enter your name: ')
    player_1 = player(name_1)
    player_2 = player(name_2)
    players = [player_1, player_2]
    
    #choose first player
    current_player_num = randint(0,len(players)-1)
    current_player = players[current_player_num]

    print('Hi {} and {}! Welcome to Shiritori!'.format(name_1, name_2))
    print('Players are required to say a word which begins with the last letter of the previous word.')
    print('Computer will choose the first player and first letter')
    start_game = input('Press Enter to start! \n')
    print('---------------')
    print('{} go first, your word is {}.'.format(current_player.name, play_word))


status = ''

def game_over():
    global status
    if play_word not in dict:
        status = 'over'
        return'Game Over'
    return '----------'


def play():
    global last_letter, play_word
    global dict, played_word
    global current_player, current_player_num
    welcome()

    while True:
        last_letter = play_word[-1]
        #define timer
        t = Timer(deadline_minutes * 3,print,[game_over()])
        
        #dont need this when it is the first entry
        if bool(played_word) == True:
            print('-------------------')
            print("{}'s turn. You have {} minutes".format(current_player.name, deadline_minutes))
        
        t.start()
        play_word = input("Type in a word that starts with {} ".format(last_letter))

        #check validity of input
        while play_word[0] != last_letter or play_word not in dict:
            play_word = input('Word incorrect or have been played. Try again! ')
        #calculate score of current player
        if play_word[0] in difficult_letters:
            current_player.score += 2
        else: 
            current_player.score += 1
        current_player.score += len(play_word)
        played_word[play_word] = current_player.name
        dict.remove(play_word)
        print("{}'s current score: {}".format(current_player.name, current_player.score))

        #switch to next player
        current_player_num = (current_player_num + 1) % (len(players))
        current_player = players[current_player_num]
        print(status)
        t.cancel()
        print(status)
play()