import numpy as np  # a module for working with numerical array
import pandas as pd  # a module for working with data-frames
from matplotlib import pyplot as plt

################ # Loading elections 2021 elections data:

data_path = "/Users/elad.sofer/src/Python_Course/task6/"

# Notice that the  encoding isn't ASCII, since hebrew isn't supported.
df_2021_raw = pd.read_csv(data_path + 'votes per city 2021.csv',  encoding = 'iso-8859-8', index_col='שם ישוב')

# removing unnecessary meta-data
df_2021 = df_2021_raw.drop('סמל ועדה', axis=1)
df_2021 = df_2021[df_2021.columns[5:]]
df_2021_raw.head()
df_2021.style.set_properties(**{'text-align': 'left'})
df_2021.head()

################ Question 1:

def question_1():
    """
    :return:
    """

################ Question 2:

def question_2():
    """

    :return:
    """

################ Question 3:

def question_3():
    """

    :return:
    """