import time
import random

def number_to_list(number_value) :
	number_value = int(number_value)
	list_value = []
	while (number_value > 0):
		list_value.append(number_value % 10)
		number_value = int(number_value / 10)
	list_value.reverse()
	return list_value

def check_repeats(list):
	for i in list:
		if list.count(i) >= 2:
			print("Please don't repeat any numbers.")
			return True
	return False

def isNumberOK(number):
	number_list = number_to_list(number)
	if check_repeats(number_list):
			return False
	if len(number_list) != 4 :
			return False
	return True

def find_miss(hidden, guessed):
	no_miss = 0
	hidden_list = number_to_list(hidden)
	guessed_list = number_to_list(guessed)
	for guessed_no in guessed_list:
		if guessed_no in hidden_list:
			no_miss = no_miss + 1
	return no_miss


def find_hit(o, g):
	no_hit = 0
	o_list = number_to_list(o)
	g_list = number_to_list(g)
	for i in range(len(g_list)):
		if o_list[i] == g_list[i]:
			no_hit = no_hit + 1
	return no_hit




print('''Welcome to HIT OR MISS V1.0 by TrustedMercury!''')
time.sleep(2)
print('''Presenting Tutorial and then starting...''')
time.sleep(5)
print('''You must enter a 4-digit-number.
The computer will automatically generate a 4-digit-number too.
After that, you must try guessing the computer's secret number.
If you guess a digit of the computer's number, and if it's in the same position as the computer's number, it'll print HIT,
or the number of digits that were a HIT. If you get a right digit but in a wrong positon,
it'll print MISS. If you get nothing it'll just continue.
This code isn't bug proof, so there still might be some errors. And yeah, you mustn't repeat any digit
or have any 0s in your secret number''')
print("Redirected to start. Starting...")
time.sleep(3)

no_hit = 0
no_miss = 0

hiddenuser = input("Enter your secret four digit number: ")
hiddenuser_list = number_to_list(hiddenuser)

time.sleep(1)

while isNumberOK(hiddenuser) == False:
	hiddenuser = input("Enter your secret four digit number: ")
	hiddenuser_list = number_to_list(hiddenuser)

hiddencomp = random.randint(1000,10000)

list_hiddencomp = []
list_hiddencomp = number_to_list(hiddencomp)

for i in list_hiddencomp:
	if list_hiddencomp.count(i) >= 2:
		hiddencomp = random.randint(1000,10000)
		list_hiddencomp = number_to_list(hiddencomp)

while no_hit <= 4:
	userguess = input("Your chance! Try guessing the computer's hidden number: ")
	userguess = int(userguess)

	list_userguess = number_to_list(userguess)

	while isNumberOK(userguess) == False:
		time.sleep(1)
		userguess = input("Your chance! Try guessing the computer's hidden number: ")
		userguess_list = number_to_list(userguess)
	no_miss = find_miss(str(hiddencomp),str(userguess))
	no_hit = find_hit(str(hiddencomp), str(userguess))
	no_miss = no_miss - no_hit
	print('''Number of Misses = %s
Number of Hits = %s''' % (no_miss, no_hit))
	if no_hit == 4:
		print("Congratulations! You won the game!")
		break

