from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem


class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """

    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance and any remaining arguments captured in **kwargs.
        """
        # Instantiate Tileboard
        self.puzzle = TileBoard(n, force_state)

        # Initialize parent class, Problem
        super().__init__(self.puzzle.state_tuple(), self.puzzle.goals, kwargs["g"], kwargs["h"])

        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs["keyname"], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

    def actions(self, state):
        """actions(state) - find a set of actions applicable to specified state"""
        
        actions = []
        # check row and column, no diagonal moves allowed
        boarddims = [self.puzzle.get_rows(), self.puzzle.get_cols()]
        for dim in [0, 1]:  # rows, then columns
            # Append offsets to the actions list, 
            # e.g. move left --> (-1,0)
            #      move down --> (0, 1)
            # Note that when we append to the list of actions,
            # we use list( ) to make a copy of the list, otherwise
            # we just get a pointer to it and modification of offset
            # will change copies in the list.
            offset = [0, 0]
            # add if we don't go off the top or left
            empty_tile_index = state.index(None)
            if empty_tile_index - 1 >= 0:
                offset[dim] = -1
                actions.append(list(offset))
            # append if we don't go off the bottom or right
            if empty_tile_index + 1 < boarddims[dim]:
                offset[dim] = 1
                actions.append(list(offset))

        return actions

    def result(self, state, action):
        """result(state, action)- apply action to state and return new state"""

        # Create a deep copy of the current board
        new_b = copy.deepcopy(self.puzzle)

        # Search for empty tile's coordinates (NOT index) using the deep copy
        found = False
        for x in range(len(new_b.board)):
            for y in range(len(new_b.board[x])):
                if new_b.board[x][y] is None:
                    empty_t = [x, y]
                    found = True
                    break
            if found:
                break
        
        # Apply move offset accordingly
        if offset[0] != 0:
            # Move up or down
            new_b.board[empty_t[0]][empty_t[1]] = new_b.board[empty_t[0] + offset[0]][empty_t[1]]
            new_b.board[empty_t[0] + offset[0]][empty_t[1]] = None
        elif offset[1] != 0:
            # Move left or right
            new_b.board[empty_t[0]][empty_t[1]] = new_b.board[empty_t[0]][empty_t[1] + offset[1]]
            new_b.board[empty_t[0]][empty_t[1] + offset[1]] = None

        # Return our shifted board to be assigned
        return new_b

        return state.move(action)

    def goal_test(self, state):
        """goal_test(state) - Is state a goal?"""

        goal = state in puzzle.goals
        return goal
