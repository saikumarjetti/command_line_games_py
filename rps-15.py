import random

print("Welcome to advance rock-paper-scissors(RPS-15) game")
print("if you dont know how to play visite this link: www.umop.com/rps15.htm")

#All possible moves
moves =['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']

name = input("Enter your name: ")
print("Hello,",name)

print("Enter your list of moves which are seperated by comma(like : paper,rock,fire...... ) ")
print(f"list of all possible moves\n{moves}")

flist = [i for i in input().split(",")]
print("Okay, let's start")
if len(flist) < 3:
	flist = ['paper', 'scissors', 'rock' ]

#reading file if not exit then create ..
try:
	file = open("rating.txt","r+")
except:
	file = open("rating.txt","w+")

data = [i.split() for i in file.readlines()]
score = 0
flag = 0


#checking for user name and if found store his score in score variable (score)
for i in data:
	if name == i[0]:
		score = int(i[1])
		flag = 1


def bye():
	if not flag:
		data.append([name,score])
	else:
		for i in data:
			if name == i[0]:
				i[1] = f"{score}"
	#converting data(list) to string so we can store in file  
	finalData = ""
	for k in data:
		finalData += f"{k[0]} {k[1]}\n"
	#writing the data to file 
	file.seek(0)
	file.write(finalData)
	file.flush()
	print("Bye!")
	file.close()
	exit(0)


#cheat sheet to check 

main = {'rock': ['fire', 'scissors', 'snake', 'human', 'wolf', 'sponge', 'tree'], 
		'fire': ['scissors', 'paper', 'snake', 'human', 'tree', 'wolf', 'sponge'], 
		'scissors': ['air', 'tree', 'paper', 'snake', 'human', 'wolf', 'sponge'], 
		'snake': ['human', 'wolf', 'sponge', 'tree', 'paper', 'air', 'water'], 
		'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'], 
		'tree': ['wolf', 'dragon', 'sponge', 'paper', 'air', 'water', 'devil'], 
		'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'lightning'], 
		'sponge': ['paper', 'air', 'water', 'devil', 'dragon', 'gun', 'lightning'], 
		'paper': ['air', 'rock', 'water', 'devil', 'dragon', 'gun', 'lightning'], 
		'air': ['fire', 'rock', 'water', 'devil', 'gun', 'dragon', 'lightning'], 
		'water': ['devil', 'dragon', 'rock', 'fire', 'scissors', 'gun', 'lightning'], 
		'dragon': ['devil', 'lightning', 'fire', 'rock', 'scissors', 'gun', 'snake'], 
		'devil': ['rock', 'fire', 'scissors', 'gun', 'lightning', 'human'], 
		'lightning': ['gun', 'scissors', 'rock', 'tree', 'fire', 'snake', 'human'], 
		'gun': ['rock', 'tree', 'scissors', 'snake', 'human', 'wolf']}



while 1:
	a = input()
	robot = random.choice(flist)
	if a == "!exit":
		bye()
	elif a == "!rating":
		print("Your rating:",score)
	#elif robot == a:
	#	print(f"There is a draw ({robot})")
	#	score += 50
	elif a in moves:
		if robot == a:
			print(f"There is a draw ({robot})")
			score += 50
		elif robot in main[a]:
			print(f"Well done. Computer chose {robot} and failed")
			score += 100
		else:
			print(f"Sorry, but computer chose {robot}")
	elif a not in flist:
		print("Invalid input")
