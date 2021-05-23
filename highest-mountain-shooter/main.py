import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    mountain_list = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountain_list.append(mountain_h)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    target = 0
    for i in range(len(mountain_list)):
        if mountain_list[i] > mountain_list[target]:
            target = i
    print(target)
    # The index of the mountain to fire on.
