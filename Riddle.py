q1_answers = ["London" , " London"]

player_name = input("What is your name? ")

player_dob = int(input("Welcome to Riddle City " + player_name + "\nWhich year were you born in? "))

age = 2020 - player_dob

print("You are " ,age, " years of age" )

print("Answer each question correctly, you have 3 attempts.")

if age >= 18:

	lives = 3
	
	while lives >= 1:

		x = input("What is the largest city in the United Kindgom? ")

		answer = x.capitalize()

		if answer in q1_answers:
			
			print("Correct answer")
			break

		else:

			lives = lives - 1

			if lives == 1:

				print("Wrong answer, careful now you have ONLY " + str(lives) + " life left!!!")
			
			elif lives == 0:

				print("GAME OVEREEEEERRRRRRRRRRR ^_^")

			else:

				print("Wrong answer, you have " + str(lives) + " lives left")
else:

	print("You need to be 18 or over to play this game.")

print("Thanks for playing")
