"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is at the bottom right, e.g.:
        123
        456
        78
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math


# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value

# TODO: Implement classes BreadthFirst, DepthFirst, and Manhattan. These are classes that provide implementations for
#  the cost to node (g) and cost from node to goal heuristic (h) functions. Note g and h are class methods (see
#  details on class methods in the comments of the provided code) and that when you pass them to the NPuzzle
#  constructor, you need to pass the function handles to the constructor rather than invoking the function.
#  Concretely, if you wanted to pass BreadthFirst’s function handle for g to NPuzzle, you would call NPuzzle(
#  num_tiles, g=BreadthFirst.g, ... ). NPuzzle’s parent class stores g in a publicly accessible instance variable and
#  other code (e.g. the Node class discussed below) will invoke the functions to evaluate search nodes. Note that we
#  defined DepthFirst’s g as a constant and h as the negative depth. The structure of the Node implementation expects
#  h to be called with a single argument: state. As the depth is captured in the Node, and not the state, reverse the
#  roles of g and h when implementing DepthFirst. The depth can be accessed from the g function which expects a
#  parent, action, and the search node itself.

class BreadthFirst:
    """BreadthFirst - breadthfirst search"""

    @classmethod
    def g(cls, parentnode, action, childnode):
        return 1 + parentnode.get_g()

    @classmethod
    def h(cls, state):
        return 0


class DepthFirst:
    """DepthFirst - depth first search"""

    @classmethod
    def h(cls, parentnode, action, childnode):
        return -1*(parentnode.get_h() + 1)

    @classmethod
    def g(cls, state):
        return 0


class Manhattan:
    """Manhattan Block Distance heuristic"""

    @classmethod
    def g(cls, parentnode, action, childnode):
        return 1 + parentnode.get_g()

    @classmethod
    def h(cls, state):
        dim = math.sqrt(len(state))
        hval = sum(abs((tile % dim) - (i % dim)) +
                   abs((tile // dim) - (i // dim))
                   for i, tile in enumerate(state) if tile)
        return hval
