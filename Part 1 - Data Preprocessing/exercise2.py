# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
# Load the dataset
dataset=pd.read_csv('pima-indians-diabetes.csv')
# Identify missing data (assumes that missing data is represented as NaN)
md=dataset.isnull().sum()
# Print the number of missing entries in each column
print(md)
# Configure an instance of the SimpleImputer class
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
# Fit the imputer on the DataFrame
imputer.fit(dataset)
# Apply the transform to the DataFrame
datasett=imputer.transform(dataset)
#Print your updated matrix of features
print(datasett)