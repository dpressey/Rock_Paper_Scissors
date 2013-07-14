import random 

print "Welcome to the rock_paper_scissors game"
print "I hope you enjoy, play you later!"

print

tie_counter = 0
win_counter = 0
loss_counter = 0
round_num = 1

weapon = ["rock", "paper", "scissor"]
rand_weapon = random.choice(weapon)

print "Round " + str(round_num)

p_choice = raw_input("choose rock(r), paper(p), or scissors(s): ")

if (p_choice == 'r' or p_choice == 'R') and rand_weapon == "rock":
	tie_counter += 1
	print "It's a tie"
elif (p_choice == 'r' or p_choice == 'R') and rand_weapon == "paper":
	loss_counter += 1
	print "You lost, computer chose " + str(rand_weapon)
elif (p_choice == 'r' or p_choice == 'R') and rand_weapon == "scissor":
	win_counter += 1
	print "You won, computer chose " + str(rand_weapon)
else:
        print 

	
	
	

	
	
