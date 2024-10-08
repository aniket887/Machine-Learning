# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Loading the Iris dataset
dataset=pd.read_csv('iris.csv')
# Creating the matrix of features (X) and the dependent variable vector (y)
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
# Printing the matrix of features and the dependent variable vector
print(X)
print(y)