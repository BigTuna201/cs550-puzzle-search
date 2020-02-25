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
    ntrials = 10
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

    bdata.append(mean(bsteps)), bdata.append(stdev(bsteps, bdata[0]))
    bdata.append(mean(bnodes)), bdata.append(stdev(bnodes, bdata[2]))
    bdata.append(mean(btime)), bdata.append(stdev(btime, bdata[4]))

    ddata.append(mean(dsteps)), ddata.append(stdev(dsteps, ddata[0]))
    ddata.append(mean(dnodes)), ddata.append(stdev(dnodes, ddata[2]))
    ddata.append(mean(dtime)), ddata.append(stdev(dtime, ddata[4]))

    adata.append(mean(asteps)), adata.append(stdev(asteps, adata[0]))
    adata.append(mean(anodes)), adata.append(stdev(anodes, adata[2]))
    adata.append(mean(atime)), adata.append(stdev(atime, adata[4]))

    bdata = [round(elem, 4) for elem in bdata]
    ddata = [round(elem, 4) for elem in ddata]
    adata = [round(elem, 4) for elem in adata]

    data = [bdata, ddata, adata]
    searches = ["Breadth Search", "Depth Search", "A* Search"]
    stats = ["Mean Steps", "Std Steps",
             "Mean Nodes", "Std Nodes",
             "Mean Time", "Std Time"]

    ctr = 0
    row_format = ("{:>15}" * (len(stats) + 1))
    print(row_format.format("", *stats))
    for stat, row in zip(stats, data):
        print(row_format.format(searches[ctr], *row))
        ctr += 1


if __name__ == '__main__':
    driver()
