# 1.import logo, game_data
import art, game_data
import random
from replit import clear


# 2. Display the "Compare A: name, description, country"
	# 2b.Randomly pick data and game_data to compare a vs b
def random_question():
	"""Get data from random accounts"""
	return random.choice(game_data.data)

def format_data(account):
	name = account['name']
	description = account['description']
	country = account['country']
	follower = account['follower_count']
	return f"{name}, a {description}, from {country}, {follower}"

# 5. If the user gusses correct, continue playing 
			
			# 6. Have score keeper, print "You're right! Current score: .

# 4. Compare the follower count, who has more followers on insta
def compare(a_follower, b_follower):
	if a_follower > b_follower:
		# print(a_follower)
		return 'a'
	else:
		# print(b_follower)
		return 'b'



def game():
	print(art.logo)
	score = 0 #keeps the score when the user get is right
	is_game_over = False
	# assigns a random questions to choice_a
	# compare_a capture all the clues that needs to be printed out
	# put A outside the while loop b/c, this only need to print once when the game is started
	# after that A is placed by the B with replace() function

	choice_a = random_question()
	choice_b = random_question()

	while not is_game_over:
		#when the user gets it right b should become a
		choice_a = choice_b
		#choice_b change everytime user answers a correctly
		choice_b = random_question()
		
		if choice_a == choice_b:
			choice_b = random_question()
			
		print(f"Compare A: {format_data(choice_a)}")
		print(art.vs)
		print(f"Against B:  {format_data(choice_b)}")

		users_anwser = input("Who has more followers? Type 'A' or 'B': ").lower()
		choice_a_follower_count = choice_a['follower_count']
		choice_b_follower_count = choice_b['follower_count']
		correct = compare(choice_a_follower_count, choice_b_follower_count)
		
		clear()
		print(art.logo)
		if users_anwser == correct:
			score += 1
			print(f"You're right! Current score: {score}.")
			# choice_a = choice_b
			# print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}, {choice_a['follower_count']}")
		else:
			# 7. if the user gusses incorrectly, print "Sorry, that's wrong. Final score: "
			print(f"Sorry, that's wrong. Final score: {score}.")
			is_game_over = True

game()
