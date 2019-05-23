import time
from playsound import playsound

def userxposition(userxpos):
    userxpos = int(userxpos)
    if userxpos == 1:
        nowboard = '''
             |     |     
          x  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 2:
        nowboard = '''
             |     |     
          1  |  x  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 3:
        nowboard = '''
             |     |     
          1  |  2  |  x  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 4:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          x  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 5:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  x  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 6:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  x  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 7:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          x  |  8  |  9  
             |     |     '''
    if userxpos == 8:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    if userxpos == 9:
        nowboard = '''
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |     '''
    return nowboard


print('Hello! Welcome to TrustedTicTacToe!')
time.sleep(1)
print('If you don\'t know how to play TicTacToe, please visit this page - https://www.wikihow.com/Play-Tic-Tac-Toe')

readyornot = input('If you\'re ready, please click enter, if you are not, don\'t click enter. \n')
print('Starting in...')
#playsound('E:\TrustedMercury\PYTHON\ProjectNeeds\Start.mp3')
time.sleep(0.5)
print('Loading TrustedTicTacToe Multiplayer...')
userx = input('Please enter player1\'s name\n')
time.sleep(0.25)
print('Welcome %s!' % userx.capitalize())
print('''
''')
usero = input('Please enter player2\'s name\n')
time.sleep(0.25)
print('Welcome %s!' % usero.capitalize())
time.sleep(1)
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
     |     |     ''')
userxpos = input('%s it\'s your chance! Your value is \'x\'! Choose a number: ' % userx.capitalize())
nowboard = userxposition(userxpos)
time.sleep(1)
print(nowboard)






