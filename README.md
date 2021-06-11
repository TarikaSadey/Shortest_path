## ASSIGNMENT 0 REPORT
### SUBMITTED BY TARIKA SADEY

### PART 1: NAVIGATION
* The problem poses that autonomous agents(like 'Pichu') represented as 'p' need to traverse through a house grid 
  consisting of N × M cells (N rows M columns) 
* Each cell of the house is marked with three symbols :
  p : represents the agent's current location
  X : represents a wall through which the agent cannot pass through
  . : represents open space over which the agent can fly
  @ : represents man(our) location which is the destination that the agent should reach.
* Our goal is to find the shortest path between the agent(p) and man(@). The agent can move one square at a time in four
  principled directions (path consisting of '.'), provide an output listing the shortest distance, and the path travelled 
  by the agent to reach the destination(@), return -1 as path length and empty string as path travelled if there is no
  path found.

#### SEARCH ABSTRACTION : 
the search abstraction used in solving this problem is defined below(We assume that there is always exactly one p and 
one @ in the map)
* State Space S : is the set of all possible solutions representing a path between agent(p) and destination(@).
* Initial State s0: Initial state is the house map of N rows and M columns with exactly one 'p' and one '@' along with 
  path variables '.' and walls 'X'.
* Successor States (Function) : Is the set of all possible next states to which the agent can travel from the current 
  position of agent(p) that is it checks for '.' and '@' to be a valid next move.
* Goal State : The shortest path between the agent(p) and man(@) with all the conditions followed.
* Cost Function : Here the algorithm is using BFS search technique which optimizes the solution and the cost function
  will be uniform as we have used the visiting node function. Time complexity will depend on the nodes travelled in the 
  path

#### OVERVIEW OF THE SOLUTION (route_pichu):
* The input house_map is passed as a parameter to a 'search' function which initially figures out the initial state of 
  the placement of agent 'p'(pichu_loc) and appends pichu's location along with initial empty string for the path 
  traversed and current distance travelled as '0' into a 'fringe'.
* I have used visited_m nodes to avoid already visited locations to avoid entering an infinite loop if any occur and to
  help give out a near optimal solution to the problem while avoiding the already traversed void coordinates.
* The control based loop while assigns the fringe to variables (curr_move, path_dir, curr_dist). Using the for loop we 
  traverse through all the moves(successor states) while passing the house-map,current coordinates of pichu and the path-
  direction travelled by pichu into the 'moves' method which validates whether the successor state is a valid index for 
  the pichu to move and returns the next location along with 'path_direction' in the form of the string which appends
  the principle direction the agent is moving (U-'Up', D-'Down', L-'Left', R-'Right') and returns to the 'search' function
* I have validated whether the next possible move(returned from moves) is not already visited and check whether the next 
  move consists the man(@) then we return the current distance travelled, and the path traversed. If not we insert the 
  location (row,column),path_direction and incremented current distance travelled into the fringe.
* This process is repeated until the move in the house map location returns the goal state.
* If there is no solution path found even after the house map is traversed we return -1 as distance travelled, and an 
  empty fringe as the path traversed.

#### SIMPLIFICATION/DESIGN MODIFICATIONS :
* I am passing an additional parameter to the 'moves' function 'path_dir' which will store the path traversed 
  ```
  fringe = [(pichu_loc, '', 0)]
  moves(house_map, *curr_move, path_dir)
  ```
  
* The moves function which validates the next move and concatenates the next move(successor path)
  ```
  moves1 = ((row + 1, col, path_dir + 'D'), (row - 1, col, path_dir + 'U'), (row, col - 1, path_dir + 'L'),
          (row, col + 1, path_dir + 'R'))
  ```
* I have converted the fringe as a stack to fringe as a queue implementing BFS as the search algorithm is complete and 
  will return an optimized solution.
  ```
  fringe.insert(0, (move[0:2], move[2], curr_dist + 1))
  ```
* Visited_m nodes list will ignore the already traversed nodes to avoid getting into an infinite loop and get a near 
  optimal solution.
  ```
  visited_m.append(curr_move)
        for move in moves(house_map, *curr_move, path_dir):
            if move[0:2] not in visited_m:
  ```
