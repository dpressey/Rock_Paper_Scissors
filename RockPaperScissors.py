#!/usr/bin/env python

import random 
import sys


print "======================Welcome to the rock_paper_scissors game================================="
print "========================I hope you enjoy, play you later!====================================="

print

tie_counter = 0
win_counter = 0
loss_counter = 0
round_num = 1

loop_var = True
player_pick_rock = 0
player_pick_paper = 0
player_pick_scissor = 0

weapon = ["r", "p", "s"]
comp_weapon = random.choice(weapon)

while loop_var == True:
    print "==============Round " + str(round_num) + "==============="
    print 
    for match in range(0,3):
        choice = raw_input("pick rock(r), paper(p), or scissor(s): ")
        weapon = choice.lower()
        if weapon == 'r' and comp_weapon == 'r':
            print "it's a tie"
            tie_counter += 1
            player_pick_rock += 1
        elif weapon == 'r' and comp_weapon == 'p':
            print "you lost!"
            loss_counter += 1
            player_pick_rock += 1
        elif weapon == 'r' and comp_weapon == 's':
            print "you won!"
            win_counter += 1
            player_pick_rock += 1
        elif weapon == 'p' and comp_weapon == 'r':
            print "you won!"
            win_counter += 1
            player_pick_paper += 1
        elif weapon == 'p' and comp_weapon == 'p':
            print "it's a tie"
            tie_counter += 1
            player_pick_paper += 1
        elif weapon == 'p' and comp_weapon == 's':
            print "you lost!"
            loss_counter += 1
            player_pick_paper += 1
        elif weapon == 's' and comp_weapon == 'r':
            print "you lost!"
            loss_counter += 1
            player_pick_scissor += 1
        elif weapon == 's' and comp_weapon == 'p':
            print "you won!" 
            win_counter += 1
            player_pick_scissor += 1
        elif weapon == 's' and comp_weapon == 's':
            print "it's a tie"
            tie_counter += 1
            player_pick_scissor += 1
        comp_weapon = random.choice(weapon)
            
            
    round_num += 1

    if (round_num >= 2 and (player_pick_paper > player_pick_rock) or (player_pick_paper > player_pick_scissor)):
        comp_weapon = 's'
    elif (round_num >= 2 and (player_pick_rock > player_pick_paper) or (player_pick_rock > player_pick_scissor)):
        comp_weapon = 'p'
    elif (round_num >= 2 and (player_pick_scissor > player_pick_rock) or (player_pick_scissor > player_pick_paper)):
        comp_weapon = 'r'
    
    print "Results so far: "
    print 
    print "you won: " + str(win_counter) + " times"
    print "you lost: " + str(loss_counter) + " times"
    print "you tied: " + str(tie_counter) + " times"
    print
    quit_choice = raw_input("want to quit(q)? ")
    quit = quit_choice.lower()
    if quit == 'q' or quit == 'y' or quit == 'yes':
        sys.exit()  


