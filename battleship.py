#!/usr/bin/python

import random
import sys
import os

def check_boat_board(_board_boats, _boat_size, _boat_x, _boat_y, _boat_hv, _board_x, _board_y):
	# Check Horizontal cases
	if ( _boat_hv == "h" ):
		# If the boat does not fit
		if ( _boat_x + _boat_size > _board_x - 1 ):
			return False

		# If the choosen positions are not available
		for z in range(_boat_size):
			if ( _board_boats[_boat_x + z][_boat_y] != "." ):
				return False
	# Check Vertical cases
	if ( _boat_hv == "v" ):
		# If the boat does not fit
		if ( _boat_y + _boat_size > _board_y - 1):
			return False

		# If the choosen positions are not available
		for z in range(_boat_size):
			if ( _board_boats[_boat_x][_boat_y + z] != "." ):
				return False

	# The boat is ok to the position
	return True

def print_board(_board_to_print, _x, _y):
	for b in range(_y):
		for a in range(_x):
			# Print each position
			print _board_to_print[a][b],

		print " "

def main():
	# Boars size options, for X and Y cordinates
	#board_xy_options = [1, 2, 3, 4, 6]
	board_xy_options = [10, 12, 14, 16, 18]

	# Ships sizes and hit counters
	boats_size = {"A":6, "B":4, "C":4, "D":3, "E":3, "F":3, "G":2, "H":2, "I":2}
	boats_hit_counter = boats_size

	# Orientation options
	boats_hv_options = ["h", "v"]

	# Choosing, randomicaly, the size of the board
	board_x = random.choice(board_xy_options)
	board_y = random.choice(board_xy_options)

	# Filling the shots board, with dots
	board_shots = [[] for _ in range(board_x)]

	for a in range(board_x):
		for b in range(board_y):
			board_shots[a].append(".")

	# Filling the board for boats placement with dots
        board_boats = [[] for _ in range(board_x)]

        for a in range(board_x):
		for b in range(board_y):
                	board_boats[a].append(".")

	# Placing the boats on the board
	for boat in boats_size.keys():
		boat_ok = False
		while( not boat_ok ):
			# Coordination Randomicaly generated 
			boat_x = random.randint(1, board_x) - 1
			boat_y = random.randint(1, board_y) - 1
			boat_hv = random.choice(boats_hv_options)

			# Call the function to validate the boat on the board
			boat_ok = check_boat_board(board_boats, boats_size[boat], boat_x, boat_y, boat_hv, board_x, board_y)

		# Placing, after validation
		if ( boat_hv == "h" ):
			for z in range(boats_size[boat]):
				board_boats[boat_x + z][boat_y] = boat

		if ( boat_hv == "v" ):
			for z in range(boats_size[boat]):
				board_boats[boat_x][boat_y + z] = boat

	# Loop for the shots
	while ( True ):

		# Printing the current scenario
		os.system('clear')
		print " "
		print "X size: " +  str(board_x)
		print "Y size: " +  str(board_y)

		# Please, uncomment the lines bellow, if you want to show the boats position
		#print " "
		#print "Boats board:"
		#print_board(board_boats, board_x, board_y)

		# Printing the shots board
		print " "
		print "Board:"
		print_board(board_shots, board_x, board_y)

		# Check if all boats are sunk
		all_sunk = True

		for boat in boats_hit_counter.keys():
			if ( boats_hit_counter[boat] > 0 ):
				all_sunk = False			

		# If so, the game is over
		if ( all_sunk ):
			print " "
			print "You win !!!!"
			sys.exit(0)

		# Getting the x coordinate
		print " "
		print "Please, provide the coordinates for your shot (Use 'q' to quit):"

		print "x: ",
		input_x = raw_input()

		if ( input_x == "q" ):
			sys.exit(0)
		
		# Getting the y coordinate
                print "y: ",
                input_y = raw_input()

                if ( input_y == "q" ):
                        sys.exit(0)

		# Converting the x coordinate on an integer value
		try:
			shot_x = int(input_x) - 1
		except:
			shot_x = 0

		# Converting the y coordinate on an integer value
		try:
			shot_y = int(input_y) - 1
		except:
			shot_y = 0

		# Validating if the shot is valid
		if ( shot_x >= 0 and shot_x < board_x and shot_y >= 0 and shot_y < board_y ):
			# Validating if the shot position is available
			if ( board_shots[shot_x][shot_y] != "." ):
				print " "
				print "Sorry, you already did this shot."
				print "Please, hit <enter>."
                        	aa = raw_input()
			else:
				# Validating if the player hit a boat
				if ( board_boats[shot_x][shot_y] != "." ):
					board_shots[shot_x][shot_y] = "x"

					boat = board_boats[shot_x][shot_y]

					boats_hit_counter[boat] -= 1

					# Validating if the boat is sunk
					if ( boats_hit_counter[boat] <= 0 ):
						boats_hit_counter[boat] = 0

						# If so, print the boat on the board
						for a in range(board_x):
							for b in range(board_y):
								if ( board_boats[a][b] == boat ):
									board_shots[a][b] = boat
				else:
					# Mark the position as "water"
					board_shots[shot_x][shot_y] = "~"
		else:
			print " "
			print "Sorry, the coordinates x,y are out of the board."
			print "Please, hit <enter>."
			aa = raw_input()

if __name__=="__main__":
	main()
