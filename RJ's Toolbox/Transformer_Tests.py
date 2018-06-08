# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 08:02:30 2018

@author: Ray Justin O. Huang
"""
from Custom_Transformers import PerColumnAttributesAdder, StringCaseChanger, Randomizer, StringCleaner, GroupAggregator
import pandas as pd
import numpy as np
import string


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


# Sample dirty string DataFrames
sample5 = pd.DataFrame({'John': ['P@ssword', 'c@rp', 'Te^&*ting'],
                        'Mary': ['L*t##e','B!g','M$d*u_'],
                        'Jane': ['L!^b', 'H@d', 'P@!l']})


# StringCleaner testing
sample5.head()
cleaner = StringCleaner('Mary')
cleaner = StringCleaner('Mary')
cleaner.transform(sample5)
# sample5['Mary'].str.replace(string.punctuation, '')
sample5['Mary'].str.replace('[{}]'.format(string.punctuation), '')
# sample5['Mary'].str.translate(None, string.punctuation)
sample5['Mary'].str.translate({string.punctuation: None})
sample5.info()
sample5['Mary'].str.lower()

cleaner2 = StringCleaner('John')
cleaner2.transform(sample5)


# Sample grouping DataFrames
sample6 = pd.DataFrame({'Customer': ['Customer A', 'Customer A', 'Customer A',
                                     'Customer B', 'Customer B', 'Customer B',],
                        'Product': ['Product A', 'Product B', 'Product B',
                                    'Product A', 'Product C', 'Product A'],
                        'Price': [10, 15, 17, 8, 20, 7]})


# GroupAggregator testing
sample6.head()
grouper = GroupAggregator('Customer', np.median)
grouper.transform(sample6)
sample6.groupby('Customer').transform(np.mean)
