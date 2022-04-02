# Author: Kitty Kwan



from nbformat import write


import pandas as pd  
# importing pandas to read the csv file

import numpy as np
# importing the numpy function


df = pd.read_csv('iris.csv', header=None)  
# Read CSV data and form a dataframe. Added "header=none" to take the first line of data set into account.

df.columns = ["Sepal_length", "Sepal_width", "Petal_length", "Petal_width", "Iris class"] 
# Adding headings to the dataset.

print (df)
# Print dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).

f = open ("iris.txt", "x")
# Create a txt file called iris and put to write mode

f.write (df.to_string)
# Writes the dataframe in the txt file,f.write (df) will only write a string into the txt file, not dataframe
