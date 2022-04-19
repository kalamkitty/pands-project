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


df.columns = ["Sepal_length", "Sepal_width", "Petal_length", "Petal_width", "Class"] 
# Adding headings to the dataset.
# If I was to print, dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).

pd.set_option ("display.max_rows", 150)
# set no limit on the amount of rows or columns, to avoid "..." in summary data

df.groupby("Class")

with open ("data.txt", "w") as f:
     f.write (str(df))
# open txt file and set to write mode. Write data into txt file., added str ....

with open ("summaryData.txt", "w") as f:
    f.write (str(df[["Sepal_length", "Sepal_width", "Petal_length", "Petal_width"]].describe()))
   # the describe method, write a summary of statistics in a single txt file called summaryData, summary of each heading, not including class.


df.groupby("Class")
fig 1 = sns.histplot (data= df, x= "Sepal_length", hue= "Class",multiple='stack')
plt.title ("Sepal_Length")
plt.savefig ("sepalLengthHist.png")


sns.histplot (data= df, x= "Sepal_width", hue= "Class",multiple='stack')
plt.title ("Sepal_width")
plt.savefig ("sepalWidthhist.png")


sns.histplot (data= df, x= "Petal_length", hue= "Class",multiple='stack')
plt.title ("Petal_length")
plt.savefig ("petalLengthhist.png")


sns.histplot (data= df, x= "Petal_width", hue= "Class",multiple='stack')
plt.title ("Petal_width")
plt.savefig ("petalWidthhist.png")

######## Scatter Plots ########

sns.scatterplot (x= "Sepal_length", y= "Petal_length", data= df, hue= "Class")
plt.title ("SepalLength vs PetalLength")
plt.savefig ("scatterPlot1.png")

sns.scatterplot (x= "Sepal_length", y= "Sepal_Width", data= df, hue= "Class")
plt.title ("SepalLength vs SepalWidth")
plt.savefig ("scatterPlot2.png")

sns.scatterplot (x= "Petal_length", y= "Sepal_Width", data= df, hue= "Class")
plt.title ("PetalLength vs SepalWidth")
plt.savefig ("scatterPlot3.png")

sns.scatterplot (x= "Petal_length", y= "Petal_Width", data= df, hue= "Class")
plt.title ("PetalLength vs PetallWidth")
plt.savefig ("scatterPlot4.png")

sns.scatterplot (x= "Sepal_length", y= "Petal_Width", data= df, hue= "Class")
plt.title ("SepalLength vs PetalWidth")
plt.savefig ("scatterPlot5.png")

sns.scatterplot (x= "Sepal_Width", y= "Petal_Width", data= df, hue= "Class")
plt.title ("SepalWidth vs PetalWidth")
plt.savefig ("scatterPlot6.png")








