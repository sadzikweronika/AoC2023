from functools import reduce
import aoc_lube
import numpy as np

data = aoc_lube.fetch(year=2023, day=6)
times, dists = map(lambda x: np.array(x.split()[1:]).astype(np.int_), data.splitlines())
deltas = times ** 2 - 4 * dists
sols1 = np.ceil((times - np.sqrt(deltas)) / 2).astype(np.int_)
sols2 = np.floor((times + np.sqrt(deltas)) / 2).astype(np.int_)
print("Part 1:", np.prod(sols2 - sols1 + 1))

time, dist = map(lambda x: x.split()[1:], data.splitlines())
time = int(reduce(lambda x, y: x + y, time))
dist = int(reduce(lambda x, y: x + y, dist))
delta = time ** 2 - 4 * dist
sols1 = np.ceil((time - np.sqrt(delta)) / 2).astype(np.int_)
sols2 = np.floor((time + np.sqrt(delta)) / 2).astype(np.int_)
print("Part 2:", sols2 - sols1 + 1)

