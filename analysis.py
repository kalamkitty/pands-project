# Author: Kitty Kwan

######## Import Libraries ########

import pandas as pd  
# importing pandas to create dataframes, read the csv file, write to txt file.

import matplotlib.pyplot as plt
# importing matplotlib library for plots.

import seaborn as sns
# importing seaborn library, used to make histograms and scatter plots.

######## Reading from CSV and writing to txt ########

df = pd.read_csv ('iris.csv', header = None)  
# Read CSV data and form a dataframe. Added "header=none" to take the first line of data set into account.


df.columns = ["Sepal_length", "Sepal_width", "Petal_length", "Petal_width", "Class"] 
# Adding headings to the dataset.
# If I was to print, dataframe, the data set is too large therefore it will print a summary (first and last 5 rows).

pd.set_option ("display.max_rows", 150)
# set no limit on the amount of rows or columns, to avoid "..." in summary data.


with open ("data.txt", "w") as f:
     f.write (str(df))
    # open txt file and set to write mode. Write data into txt file.

with open ("summaryData.txt", "w") as f:
    f.write (str(df[["Sepal_length", "Sepal_width", "Petal_length", "Petal_width"]].describe()))
    f.write ("\n")
    f.write ("\n")
    # the describe method, write a summary of statistics in a single txt file called summaryData, summary of each heading, not including class. "\n"
    # used to append a line to space out info.

    f.write (str("Correlation between pairs of variables by class of iris\n"))
    f.write (str(df.groupby("Class").corr ()))
    # using pandas' built in 'corr' function to calculate the correlation between the variables of the dataset.

######## Histograms ########
# using seaborn.


sns.histplot (df, x= "Sepal_length", hue= "Class")   # y axis is frequancy.
plt.title ("Sepal_Length")                           # gives title to the plot.
plt.savefig ("sepalLengthHist.png")                  # save plot as _.png.
plt.close()                                          # stops plots overlapping each other.
                                                     # didn't use plt.legend as it was unneccessary.

sns.histplot (df, x= "Sepal_width", hue= "Class")
plt.title ("Sepal_width")
plt.savefig ("sepalWidthhist.png")
plt.close()

sns.histplot (df, x= "Petal_length", hue= "Class")
plt.title ("Petal_length")
plt.savefig ("petalLengthhist.png")
plt.close()

sns.histplot (df, x= "Petal_width", hue= "Class")
plt.title ("Petal_width")
plt.savefig ("petalWidthhist.png")
plt.close()

######## Scatter Plots ########
# using seaborn

sns.scatterplot (x= "Sepal_length", y= "Petal_length", data= df, hue= "Class")     # code similar to histplots above.
plt.title ("SepalLength vs PetalLength")
plt.savefig ("scatterPlot1.png")
plt.close()

sns.scatterplot (x= "Sepal_length", y= "Sepal_width", data= df, hue= "Class")
plt.title ("SepalLength vs SepalWidth")
plt.savefig ("scatterPlot2.png")
plt.close()

sns.scatterplot (x= "Petal_length", y= "Sepal_width", data= df, hue= "Class")
plt.title ("PetalLength vs SepalWidth")
plt.savefig ("scatterPlot3.png")
plt.close()

sns.scatterplot (x= "Petal_length", y= "Petal_width", data= df, hue= "Class")
plt.title ("PetalLength vs PetallWidth")
plt.savefig ("scatterPlot4.png")
plt.close()

sns.scatterplot (x= "Sepal_length", y= "Petal_width", data= df, hue= "Class")
plt.title ("SepalLength vs PetalWidth")
plt.savefig ("scatterPlot5.png")
plt.close()

sns.scatterplot (x= "Sepal_width", y= "Petal_width", data= df, hue= "Class")
plt.title ("SepalWidth vs PetalWidth")
plt.savefig ("scatterPlot6.png")
plt.close()










