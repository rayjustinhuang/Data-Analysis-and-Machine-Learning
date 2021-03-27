# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:19:17 2021

@author: Ray Justin O. Huang
"""

# Traveling Salesman Problem
# Based on P01 from https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
from pulp import *
import pandas as pd

# Initialize model
model = LpProblem('TravelingSalesmanProblem', LpMinimize)

# Define lists and DataFrames
n = 15
cities = range(0, 15)
dist = pd.read_csv('p01_d.txt', sep='\s+', header=None)

# Define Decision Variables
x = LpVariable.dicts('X', [(c1, c2) for c1 in cities for c2 in cities], 
                     cat='Binary')
u = LpVariable.dicts('U', [c1 for c1 in cities], 
                     lowBound=0, upBound=(n-1), cat='Integer')

# Define Objective
model += lpSum([dist.iloc[c1, c2] * x[(c1, c2)] 
                for c1 in cities for c2 in cities])

# Define Constraints
for c1 in cities:
    model += lpSum([x[(c1, c2)] for c2 in cities if c1 != c2]) == 1
for c2 in cities:
    model += lpSum([x[(c1, c2)] for c1 in cities if c1 != c2]) == 1
for c1 in cities:
    for c2 in cities:
        model += lpSum(x[(c1, c2)] + x[(c2, c1)]) <= 1
    
# Solve model
model.solve()
print(model.objective.value())
for v in model.variables():
#    print(v)
    if v.varValue > 0:
        print(v.name, "=", v.varValue)