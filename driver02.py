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
    ntrials = 1
    n = 8

    btime, dtime, atime = [], [], []
    bnodes, dnodes, anodes = [], [], []
    bsteps, dsteps, asteps = [], [], []

    for trials in range(ntrials):
        bt = Timer()
        breadthpuzzle = NPuzzle(n, g=BreadthFirst.g, h=BreadthFirst.h)
        bsearch = graph_search(breadthpuzzle, verbose=False)
        bsteps.append(len(bsearch[0]))
        bnodes.append(bsearch[1])
        btime.append(bt.elapsed_s())

        dt = Timer()
        depthpuzzle = NPuzzle(n, g=DepthFirst.h, h=DepthFirst.g)
        dsearch = graph_search(depthpuzzle, verbose=False)
        dsteps.append(len(dsearch[0]))
        dnodes.append(dsearch[1])
        dtime.append(dt.elapsed_s())

        at = Timer()
        astarpuzzle = NPuzzle(n, g=Manhattan.g, h=Manhattan.h)
        asearch = graph_search(astarpuzzle, verbose=False)
        asteps.append(len(asearch[0]))
        anodes.append(asearch[1])
        atime.append(at.elapsed_s())

    bmean_steps, bmean_nodes, bmean_time = mean(bsteps), mean(bnodes), mean(btime)
    bstd_steps, bstd_nodes, bstd_time = stdev(bsteps, bmean_steps), stdev(bnodes, bmean_nodes), stdev(btime, bmean_time)
    
    dmean_steps, dmean_nodes, dmean_time = mean(dsteps), mean(dnodes), mean(dtime)
    dstd_steps, dstd_nodes, dstd_time = stdev(dsteps, dmean_steps), stdev(dnodes, dmean_nodes), stdev(dtime, dmean_time)
    
    amean_steps, amean_nodes, amean_time = mean(asteps), mean(anodes), mean(atime)
    astd_steps, astd_nodes, astd_time = stdev(asteps, amean_steps), stdev(anodes, amean_nodes), stdev(atime, amean_time)
    
    print("Breadth Search", "Depth Search", "A* Search")
    print("Mean Steps", bmean_steps, dmean_steps, amean_steps)
    print("St Dev Steps %.4f %.4f %.4f" % (round(bstd_steps,4), round(dstd_steps,4), round(astd_steps,4)))
    print("Mean Nodes", bmean_nodes, dmean_nodes, amean_nodes)
    print("St Dev Nodes %.4f %.4f %.4f" % (round(bstd_nodes,4), round(dstd_nodes,4), round(astd_nodes,4)))
    print("Mean Time %.4f %.4f %.4f" % (round(bmean_time,4), round(dmean_time,4), round(amean_time,4)))
    print("St Dev Time %.4f %.4f %.4f" % (round(bstd_time,4), round(dstd_time,4), round(astd_time,4)))


if __name__ == '__main__':
    driver()
