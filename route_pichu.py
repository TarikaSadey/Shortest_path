#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : TARIKA SADEY(tsadey)
#
# Based on skeleton code provided in CSCI B551, Spring 2021.

import sys


# import json
# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
# Find the possible moves from position (row, col, direction_of_the_path_defined in {D,U,L,R})
def moves(map1, row, col, path_dir):
    # path_dir concatenates the direction the agent is moving
    moves1 = ((row + 1, col, path_dir + 'D'), (row - 1, col, path_dir + 'U'), (row, col - 1, path_dir + 'L'),
              (row, col + 1, path_dir + 'R'))
    # Return only moves that are within the board and legal (i.e. go through open space ".")
    return [move for move in moves1 if valid_index(move, len(map1), len(map1[0])) and (map1[move[0]][move[1]] in ".@")]


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
    # Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "p"][0]
    fringe = [(pichu_loc, '', 0)]
    # visited_m used to remove already visited states to avoid the path going into infinite loop and to optimize the solution
    visited_m = []
    while fringe:
        (curr_move, path_dir, curr_dist) = fringe.pop()
        visited_m.append(curr_move)
        for move in moves(house_map, *curr_move, path_dir):
            if move[0:2] not in visited_m:
                # print(move)
                if house_map[move[0]][move[1]] == "@":
                    # return number of moves required to navigate from start to finish and the path traversed
                    return curr_dist + 1, move[2]
                else:
                    # converting stack to a queue
                    fringe.insert(0, (move[0:2], move[2], curr_dist + 1))
    return -1, ''


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    print("Routing in this board:\n" + printable_board(house_map) + "\n")
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + str(solution[1]))
