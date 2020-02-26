"""
driver for graph search problem
"""

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


class Timer:
    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """

    def __init__(self):
        """Timer - Start a timer"""
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        """elapsed_s - Seconds elapsed since start (wall clock time)"""
        return time.time() - self.start

    def elapsed_min(self):
        """elapsed_min - Minutes elapsed since start (wall clock time)"""

        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min


def driver():
    # Assign number of trials, size of tileboards, and set verbose / debug flags or force_state
    ntrials = 1
    n = 8
    verbose, debug = False, False
    # f_state = [1, 2, 3, 4, 5, 6, None, 7, 8]

    # Initialize empty arrays to hold stat values
    btime, dtime, atime = [], [], []
    bnodes, dnodes, anodes = [], [], []
    bsteps, dsteps, asteps = [], [], []

    """ Run ntrials: each loop runs a breadth search, 
        depth search, and A* search """
    for trials in range(ntrials):
        # Initialize timer before each search
        # Create puzzle with costs specific to search type
        # Run graph search on created puzzle
        # Add stats to stat arrays

        bt = Timer()
        breadthpuzzle = NPuzzle(n, g=BreadthFirst.g, h=BreadthFirst.h)
        bsearch = graph_search(breadthpuzzle, verbose, debug)
        bsteps.append(len(bsearch[0]))
        bnodes.append(bsearch[1])
        btime.append(bt.elapsed_s())

        dt = Timer()
        depthpuzzle = NPuzzle(n, g=DepthFirst.h, h=DepthFirst.g)
        dsearch = graph_search(depthpuzzle, verbose, debug)
        dsteps.append(len(dsearch[0]))
        dnodes.append(dsearch[1])
        dtime.append(dt.elapsed_s())

        at = Timer()
        astarpuzzle = NPuzzle(n, g=Manhattan.g, h=Manhattan.h)
        asearch = graph_search(astarpuzzle, verbose, debug)
        asteps.append(len(asearch[0]))
        anodes.append(asearch[1])
        atime.append(at.elapsed_s())

    # Merge each stat array into an array for each search
    bdata, ddata, adata = [], [], []

    """ Compile stats and create table """
    if ntrials > 1:
        # Find mean and standard deviation for each stat of each search
        bdata = [mean(bsteps), stdev(bsteps, mean(bsteps)),
                 mean(bnodes), stdev(bnodes, mean(bnodes)),
                 mean(btime), stdev(btime, mean(btime))]

        ddata = [mean(dsteps), stdev(dsteps, mean(dsteps)),
                 mean(dnodes), stdev(dnodes, mean(dnodes)),
                 mean(dtime), stdev(dtime, mean(dtime))]

        adata = [mean(asteps), stdev(asteps, mean(asteps)),
                 mean(anodes), stdev(anodes, mean(anodes)),
                 mean(atime), stdev(atime, mean(atime))]

        # Combine all data into one list and round as necessary
        data = [bdata, ddata, adata]
        data = [[round(elem, 6) for elem in lis] for lis in data]

        # Create lists for table labels
        searches = ["Breadth Search", "Depth Search", "A* Search"]
        stats = ["Mean Steps", "Std Steps",
                 "Mean Nodes", "Std Nodes",
                 "Mean Time", "Std Time"]

        # Create table using formatted strings and for loop
        i = 0
        row_format = ("{:>14}" * (len(stats) + 1))
        print(row_format.format("", *stats))
        for stat, row in zip(stats, data):
            print(row_format.format(searches[i], *row))
            i += 1


if __name__ == '__main__':
    driver()
