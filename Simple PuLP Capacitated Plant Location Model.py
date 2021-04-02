# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:19:45 2021

@author: Ray Justin Huang
"""

# Capacitated Plant Location Model

from pulp import *
import pandas as pd

# Initialize Class
model = LpProblem("CapacitatedPlantLocationModel", LpMinimize)

# Define helper function to convert pasted data into DataFrames
def convert_text_to_df(text):
    new_list = [i.strip() for i in text.splitlines() if i.strip() != ""]
    new_dict = {}
    col_name = new_list[0].strip().split()
    index_name = new_list[1].strip()
    for item in new_list[2:]:
        index, *others = item.split()
        others = [float(i) for i in others]
        new_dict[index] = others
    new_df = pd.DataFrame(new_dict).transpose()
    new_df.index.name = index_name
    new_df.columns = col_name
    return new_df

# Define Data
demand = '''                  Dmd
Supply_Region        
USA            2719.6
Germany          84.1
Japan          1676.8
Brazil          145.4
India           156.4
'''

variable_cost = """               USA  Germany  Japan  Brazil  India
Supply_Region                                    
USA              6       13     20      12     17
Germany         13        6     14      14     13
Japan           20       14      3      21      9
Brazil          12       14     21       8     21
India           22       13     10      23      8"""


fixed_cost = """               Low_Cap  High_Cap
Supply_Region                   
USA               6500      9500
Germany           4980      7270
Japan             6230      9100
Brazil            3230      4730
India             2110      3080"""

plant_capacities = """               Low_Cap  High_Cap
Supply_Region                   
USA                500      1500
Germany            500      1500
Japan              500      1500
Brazil             500      1500
India              500      1500"""

dmd = convert_text_to_df(demand)
var_cost = convert_text_to_df(variable_cost)
fix_cost = convert_text_to_df(fixed_cost)
cap = convert_text_to_df(plant_capacities)

# Define Decision Variables
loc = ['USA', 'Germany', 'Japan', 'Brazil', 'India']
size = ['Low_Cap','High_Cap']
x = LpVariable.dicts("production_",
                     [(i,j) for i in loc for j in loc],
                     lowBound=0, upBound=None, cat='Continuous')
y = LpVariable.dicts("plant_", 
                     [(i,s) for s in size for i in loc], cat='Binary')

# Define objective function
model += (lpSum([fix_cost.loc[i,s] * y[(i,s)] 
                 for s in size for i in loc])
          + lpSum([var_cost.loc[i,j] * x[(i,j)] 
                   for i in loc for j in loc]))

# Still need to add constraints and solution