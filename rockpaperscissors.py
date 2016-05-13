import random
import sys

def show_moves(p_move, c_move):
	print "\tyou played %s" % p_move
	print "\tyour opponent played %s" % c_move

player_move = raw_input("your move, mister bond...\n > ")
computer_move = random.choice(["rock", "paper", "scissors"])

	
	if player_move == "quit" or "exit":
  	sys.exit()
	
	elif player_move == computer_move:
		show_moves(player_move, computer_move)
		print "\tIt's a tie."
		
	elif (player_move == "rock") and (computer_move == "paper"):
		show_moves(player_move, computer_move)
		print "\tpaper covers rock. you lose."
		computer_score = computer_score + 1
		
	elif (player_move == "rock") and (computer_move == "scissors"):
		show_moves(player_move, computer_move)
		print "\trock breaks scissors. you win."
		player_score = player_score + 1
		
	elif (player_move == "paper") and (computer_move == "rock"):
		show_moves(player_move, computer_move)
		print "\tpaper covers rock. you win,"
		player_score = player_score + 1
		
	elif (player_move == "paper") and (computer_move == "scissors"):
		print "\tscissors cut paper, you lose."
		computer_score = computer_score + 1
		
	elif (player_move == "scissors") and (computer_move == "rock"):
		show_moves(player_move, computer_move)
		print "\trock breaks scissors. you lose."
		computer_score = computer_score + 1
		
	elif (player_move == "scissors") and (computer_move == "paper"):
		show_moves(player_move, computer_move)
		print "\tscissors cut paper. you win."
		player_score = player_score + 1
	
	else:
		print "That is not a valid move. You lose a point."
		player_score = player_score - 1

	print "\tplayer score = %s \n\tcomputer_score = %s" % (player_score, computer_score)	
	
