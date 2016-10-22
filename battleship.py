#!/usr/bin/python

import random
import sys

def check_boat_board(_board_boats, _boat_size, _boat_x, _boat_y, _boat_hv, _board_x, _board_y):
	#print_board(_board_boats, _board_x, _board_y)

	#print "_boat_size : "+ str(_boat_size)
	#print "_boat_x : " + str(_boat_x)
	#print "_boat_y : " + str(_boat_y)
	#print "_boat_hv : " + str(_boat_hv)
	#print "_board_x : " + str(_board_x)
	#print "_board_y : " + str(_board_y)

	if ( _boat_hv == "h" ):
		if ( _boat_x + _boat_size > _board_x - 1 ):
			return False

		for z in range(_boat_size):
			#print "z: " + str(z)
			if ( _board_boats[_boat_x + z][_boat_y] != "." ):
				return False
	if ( _boat_hv == "v" ):
		if ( _boat_y + _boat_size > _board_y - 1):
			return False

		for z in range(_boat_size):
			#print "z: " + str(z)
			if ( _board_boats[_boat_x][_boat_y + z] != "." ):
				return False

	return True

def print_board(_board_to_print, _x, _y):
	for b in range(_y):
		for a in range(_x):
			print _board_to_print[a][b],

		print " "

def main():
	# Boars size options, for X and Y cordinates
	#board_xy_options = [1, 2, 3, 4, 6]
	board_xy_options = [10, 12, 14, 16, 18]

	# Ships by their:
	# Sizes
	boats_size = {"A":6, "B":4, "C":4, "D":3, "E":3, "F":3, "G":2, "H":2, "I":2}
	# Status 
	boats_active = {"A":False, "B":False, "C":False, "D":False, "E":False, "F":False, "G":False, "H":False, "I":False}

	# Orientation options
	boats_hv_options = ["h", "v"]

	# Choosing, randomicaly, the size of the board
	board_x = random.choice(board_xy_options)
	board_y = random.choice(board_xy_options)

	print "Board x , y : %d , %d" % (board_x, board_y)
	print " "

	# Filling the board for bets with dots
	board_bets = [[] for _ in range(board_x)]

	for a in range(board_x):
		for b in range(board_y):
			board_bets[a].append(".")

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
			#print "Validating boat: " + boat 
			boat_ok = check_boat_board(board_boats, boats_size[boat], boat_x, boat_y, boat_hv, board_x, board_y)

		# Placing, after validation
		#print "Placing the boat: " + boat

		if ( boat_hv == "h" ):
			for z in range(boats_size[boat]):
				board_boats[boat_x + z][boat_y] = boat

		if ( boat_hv == "v" ):
			for z in range(boats_size[boat]):
				board_boats[boat_x][boat_y + z] = boat

	# Printing the boats board
	print " "
        print "Boats board:"
	print_board(board_boats, board_x, board_y)

	# Printing the bets board
	print " "
	print "Bets board:"
	print_board(board_bets, board_x, board_y)


	# Validating the boats
	#is_boats_available = False

	#print " "
	#print "Boats:"

	#for boat in boats_size.keys():
	#	if ( boats_size[boat] <= board_x or boats_size[boat] <= board_y ):
	#		is_boats_available = True
	#		boats_active[boat] = True

	#	print str(boat) + ": size " + str(boats_size[boat]) + " is " + str(boats_active[boat])

	#if not is_boats_available:
	#	print "The board size doesn't allow to place any boat, sorry."
	#	sys.exit(0)


if __name__=="__main__":
	main()
