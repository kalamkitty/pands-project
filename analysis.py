# Author: Kitty Kwan



from nbformat import write


import pandas as pd  
# importing pandas to read the csv file

import numpy as np
# importing the numpy function


df = pd.read_csv('iris.csv', header = None)  
# Read CSV data and form a dataframe. Added "header=none" to take the first line of data set into account.


df.columns = ["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)", "Class"] 
# Adding headings to the dataset.
# If I was to print, dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).

pd.set_option('display.max_rows', 150)
# setting the max display rows to 150 as there are 150 lines of data.

with open('dataSummary.txt', "w") as f:
     f.write(str(df))
# open txt file and set to write mode. Write data into txt file.

print ("Mean", df["Sepal length (cm)"].mean())   
print ("Mean", df["Sepal width (cm)"].mean()) 
print ("Mean", df["Petal length (cm)"].mean()) 
print ("Mean", df["Petal width (cm)"].mean())  



