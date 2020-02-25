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
        state_list = [state[i:i + boarddims[0]] for i in range(0, len(state), boarddims[0])]

        # find empty tile coordinates
        found = False
        for x in range(len(state_list)):
            for y in range(len(state_list[x])):
                if state_list[x][y] is None:
                    empty = [x, y]
                    found = True
                    break
            if found:
                break

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
            if empty[dim] - 1 >= 0:
                offset[dim] = -1
                actions.append(list(offset))
            # append if we don't go off the bottom or right
            if empty[dim] + 1 < boarddims[dim]:
                offset[dim] = 1
                actions.append(list(offset))

        return actions

    def result(self, state, action):
        """result(state, action)- apply action to state and return new state"""
        n = self.puzzle.get_rows()
        state_list = [list(state[i:i + n]) for i in range(0, len(state), n)]

        r = c = 0
        found = False
        for x in range(len(state_list)):
            for y in range(len(state_list[x])):
                if state_list[x][y] is None:
                    r, c = x, y
                    found = True
                    break
            if found:
                break

        [delta_r, delta_c] = action

        # validate
        rprime = r + delta_r
        cprime = c + delta_c
        if rprime < 0 or cprime < 0 or \
                rprime >= n or cprime >= n:
            raise ValueError("Illegal move (%d,%d) from (%d,%d)" % (
                delta_r, delta_c, r, c))
        print("rprime: ", rprime, "r:", r, "cprime:", cprime, "c", c)

        # Apply move offset accordingly
        if delta_r != 0:
            # Move up or down
            state_list[r][c] = state_list[rprime][c]
            state_list[rprime][c] = None
        elif delta_c != 0:
            # Move left or right
            state_list[r][c] = state_list[r][cprime]
            state_list[r][cprime] = None

        new_state = [item for sublist in state_list
                     for item in sublist]
        # convert to tuple (hashable) and return
        return tuple(new_state)

    def goal_test(self, state):
        """goal_test(state) - Is state a goal?"""
        goal = state in self.puzzle.goals
        return goal

    def value(self, state):

        pass
