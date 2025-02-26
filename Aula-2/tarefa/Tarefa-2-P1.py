import pandas as pd
import numpy as np

dataset = pd.read_csv('Exasens.csv')
dataset

dataset['Age'].fillna(dataset['Age'].mean(), inplace=True)
dataset