import random
import sys

valid_moves = ['r', 'p', 's']
move_name = {
  'r': 'rock',
  'p': 'paper', 
  's': 'scissors',
}

win_scen = {
  'rs': 'rock breaks scissors.',
 'pr': 'paper covers rock.',
 'sp': 'scissors cut paper',
 }
lose_scen = {
 'rp': 'paper covers rock.',
 'ps': 'scissors cut paper.', 
 'sr': 'rock breaks scissors.',
 }

player_score = 0
computer_score = 0

def show_moves(p1_move, p2_move):
  print "\tyou played %s" % move_name[p1_move]
  print "\tyour opponent played %s" % move_name[p2_move]

player_move = raw_input("your move, mister bond...\n > ")
computer_move = random.choice(valid_moves)

if player_move == "quit" or player_move == "exit":
  sys.exit()
elif player_move not in valid_moves:
  print "\tInvalid move! You lose a point."
  player_score -= 1
else:
  show_moves(player_move, computer_move)
  scen = player_move + computer_move

if player_move == computer_move:
  print "\tit's a tie. yay."
elif scen in win_scen:
  print win_scen[scen]
  print "\tyou win. yay."
  player_score += 1
elif scen in lose_scen:
  print lose_scen[scen]
  print "\tyou lose."
  player_score += 1
else:
  print "\tthat is not a valid move. You lose a point."
  player_score -= 1

print "\tplayer score = %s \n\tcomputer_score = %s" % (player_score, computer_score)  
  
