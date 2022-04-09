# Author: Kitty Kwan



from nbformat import write


import pandas as pd  
# importing pandas to read the csv file

import numpy as np
# importing the numpy function

import matplotlib.pyplot as plt

import seaborn as sns




df = pd.read_csv ('iris.csv', header = None)  
# Read CSV data and form a dataframe. Added "header=none" to take the first line of data set into account.


df.columns = ["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)", "Class"] 
# Adding headings to the dataset.
# If I was to print, dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).

pd.set_option ("display.max_rows", 150)
# set no limit on the amount of rows or columns, to avoid "..." in summary data

with open ("data.txt", "w") as f:
     f.write (str(df))
# open txt file and set to write mode. Write data into txt file., added str ....

with open ("summaryData.txt", "w") as f:
    f.write (str(df[["Sepal length (cm)", "Sepal width (cm)", "Petal length (cm)", "Petal width (cm)"]].describe()))
   # the describe method, write a summary of statistics in a single txt file called summaryData, summary of each heading, not including class.



#df.hist (column="Sepal length (cm)")
#df.hist (column="Sepal width (cm)")
#df.hist (column="Petal length (cm)")
#df.hist (column="Petal width (cm)")
#plt.show()


sns.histplot (data= df, x= "Sepal length (cm)", hue= "Class",multiple='stack')
plt.title ("Sepal Length (cm)")
plt.savefig ("sepalLengthHist.png")

sns.histplot (data= df, x= "Sepal width (cm)", hue= "Class",multiple='stack')
plt.title ("Sepal width (cm)")
plt.savefig ("sepalWidthhist.png")

sns.histplot (data= df, x= "Petal length (cm)", hue= "Class",multiple='stack')
plt.title ("Petal length (cm)")
plt.savefig ("petalLengthhist.png")

sns.histplot (data= df, x= "Petal width (cm)", hue= "Class",multiple='stack')
plt.title ("Petal width (cm)")
plt.savefig ("petalWidthhist.png")
   







