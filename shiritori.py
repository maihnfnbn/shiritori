class player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

open_dict = open("C:\python\shiritori\word.txt", "r").read()
dict = open_dict.split('\n')

from random import randint
last_letter = ''
difficult_letters = ['q','j','z','x','v','k','w','y','f']
play_word = ''
current_player = {}

def welcome():
    global play_word
    play_word = dict[randint(0,len(dict) - 1)]

    name_1 = input('First player please enter your name: ')
    name_2 = input('Second player please enter your name: ')
    player_1 = player(name_1)
    player_2 = player(name_2)
    players = {1: player_1, 2: player_2}

    print('Hi {} and {}! Welcome to Shiritori!'.format(name_1, name_2))
    print('Players are required to say a word which begins with the final kana of the previous word.')
    print('Computer will choose the first player and first letter')
    rand_current_player = randint(1,2)
    current_player = players[rand_current_player]
    play_word = input('{} go first, your word is {}'.format(current_player.name, play_word))

welcome()


def check_word(last_letter, word, player):
    global dict
    if word[0] == last_letter: #if first letter of input is last letter
        if word in dict:
            if word[0] in difficult_letters:
                player.score += 2
            else: player.score += 1
            player.score += len(word)
            dict.pop(word)
    else: word = input('word incorrect. Try again! ')

def play():
    next_player= {}
    welcome()
    last_letter = play_word[-1]
    check_word(last_letter, play_word, next_player)
