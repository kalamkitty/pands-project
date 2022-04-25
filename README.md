# Pands project 2022

# How to run the code
 - Install the latest version of python for example Anaconda.
 - Install Visual Studio Code.
 - Install any neccessary Python libraries e.g. Seaborn, matplotlib

# Introduction

This is my project for Programming and Scripting module. 
The Iris Data Set by Fisher, 1936 is a data set which consists of 150 records of "3 classes of 50 instances each", each class referes to a type of iris plant. It was first published in "The use of multiple measurements in taxonomic problems". 

The attributes (variables) that distinguish each type of iris plant are
      1. Sepal length in cm
      2. Sepal width in cm
      3. Petal width in cm
      4. Petal length in cm
      5. Class
         -- Iris Setonsa
         -- Iris Versicolour
         -- Iris Vinginica

# Task

The task is to research and analyse this data set using Python, produce visual representation of the data and summarise the findings.
 - summary of each variable to a single text file (overview of entire data set)
 - Histogram of each vairable to png files
 - Scatter plot for each pair of vairables
 - Any other analysis (correlation)

# Analysis of the Iris dataset

Libraries used:

- Matplotlib - This library is used to create visual representations of data such as histograms and bar charts. Further information on Matplotlib can be found here https://matplotlib.org/.

- Seaborn - The Seaborn library, based on Matplotlib is a data visualisation tool. It allows the user to fully customise the plots. Further information on Seaborn can be found here https://seaborn.pydata.org/index.html.

- Pandas - This is very useful tool in data analysisTo analyse the data, it allows users to analyse a data set, sort the data and add value. Put dataset into tables called dataframes, to write data to different file formats such as CSV and text files. Further information on pandas can be found here http://pandas.pydata.org/.


# TO DO

1. Importing dataset to repo as csv file. Write in file, headings ( https://www.pythontutorial.net/python-basics/python-write-csv-file/).
   Sort the data to a single text file. Add headings. "header=none" to take in account of the first row of data (ex how w/o it'll assume second row) (Ref w3 schools)
   To save this to a single text file. At my first attempt, I used write to txt file, notes from lecture, however the data did not look tidy, therefore I did further research (https://pandas.pydata.org/docs/user_guide/options.html)
   Organise the data.

2. Summary of data : min, max, median, skew, mean, std of each variable ("how to calculate summary statistics pandas). Used pandas' math functions to do this, but the code looked repetitive. To represent the summary stats on a table (towardsdatascience), using pandas' decribe method, compile the summary stats and display on a table. Summary of stats over all and by iris class using groupby function. (activestate)

3. For visual representation of data, there are Matplotlib, Seaborn and more (simplelilearn). Histogram of each variable, use matplotlib, showing the frequancy/distribution of a variable. Using w3 as base for my code. Histogram by class using seaborn (dataindependent). Step (element = "step") hard to read. According to jigsawacademy, Seaborn is used over Grouping data in python.
   Scatter plots, correlation between variables.  Used plt.close to avoid overlapping plots.


# Analysing dataset

# Observtions

- Summary of data

- Correlation 
  0 indicate no relationship/correlation
  1 indicate positive linear relationship
  This table suggest
  
- Histograms/Scatter plots
  






# References
https://www.w3schools.com/python/pandas/default.asp

https://realpython.com/pandas-dataframe/#retrieving-labels-and-data

https://www.stackvidhya.com/how-to-add-header-to-pandas-dataframe/#:~:text=You%20can%20add%20header%20to,%2C%20'column_Name_2'%5D%20method.&text=You%20can%20use%20the%20below,column%20headers%20to%20the%20dataframe.

https://pandas.pydata.org/docs/user_guide/options.html

https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html

https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe

https://towardsdatascience.com/mastering-summary-statistics-with-pandas-d515e17756be#:~:text=Pandas%20is%20a%20python%20library,statistical%20analysis%20and%20much%20more.

https://stackoverflow.com/questions/49188960/how-to-show-all-columns-names-on-a-large-pandas-dataframe

https://www.simplilearn.com/tutorials/python-tutorial/data-visualization-in-python#:~:text=Matplotlib%20and%20Seaborn%20are%20python,primarily%20used%20for%20statistical%20graphs.

https://www.onlinetutorialspoint.com/pandas/pandas-plotting-histogram-from-pandas-dataframes.html

https://dataindependent.com/pandas/pandas-histogram-dataframe-hist/

https://seaborn.pydata.org/generated/seaborn.histplot.html

https://realpython.com/pandas-groupby/

https://www.activestate.com/resources/quick-reads/how-to-group-data-in-python-using-pandas/

https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.close.html

https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf

Ratner, B. The correlation coefficient: Its values range between +1/−1, or do they?. J Target Meas Anal Mark 17, 139–142 (2009). https://doi.org/10.1057/jt.2009.5