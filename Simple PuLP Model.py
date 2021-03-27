# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:37:46 2021

@author: rjlo_
"""

# Optimization with PuLP

from pulp import *

# Initialize model
model = LpProblem("MaximizeBakeryProfits", LpMaximize)

# Define variables
A = LpVariable('A_var', lowBound = 0, cat='Integer')
B = LpVariable('B_var', lowBound = 0, cat='Integer')

# Define objective function
model += 20 * A + 40 * B

# Define constraints - PuLP knows these are constraints because of the inequalities
model += 0.5 * A + 1 * B <= 30
model += 1 * A + 2.5 * B <= 60
model += 1 * A + 2 * B <= 22

# Solve model
model.solve()
print('Produce {} cake A'.format(A.varValue))
print('Produce {} cake B'.format(B.varValue))