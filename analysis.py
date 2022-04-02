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
# If I was to print, dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).


print(df.to_csv(r'dataSummary.txt',
                header = df.columns,
                index = "Dataset",
                sep= " ",
                mode = "a"))
            