#### PROBLEMS FACED/OTHER FAILED APPROACHES:
* Took time to configure reducing the time factor of the solution.
* I have tried implementing the path travelled by concatenating the directions in the 'search' function for loop which 
  has returned the path travelled by the agent considering the void conditions too. Have tried various approaches but 
  couldn't solve this hence modified the 'moves' method which I found to be quite satisfactory.
  ```
  def search(house_map):
    #Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i] == "p"][0]
    fringe = [(pichu_loc, 0)]
    visited_m = []
    path_dir = ''
    while fringe: 
        (curr_move, curr_dist) = fringe.pop()
        visited_m.append(curr_move)
        for move in moves(house_map, *curr_move):
            if move not in visited_m:
                if move[0] == curr_move[0] + 1:
                    path_dir = path_dir + 'D'
                if move[0] == curr_move[0] - 1:
                    path_dir = path_dir + 'U'
                if move[1] == curr_move[1] + 1:
                    path_dir = path_dir + 'R'
                if move[1] == curr_move[1] - 1:
                    path_dir = path_dir + 'L'
                # print(move)
                if house_map[move[0]][move[1]] == "@":
                    return curr_dist + 1, path_dir  # return a dummy answer
                else:
                    fringe.insert(0, (move, curr_dist + 1))
    return -1, ''
  ```
------------------------------------------------------------------------------------------------------------------------
### PART 2: HIDE AND SEEK
* We will adopt k agents instead of one agent 'p' and try to position all the agents in the house map following the 
  below conditions.
1. The agents can be placed only on empty positions marked '.'.
2. No two agents can face each other i.e., they cannot be in the same row or same column.
3. If two agents are in the same row or the same column then they may be partitioned either by a wall 'X' or the man'@'

#### SEARCH ABSTRACTION : 
the search abstraction used in solving this problem is defined below(We assume that exactly one agent 'p' is already 
fixed in the input file and k agents to be placed includes the p agent already present in the input map)
* State Space S : is the set of all possible solutions(valid and invalid) maps with k agents placed on the map positioned 
  considering the conditions or ignoring them.
* Initial State s0: Initial state is the house map of N rows and M columns with exactly one 'p' along with path variables
  '@', '.' and walls 'X'.
* Successor States (Function) : Is the set of all possible next states to where agent p can be positioned keeping in mind 
  of the constraints that no two pichus can face each other if facing should be partitioned either by a wall 'X' or the 
  man'@' 
* Goal State : Map with k agents positioned following the constraints mentioned above.
* Cost Function : Is uniform or rather irrelevant as positioning of agents k in any other place will not affect the 
  solution as long as the constraints are followed.

#### OVERVIEW OF THE SOLUTION (arrange_pichus):
* Initial board and number of agents k are passed as parameters to the 'solve' function which assigns the initial board
  to a fringe.
* The control based loop will call the successor function with input parameter as the initial board appended to the fringe
  which will call the function to add a pichu to the board given the board traversed through its rows and columns.
* My add pichu method determines whether the successor position sent is viable or not based on the conditions and returns 
  a board with added agent p if viable otherwise will return the initial board.
* For every successor of s we check the goal state as whether the count of agents on the board is equal to the k parameter
  value passed otherwise will append the successor to the fringe and the process is repeated until the goal state is 
  reached and returns the output map with successful positioning of k agents otherwise would return 'None'.
  
#### CODE/DESIGN MODIFICATIONS :
* Visited_s will ignore the already traversed nodes hence reducing the time complexity and optimizing the solution.
  ```
        for s in successors(fringe.pop()):
            if s not in visited_s:
                if is_goal(s, k):
                    return s, True
                fringe.append(s)
                visited_s.append(s)
  ```
* My add_pichu method will consider all the adjoining rows and columns of the successor node where the agent can be 
  positioned and traverses the rows and columns to the edge length of the board to check whether it is a valid position
  for an agent to be placed and returns the board with pichu placed if valid otherwise will return the initial board passed.
  ```
    def add_pichu(board, row, col):
    for i in range(row + 1, len(board)):
        if board[i][col] == 'X' or board[i][col] == '@':
            break
        if board[i][col] == 'p':
            return board
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'X' or board[i][col] == '@':
            break
        if board[i][col] == 'p':
            return board
    for i in range(col + 1, len(board[0])):
        if board[row][i] == 'X' or board[row][i] == '@':
            break
        if board[row][i] == 'p':
            return board
    for i in range(col - 1, -1, -1):
        if board[row][i] == 'X' or board[row][i] == '@':
            break
        if board[row][i] == 'p':
            return board
    return board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]
  ```
  