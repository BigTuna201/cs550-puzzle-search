"""
problemsearch - Functions for seaarching.
"""

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from explored import Explored


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
      (instance of basicsearch_lib02.representation.Problem or derived class),
      attempt to solve the problem.
      
      If debug is True, debugging information will be displayed.
      
      if verbose is True, the following information will be displayed:
      
      Number of moves to solution
      List of moves and resulting puzzle states
      Example:
      
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
      
      If no solution were found (not possible with the puzzles we
      are using), we would display:
      
      No solution found

      Returns a tuple (path, nodes_explored) where:
      path - list of actions to solve the problem or None if no solution was found
      nodes_explored - Number of nodes explored (dequeued from frontier)
      """

    # Create initial node as starting point and add to frontier
    initial_node = Node(problem, problem.puzzle.state_tuple())
    frontier = PriorityQueue()
    frontier.append(initial_node)

    # Create explored set and initialize variable to track nodes expanded
    explored = Explored()
    nodes_expanded = 0

    # Run while loop until graph search is complete
    done = found = False
    while not done:
        # Pop next node from frontier priority queue
        node = frontier.pop()
        if debug:
            print("Node:", node, "Action", node.action)  # View node for debugging purposes
        # Add current node state to explored set
        state = node.state
        explored.add(state)

        if problem.goal_test(state):
            # If goal found, exit while loop and return
            found = done = True
        else:
            # If goal not found, loop through possible actions depending on state
            for act in problem.actions(state):
                next_state = problem.result(state, act)
                next_node = node.child_node(act)
                # Check if next node after action is in frontier queue or explored set
                if next_node not in frontier:
                    if not explored.exists(next_state):
                        # If not, add to frontier and track the node as expanded
                        frontier.append(next_node)
                        nodes_expanded += 1

        done = len(frontier) <= -1  # Exit loop if frontier is empty

    if not found:
        print("No solution found.")
        # This should not happen, we check if board is solvable in Tileboard class
    else:
        if verbose:
            # If verbose, print puzzle states and actions in path to solution
            print("Solution in", len(node.solution()), "moves")
            print(problem.puzzle)

            # Loop through each action in path
            for i, act in enumerate(node.solution()):
                problem.puzzle = problem.puzzle.move(act)
                # Display move taken and resulting puzzle board
                print("Move", i + 1, "-", act)
                print(problem.puzzle)

        if debug:
            print("*" * 10, "Win")  # Divider for visualization during debugging

        return node.solution(), nodes_expanded
