# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:11:41 2021

@author: rjlo_
"""

# Custom Functions
import pandas as pd

# convert_text_to_df
# Used to convert printed DataFrame output text to an actual DataFrame object
def convert_text_to_df(text):
    """
    A function used to convert printed DataFrame output text to an 
    actual DataFrame object

    Parameters
    ----------
    text : str
        Printed DataFrame output, a multiline string.

    Returns
    -------
    new_df : DataFrame
        A pandas DataFrame object.

    """
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