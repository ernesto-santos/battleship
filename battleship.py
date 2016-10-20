#!/usr/bin/python

import random
import sys

board_option = [1, 2, 3, 4, 6]

board_x = random.choice(board_option)
board_y = random.choice(board_option)

print "Board x: " + str(board_x) + "  -  Board y: " + str(board_y)

boats_sizes = []
boats_sizes.append(6)
boats_sizes.append(4)
boats_sizes.append(4)
boats_sizes.append(3)
boats_sizes.append(3)
boats_sizes.append(3)
boats_sizes.append(2)
boats_sizes.append(2)
boats_sizes.append(2)

print boats_sizes

is_boats_available = False

for boat in range(9):
	if ( boats_sizes(boat) <= board_x or boats_sizes(boat) <= board_y ):
		is_boats_available = True
		print "Boat: " + str(boat) + " is ok."
	else:
		print "Boat: " + str(boat) + " is not ok."

if not is_boats_available:
	print "The board size doesn't allow to place any boat, sorry."
	sys.exit(0)
		
