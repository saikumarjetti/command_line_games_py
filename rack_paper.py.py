import random

name = input("Enter your name: ")
print("Hello,",name)

#reading file
file = open("rating.txt","w+")
data = [i.split() for i in file.readlines()]
score = 0
flag = 0


#checking for user and store his score in score variable
for i in data:
	if name == i[0]:
		score = int(i[1])
		flag = 1


def bye():
	#adding new user data to the file 
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

l = ['paper', 'scissors', 'rock' ]
while 1:
	a = input()
	robot = random.choice(l)
	if a == "!exit":
		bye()
	elif a == "!rating":
		print("Your rating:",score)
	elif a == robot:
	    print(f"There is a draw ({a})")
	    score += 50
	elif (a == "paper"):
		if robot == "scissors":
			print("Sorry, but computer chose scissors")
		else:
			print(f"Well done. Computer chose {robot} and failed")
			score += 100
	elif (a == "scissors"):
		if robot == "rock":
			print("Sorry, but computer chose rock")
		else:
			print(f"Well done. Computer chose {robot} and failed")
			score += 100
	elif (a == "rock"):
		if robot == "paper":
			print("Sorry, but computer chose paper")
		else:
			print(f"Well done. Computer chose {robot} and failed")
			score += 100
	else:
		print("Invalid input")

