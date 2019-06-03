import time
from playsound import playsound

wins = 0

def displayo(finalizednumber):
    if finalizednumber == 1:
        table1[0] = "O"
    if finalizednumber == 2:
        table2[0] = "O"
    if finalizednumber == 3:
        table3[0] = "O"
    if finalizednumber == 4:
        table4[0] = "O"
    if finalizednumber == 5:
        table5[0] = "O"
    if finalizednumber == 6:
        table6[0] = "O"
    if finalizednumber == 7:
        table7[0] = "O"
    if finalizednumber == 8:
        table8[0] = "O"
    if finalizednumber == 9:
        table9[0] = "O"
    print ([table1], "|", [table2], "|", [table3])
    print ([table4], "|", [table5], "|", [table6])
    print ([table7], "|", [table8], "|", [table9])

def displayx(finalizednumber):
    if finalizednumber == 1:
        table1[0] = "X"
    if finalizednumber == 2:
        table2[0] = "X"
    if finalizednumber == 3:
        table3[0] = "X"
    if finalizednumber == 4:
        table4[0] = "X"
    if finalizednumber == 5:
        table5[0] = "X"
    if finalizednumber == 6:
        table6[0] = "X"
    if finalizednumber == 7:
        table7[0] = "X"
    if finalizednumber == 8:
        table8[0] = "X"
    if finalizednumber == 9:
        table9[0] = "X"
    print ([table1], "|", [table2], "|", [table3])
    print ([table4], "|", [table5], "|", [table6])
    print ([table7], "|", [table8], "|", [table9])


def userxposition(userxpos, userxlist, userslist, userx):
    end = 0
    userxpos = int(userxpos)
    if userxpos not in userxlist:
        if userxpos not in userslist:
            userxlist.append(userxpos)
            userslist.append(userxpos)
    if 1 in userxlist and 2 in userxlist and 3 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 4 in userxlist and 5 in userxlist and 6 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 7 in userxlist and 8 in userxlist and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 1 in userxlist and 4 in userxlist and 7 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 2 in userxlist and 5 in userxlist and 8 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 3 in userxlist and 6 in userxlist and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 1 in userxlist and 5 in userxlist and 9 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    if 3 in userxlist and 5 in userxlist and 7 in userxlist:
        print("%s won! Congratulations!" % (userx))
        end = 1
    return (userxlist, end)

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

table1 = ["1"]
table2 = ["2"]
table3 = ["3"]
table4 = ["4"]
table5 = ["5"]
table6 = ["6"]
table7 = ["7"]
table8 = ["8"]
table9 = ["9"]


while wins != 1:
    if wins != 1:
        userxpos = input('%s it\'s your chance! Your value is \'x\'! Choose a number: ' % userx.capitalize())
        userxlist, end = userxposition(userxpos, userxlist, userslist, userx)
        finalizedxpos = userxlist[len(userxlist)-1]
        displayx(finalizedxpos)
        wins = end
        print(wins)
        print('%s\'s values = %s' % (userx.capitalize(), userxlist))
        print(userslist)
    if wins != 1:
        useropos = input('%s it\'s your chance! Your value is \'o\'! Choose a number: ' % usero.capitalize())
        userolist, end = userxposition(useropos, userolist, userslist, usero)
        finalizedopos = userolist[len(userolist) - 1]
        displayo(finalizedopos)
        wins = end
        print(wins)
        print('%s\'s values = %s' % (usero.capitalize(), userolist))
