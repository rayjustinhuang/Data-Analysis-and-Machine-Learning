# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:30:04 2021

@author: rjlo_
"""

# Simple Knapsack Problem

from pulp import *

# Initialize model
model = LpProblem("Loading Truck Problem", LpMaximize)

# Define data
weight = {'A': 12583, 'B': 9204, 'C': 12611, 'D': 12131, 'E': 12889, 'F': 11529}
profit = {'A': 102564, 'B': 130043, 'C': 127648, 'D': 155058, 'E': 238846, 'F': 197030}
prod = ['A', 'B', 'C', 'D', 'E', 'F']

# Define decision variables and objective
x = LpVariable.dicts('ship_', prod, cat='Binary')
model += lpSum([profit[i] * x[i] for i in prod])

# Define Constraint
# Maximum weight must be 25000 pounds
# Only one of D, E, or F can be included
model += lpSum([weight[i] * x[i] for i in prod]) <= 25000
model += x['D'] + x['E'] + x['F'] <= 1

model.solve()
for i in prod:
    print("{} status {}".format(i, x[i].varValue))