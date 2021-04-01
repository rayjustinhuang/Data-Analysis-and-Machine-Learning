# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:14:51 2021

@author: rjlo_
"""

# Scheduling Problem Example
from pulp import *

# The class has been initialized, and x, days, and objective function defined

# Initialize model
model = LpProblem("MinimizeStaffing", LpMinimize)

# Define decision variables as the number of drivers starting work on day x
# Drivers have to work 5 days consecutively then take the next two days off
days = list(range(7))
x = LpVariable.dicts('staff_', days, lowBound=0, cat='Integer')

# Define objective function
model += lpSum([x[i] for i in days])

# Define constraints
model += x[0] + x[3] + x[4] + x[5] + x[6] >= 31
model += x[1] + x[4] + x[5] + x[6] + x[0] >= 45
model += x[2] + x[5] + x[6] + x[0] + x[1] >= 40
model += x[3] + x[6] + x[0] + x[1] + x[2] >= 40
model += x[4] + x[0] + x[1] + x[2] + x[3] >= 48
model += x[5] + x[1] + x[2] + x[3] + x[4] >= 30
model += x[6] + x[2] + x[3] + x[4] + x[5] >= 25

# Solve model
model.solve()
print([f'{v.name} = {v.varValue}' for v in model.variables()])