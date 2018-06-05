# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 08:02:30 2018

@author: Ray Justin O. Huang
"""
from Custom_Transformers import PerColumnAttributesAdder, StringCaseChanger, Randomizer
import pandas as pd
import numpy as np


# Sample DataFrames    
sample1 = pd.DataFrame({'a': [1,2,3,4,5,6,7],
                       'b': [2,4,6,8,10,12,14],
                       'c': [3,6,9,12,15,18,21]})
    
sample2 = pd.DataFrame(np.random.randn(100,5),
                       columns=['z','y','x','w','v'])


# Testing PerColumnAttributesAdder object
percol = PerColumnAttributesAdder('b', ['a','c'])

percol.transform(sample1)

percol.numerator_columns
percol.denominator_column
percol.newcolumns

percol2 = PerColumnAttributesAdder('z', ['y','w'])

percol2.transform(sample2).head()


# Loading iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
iris.keys()

iris_X = pd.DataFrame(iris['data'], columns=iris['feature_names'])
iris_y = pd.Series(iris['target'], name='species')


# Sample DataFrames with strings
sample3 = pd.DataFrame({'ingredients': ['milk','Cheese','BACON','bread','Ham'],
                        'utensils': ['SPATULA', 'spoon', 'Fork', 'Knife', 'cheese grater']})


# Testing StringCaseChanger object
casechanger = StringCaseChanger(['ingredients','utensils'], 'title')

casechanger.transform(sample3)

sample3['ingredients'].str.upper()
sample3['ingredients']

iris_X['sepal length (cm)'].shape


# Testing Randomizer object
rdm = Randomizer(['a','b'], added_cols=True, integers=True)

rdm.fit(sample1)

rdm.transform(sample1)
rdm.newcols
rdm.randomizercols


# More sample DataFrames
rgen = np.random.RandomState(47)
sample4 = pd.DataFrame(np.rint(1000*rgen.rand(5,5)+1000), columns=['first','second','third','fourth','fifth'])
sample4.head()


# More Randomizer testing
rdm2 = Randomizer(['third', 'fifth'], added_cols=True, integers=True)

rdm2.fit(sample4)

rdm2.transform(sample4)
