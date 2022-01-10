def welcome():
    player_1 = input('First player please enter your name: ')
    player_2 = input('Second player please enter your name: ')

    print('Hi {} and {}! Welcome to Shiritori!'.format(player_1, player_2))
    print('Players are required to say a word which begins with the final kana of the previous word.')
    print('Enter "OK" when you are ready to play! Computer will choose the first player and first letter')

welcome()

    