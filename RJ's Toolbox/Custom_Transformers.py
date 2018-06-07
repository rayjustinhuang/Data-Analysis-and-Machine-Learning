# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 07:35:15 2018

@author: Ray Justin O. Huang
"""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import string


# PerColumnAttributesAdder 
# Used to quickly add columns that are fractions of other columns
class PerColumnAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, denominator_column, numerator_columns):
        self.denominator_column = denominator_column
        self.numerator_columns = numerator_columns
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        self.newcolumns = [_+"_per_"+self.denominator_column for _ in self.numerator_columns]
        X_copy = X.copy()
        
        for index, col in enumerate(self.numerator_columns):
            X_copy[self.newcolumns[index]] = X_copy[col] / X_copy[self.denominator_column]
        
        return X_copy


# StringCaseChanger
# Used to change the case of a columns that contains strings
class StringCaseChanger(BaseEstimator, TransformerMixin):
    def __init__(self, cols, case='upper'):
        self.case = case
        self.cols = cols
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        df = X.copy()
        if self.case == 'upper':
            for col in self.cols:
                df[col] = df[col].str.upper()
        elif self.case == 'lower':
            for col in self.cols:
                df[col] = df[col].str.lower()
        elif self.case == 'title':
            for col in self.cols:
                df[col] = df[col].str.title()
        
        return df
    
    
# Randomizer
# Used to randomize the number values in columns by multiplying with a random number between 0.5 and 1.5
class Randomizer(BaseEstimator, TransformerMixin):
    def __init__(self, cols, added_cols=False, integers=False, random_state=47):
        self.cols = cols
        self.added_cols = added_cols
        self.integers = integers
        self.random_state = random_state
        
    def fit(self, X, y=None):
        self.rgen = np.random.RandomState(self.random_state)
        self.rows = X[self.cols].shape[0]
        self.columns = len(self.cols)
        self.randomizercols = self.rgen.rand(self.rows, self.columns) + 0.5
        
        return self
    
    def transform(self, X, y=None):
        df = X.copy()
        if not self.added_cols:
            if not self.integers:
                df[self.cols] = df[self.cols]*self.randomizercols
                return df
            else:
                df[self.cols] = np.rint(df[self.cols]*self.randomizercols)
                return df
        else:
            if not self.integers:
                self.newcol_names = ["randomized_"+_ for _ in self.cols]
                df[self.newcol_names] = df[self.cols]*self.randomizercols
                self.newcols = df[self.newcol_names]
                # self.newcols = pd.DataFrame(self.newcols)
                # df = pd.concat([df, df[self.newcols], axis=1)
                return df
            else:
                self.newcol_names = ["randomized_"+_ for _ in self.cols]
                df[self.newcol_names] = np.rint(df[self.cols]*self.randomizercols)
                self.newcols = df[self.newcol_names]
                return df
            
            
# StringCleaner
# Used to clean columns containing strings
class StringCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, cols, case='lower'):
        self.cols = cols
        self.case = case
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        df = X.copy()
        df[self.cols] = df[self.cols].str.replace('[{}]'.format(string.punctuation), '')
        df[self.cols] = df[self.cols].str.strip()
        if self.case == 'upper':
            df[self.cols] = df[self.cols].str.upper()
        elif self.case == 'title':
            df[self.cols] = df[self.cols].str.title()
        else:
            df[self.cols] = df[self.cols].str.lower()
        return df
    
