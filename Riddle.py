age = int(input("How old are you? "))

if age >= 18:

	lives = 3
	while lives >= 1:

		answer = input("What is the largest city in the United Kindgom? ")

		if answer == "London":
			
			print("Correct answer")
			break

		elif answer == " London":

			print("Correct answer")
			break

		elif answer == "london":

			print("Correct answer")
			break

		elif answer == " london":
			
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
