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
    ntrials = 50
    n = 3

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

    bdata, ddata, adata = [], [], []

    bdata = [mean(bsteps), stdev(bsteps, mean(bsteps)),
             mean(bnodes), stdev(bnodes, mean(bnodes)),
             mean(btime), stdev(btime, mean(btime))]

    ddata = [mean(dsteps), stdev(dsteps, mean(dsteps)),
             mean(dnodes), stdev(dnodes, mean(dnodes)),
             mean(dtime), stdev(dtime, mean(dtime))]

    adata = [mean(asteps), stdev(asteps, mean(asteps)),
             mean(anodes), stdev(anodes, mean(anodes)),
             mean(atime), stdev(atime, mean(atime))]

    data = [bdata, ddata, adata]
    data = [[round(elem, 6) for elem in lis] for lis in data]

    searches = ["Breadth Search", "Depth Search", "A* Search"]
    stats = ["Mean Steps", "Std Steps",
             "Mean Nodes", "Std Nodes",
             "Mean Time", "Std Time"]

    i = 0
    row_format = ("{:>14}" * (len(stats) + 1))
    print(row_format.format("", *stats))
    for stat, row in zip(stats, data):
        print(row_format.format(searches[i], *row))
        i += 1


if __name__ == '__main__':
    driver()
