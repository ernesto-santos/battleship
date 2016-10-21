#!/usr/bin/python

import random
import sys

def print_no_newline(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()

board_xy_options = [1, 2, 3, 4, 6]

boats_size = [6, 4, 4, 3, 3, 3, 2, 2, 2]
boats_active = [False, False, False, False, False, False, False, False, False]
boats_hv_options = ["h", "v"]

board_x = random.choice(board_xy_options)
board_y = random.choice(board_xy_options)

print "Board x: " + str(board_x)
print "Board y: " + str(board_y)

board_bets = [["." for y in range(board_y)] for x in range(board_x)]
board_boats = [["." for y in range(board_y)] for x in range(board_x)]

#print board_bets

for y in range(board_y):
	print " " 
	for x in range(board_x):
		print_no_newline(board_bets[x][y] + " ")
		
is_boats_available = False

print " "
print " "
print "Boats:"

for boat in range(9):
	if ( boats_size[boat] <= board_x or boats_size[boat] <= board_y ):
		is_boats_available = True
		boats_active[boat] = True

	print str(boat) + ": size " + str(boats_size[boat]) + " is " + str(boats_active[boat])

if not is_boats_available:
	print "The board size doesn't allow to place any boat, sorry."
	sys.exit(0)
