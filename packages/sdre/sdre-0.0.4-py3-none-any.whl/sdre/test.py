#!/usr/bin/env python

import sdre
import matplotlib.pyplot as plt

n_cells = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 8]
data = {i: [n] for i, n in enumerate(n_cells)}

# set up the model with the data from before
target = sdre.LikelihoodModel(data, n_samples=64)

# we define two parameter combinations which by default are the cell cycle time, 
# log number of stages, and initial population size
x0, x1 = [.9, 2, 1], [1.2, 1, 1]

nlls = []

for i, x in enumerate([x0, x1]):
    # computes the synthetic log likelihood loss
    nll = target.compute_negative_log_likelihood(x)
    nlls.append(nll)

print(nlls)
assert nlls[0] < nlls[1]

