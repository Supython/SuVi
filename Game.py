import random
input1= input("Enter player 1 name ")
input2= input("Enter player 2 name ")
score1S=0
score2S=0
while score1S or score2S<10:
	S1= random.randint(1,6)
	S2= random.randint(1,6)
	print("Value of {0} : {1}" . format(input1,S1))
	print("Value of {0} : {1}" . format(input2,S2))
	score1S=score1S+S1
	score2S=score2S+S2
	if (score1S or score2S) >20:
		break;
	print("Total score of {0} : {1}".format(input1,score1S))
	print("Total score of {0} : {1}".format(input2,score2S))
if score1S>score2S:
	print("{0} is the winner".format(input1))
elif score1s<score2S:
	print("{0} is the winner". format(input2))
else:
	print('Score z tie! Do play again')
	
