class make_player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

open_dict = open("C:\python\shiritori\word.txt", "r").read()
dict = open_dict.split('\n')

from random import randint
from threading import Timer
last_letter = ''
difficult_letters = ['q','j','z','x','v','k','w','y','f']
play_word = ''
players = []
current_player_num = randint(1,2)
current_player = {}
deadline_minutes = 3
played_word = {}

def set_up(display_text, data_type):
    while True:
        variable = input('Enter ' + display_text + ': ')
        try:
            return data_type(variable)
            break
        except ValueError:
            print('Input Invalid! Please try again')
            continue



def welcome():
    global play_word, players
    global current_player_num, current_player, deadline_minutes
    num_of_players = 0

    input("""
    Hi! Welcome to Shiritori!
    In this game, players are required to enter a word which begins with the last letter of the previous word.
    Please enter the word in lower case.

    Computer will choose the first player and first letter.
    First, let's do some initial setup!
    Press ENTER to begin.
    """)

    #initial set-up
    print("""
    =====SETUP=====
    """)
    num_of_players = set_up('number of players', int)
    deadline_minutes = set_up('time allowed per guess in minutes', float)

    
    
    #random first word
    play_word = dict[randint(0,len(dict) - 1)]
    last_letter = play_word[-1]
    dict.remove(play_word)
    
    #get players name
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    for i in range(num_of_players):
        name = input('{} player please enter your name: '.format(ordinal(i+1)))
        player = make_player(name)
        players.append(player)
            
    #choose first player
    current_player_num = randint(0,num_of_players - 1)
    current_player = players[current_player_num]
    
    player_list = ' and '.join([p.name for p in players])

    start_game = input("""
    All set!
    {} will each have {} minutes to enter a new word.
    {}, you go first! When you are ready, press Enter to start!""".format(player_list, deadline_minutes, current_player.name))
    print('---------------')
    print('{}, your word is {}.'.format(current_player.name, play_word))

status = ''

def game_over(game_status):
    global status
    status = game_status
    print("""
    -----------------
    =====GAME OVER=====
    Final result:
    """)
    highest_score = 0
    winner = []

    for player in players:
        if player.score >= highest_score:
            winner.append(player.name)
            highest_score = player.score
        print("{}'s final score: {}".format(player.name, player.score))
    if len(winner) > 1:
        print('There is a tie between: ' + ' and '.join(winner))
    else: print('The winner is: '+winner[0])


def play():
    global last_letter, play_word
    global dict, played_word
    global current_player, current_player_num

    while True:
        last_letter = play_word[-1]
        #define timer
        t = Timer(deadline_minutes * 60,game_over,['over'])
        
        #dont need this when it is the first entry
        if bool(played_word) == True:
            print('-------------------')
            print("{}'s turn. You have {} minutes".format(current_player.name, deadline_minutes))
        
        t.start()
        play_word = input("Type in a word that starts with {} ".format(last_letter))

        #check validity of input
        while play_word[0] != last_letter or play_word not in dict:
            play_word = input('Word incorrect or have been played. Try again! ')
        
        #out of time
        t.cancel()
        if status == 'over':
            break
        #calculate score of current player
        if play_word[0] in difficult_letters:
            current_player.score += 2
        else: 
            current_player.score += 1
        current_player.score += len(play_word)
        played_word[play_word] = current_player.name
        dict.remove(play_word)

        #switch to next player
        current_player_num = (current_player_num + 1) % (len(players))
        current_player = players[current_player_num]

welcome()
play()