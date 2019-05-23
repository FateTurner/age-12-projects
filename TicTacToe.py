import time
from playsound import playsound

wins = 0

def userxposition(userxpos, userxlist, userslist, userx):
    userxpos = int(userxpos)
    if userxpos not in userxlist:
        if userxpos not in userslist:
            userxlist.append(userxpos)
            userslist.append(userxpos)
    if 1 and 2 and 3 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 4 and 5 and 6 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 7 and 8 and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 1 and 4 and 7 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 2 and 5 and 8 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 3 and 6 and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 1 and 5 and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1
    if 3 and 5 and 7 in userxlist:
        print("%s won! Congratulations!" % (userx))
        wins = 1

    return userxlist

"""print('Hello! Welcome to TrustedTicTacToe!')
time.sleep(1)
print('If you don\'t know how to play TicTacToe, please visit this page - https://www.wikihow.com/Play-Tic-Tac-Toe')

readyornot = input('If you\'re ready, please click enter, if you are not, don\'t click enter. \n')
print('Starting in...')
#playsound('E:\TrustedMercury\PYTHON\ProjectNeeds\Start.mp3')
time.sleep(0.5)
print('Loading TrustedTicTacToe Multiplayer...')"""
userx = input('Please enter player1\'s name\n')
time.sleep(0.25)
print('Welcome %s!' % userx.capitalize())
print('''
''')
usero = input('Please enter player2\'s name\n')
time.sleep(0.25)
print('Welcome %s!' % usero.capitalize())
"""time.sleep(1)
print("This is what the gameboard looks like, you'll need to use the numbers to choose your positions.")
time.sleep(2)
print('''
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     ''')"""
userxlist = []
userolist = []
userslist = []
condition = True

while wins != 1:
    userxpos = input('%s it\'s your chance! Your value is \'x\'! Choose a number: ' % userx.capitalize())
    userxlist = userxposition(userxpos, userxlist, userslist, userx)
    print('%s\'s values = %s' % (userx.capitalize(), userxlist))
    useropos = input('%s it\'s your chance! Your value is \'x\'! Choose a number: ' % usero.capitalize())
    userolist = userxposition(useropos, userolist, userslist, usero)
    print('%s\'s values = %s' % (usero.capitalize(), userolist))
