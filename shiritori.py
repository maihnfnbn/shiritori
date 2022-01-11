class player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

open_dict = open("C:\python\shiritori\word.txt", "r").read()
dict = open_dict.split('\n')

from random import randint
from datetime import datetime, timedelta
last_letter = ''
difficult_letters = ['q','j','z','x','v','k','w','y','f']
play_word = ''
players = {}
current_player_num = randint(1,2)
current_player = {}
deadline = 0

def welcome():
    global play_word, players
    global deadline
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
    players = {1: player_1, 2: player_2}
    
    #choose first player
    current_player_num = randint(1,len(players))
    current_player = players[current_player_num]

    print('Hi {} and {}! Welcome to Shiritori!'.format(name_1, name_2))
    print('Players are required to say a word which begins with the last letter of the previous word.')
    print('Computer will choose the first player and first letter')
    print('{} go first, you have 3 minutes'.format(current_player.name))
    play_word = input('Your word is {}, type in a word that starts with {} '.format(play_word, last_letter))
    deadline = datetime.now() + timedelta(minutes=3)

def check_word(last_letter):
    global dict
    global current_player, current_player_num, play_word
    while play_word[0] != last_letter or play_word not in dict:
        play_word = input('Word incorrect or have been played. Try again! ')
    
    #calculate score of current player
    if play_word[0] in difficult_letters:
        current_player.score += 2
    else: 
        current_player.score += 1
    current_player.score += len(play_word)
    dict.remove(play_word)

    #switch to next player
    current_player_num = (current_player_num + 1) % len(players)
    current_player = players[current_player_num]

def play():
    global last_letter, play_word, deadline
    welcome()
    while datetime.now() < deadline:
        last_letter = play_word[-1]
        deadline = datetime.now() + timedelta(minutes=3)
        play_word = input("{}'s turn. Type in a word that starts with {} ".format(current_player.name, last_letter))
        check_word(last_letter)
    print('TIME OUT')
    print(players)

play()