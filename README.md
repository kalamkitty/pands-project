# Pands project 2022

# How to run the code
 - Install the latest version of python for example Anaconda.
 - Install Visual Studio Code.
 - Install any neccessary Python libraries e.g. Seaborn, matplotlib

## Table of Contents
1. Introduction
    -  Fisher's Iris data set
2. Task
3. analysis.py
    -  Libraries used
      - Summary of variables in a single text file
        -  Observations
    -  Visual representation of data
        -  Observations
4. Conclusions
5. References


## 1. Introduction

This is my project for Programming and Scripting module 2022. Instructions for this assignment can be found here https://learnonline.gmit.ie/pluginfile.php/547122/mod_label/intro/Project.pdf?time=1646300056436

### Fisher's Iris data set
The Iris Data Set by Roanld Fisher, 1936 is a data set which consists of 150 records of "3 classes of 50 instances each", each class referes to a type of iris plant. It was first published in "The use of multiple measurements in taxonomic problems" (Fisher, 1936).
The data on the two species, Setonsa and Versicolour were collected in Quebac, Canada from the same location by Dr E. Anderson. It was assumed that the Virginica data was collected in the same fashion before Fisher included the dataset in his journal (Anderson, 1936).

The purpose of the dataset was to identify species of the Iris flower based on their attributes, however nowadays, it is used worldwide by those who pratice data science. It is an open source dataset with very few variables which makes data visualisation easy. There is a balance of data (50 measurements of each variable) and no missing data (Qureshi, 2021).

The attributes (variables) that distinguish each type of iris plant are
  * Sepal length in cm
  * Sepal width in cm
  * Petal width in cm
  * Petal length in cm
  * Class
         - Iris Setonsa
         - Iris Versicolour
         - Iris Virginica

## 2. Task

The task is to research and analyse this data set using Python, produce visual representation of the data and summarise the findings.
 * Summary of each variable to a single text file (overview of entire data set)
 * Histogram of each vairable to png files
 * Scatter plot for each pair of vairables
 * Any other analysis 

## 3. analysis.py

### Libraries used

* Matplotlib - This library is used to create visual representations of data such as histograms and bar charts. Further information on Matplotlib can be found here https://matplotlib.org/.

* Seaborn - The Seaborn library, based on Matplotlib is a data visualisation tool. It allows the user to fully customise the plots. Further information on Seaborn can be found here https://seaborn.pydata.org/index.html.

* Pandas - This is very useful tool in data analysisTo analyse the data, it allows users to analyse a data set, sort the data and add value. Put dataset into tables called dataframes, to write data to different file formats such as CSV and text files. Further information on pandas can be found here http://pandas.pydata.org/.

``` python
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns  
``` 

### Summary of variables in a single text file
The following program uses Pandas to creat a dataframe from importing dataset (csv file). Add headings.
Sort the data to a single text file. "header=none" to take in account of the first row of data (without it will assume second row of data is the first row of data to be considered). 

```python
df = pd.read_csv ('iris.csv', header = None)  #df = dataframe
df.columns = []
pd.set_option ()
```
Creating a summary table of data : min, max, median, mean, std of each variable using the describe function of Pandas. 
Write to summaryData.txt. Represents the summary stats on a table. To be more specific, I used the groupby function to get summary stats for each class.

```python
with open ("summaryData.txt", "w") as f:
   f.write (str(df[["Sepal_length", "Sepal_width", "Petal_length", "Petal_width"]].describe()))
   f.write (str(df.groupby("Class").describe ())) 
```

Using Pandas' built in correlation function ".corr ()", to calculate the correlation between pairs of variables in the dataset.

```python
f.write (str("Correlation between pairs of variables by class of iris\n"))
    f.write (str(df.groupby("Class").corr ()))
```

#### Observations
- Describe table 
  * Iris virginica have the longest sepal length and petal length.
  * Iris setonsa have the largest sepal width but the average (mean) petal length is much smaller than the other species.
  * Mean = average of data.
  * Standard deviation = spread of data.

- Correlation 
  0 indicate no relationship/correlation
  1 indicate positive linear relationship
  This table suggests;
* Iris setosa
   - Sepal length and sepal width have a strong correlation.
   - Low linear relationship between all other attributes.
* Iris versicolor 
    - Petal length and sepal length, petal length and petal width have strong correlation.     
* - Iris virginica
    - Only petal length and sepal length have a strong linear relationship.


### Visual representation of data
For visual representation of data, there are Matplotlib, Seaborn and more (simplelilearn). 

The below program was used to plot histogram of each variable, using seaborn, showing the frequancy/distribution of a variable.

```python
sns.histplot (df, x= , hue= )
plt.title ()
plt.savefig ()
plt.close()
```
Seaborn can be also used to create scatter plots, which shows correlation between variables.  

```python
sns.scatterplot (x= , y= , data= df, hue= )
plt.title ()
plt.savefig ()
plt.close()
```
#### Observations
The most useful scatterplots for comparison between the variables are the following;
- Sepal Length vs Sepal Width : No relation between these variables amongst all three iris class.
- Petal Length vs Sepal Width : Strong linear relationship between these variables with Verisocolor and Virginica.
- Petal Length vs Petal Width : Strongest linear relationship between these variables amongst all species. Petal length increases as petal widths increase.


From the histograms, we can make the following observations;
- Setosa stands out from the other iris classes in petal length and petal width.
- Petal length and petal width measurements are more useful for classification of the iris class as these histograms have very little overlap.

 

## 4. Conclusion
From summary data and the visual representation of the data set, I can come to the conclusion that the Setosa species is very different from Vericolour and Virginica as there is more data overlap and correlation with the latter two species, setosa petal widths are significantly smaller than the other iris classes. Petal length and petal width measurements are much better classification attributes than the other attributes.





## 5. References
Anderson, E., 1936. The Species Problem in Iris. Annals of the Missouri Botanical Garden, 23(3), p.457.

Aruchamy, V., 2021. How To Add Header To Pandas Dataframe? - Stack Vidhya. [online] Stack Vidhya. Available at: <https://www.stackvidhya.com/how-to-add-header-to-pandas-dataframe/#:~:text=You%20can%20add%20header%20to,%2C%20'column_Name_2'%5D%20method.&text=You%20can%20use%20the%20below,column%20headers%20to%20the%20dataframe.> [Accessed April 2022].

Dataindependent.com. n.d. Pandas Histogram – DataFrame.hist(). [online] Available at: <https://dataindependent.com/pandas/pandas-histogram-dataframe-hist/> [Accessed April 2022].

FISHER, R., 1936. THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS. Annals of Eugenics, 7(2), pp.179-188.

Halford, E., 2020. Evaluating linear relationships - How to use scatterplots, correlation coefficients, and linear regression effectively. [online] towardsdatascience. Available at: <https://towardsdatascience.com/evaluating-linear-relationships-1d239f51297b> [Accessed April 2022].

Matplotlib.org. n.d. Matplotlib documentation — Matplotlib 3.5.0 documentation. [online] Available at: <https://matplotlib.org/3.5.0/index.html> [Accessed April 2022].

onlinetutorialspoint. 2021. Pandas - Plotting Histogram from pandas Dataframes. [online] Available at: <https://www.onlinetutorialspoint.com/pandas/pandas-plotting-histogram-from-pandas-dataframes.html> [Accessed April 2022].

Pandas.pydata.org. n.d. pandas - Python Data Analysis Library. [online] Available at: <https://pandas.pydata.org/> [Accessed April 2022].

Pierre, S., 2020. Mastering Summary Statistics with Pandas. [online] Medium. Available at: <https://towardsdatascience.com/mastering-summary-statistics-with-pandas-d515e17756be#:~:text=Pandas%20is%20a%20python%20library,statistical%20analysis%20and%20much%20more.> [Accessed April 2022].

Python Tutorial - Master Python Programming For Beginners from Scratch. n.d. How to Write to CSV Files in Python. [online] Available at: <https://www.pythontutorial.net/python-basics/python-write-csv-file/> [Accessed April 2022].

Qureshi, S., 2021. The Mighty Iris Dataset. [online] Braintoy. Available at: <https://braintoy.ai/2021/04/19/mighty-iris-dataset/> [Accessed April 2022].

Ratner, B., 2009. The correlation coefficient: Its values range between +1/−1, or do they?. Journal of Targeting, Measurement and Analysis for Marketing, 17(2), pp.139-142.

Seaborn.pydata.org. n.d. seaborn: statistical data visualization — seaborn 0.11.2 documentation. [online] Available at: <https://seaborn.pydata.org/> [Accessed April 2022].

Simplilearn. 2021. A Complete Guide to Data Visualization in Python With Libraries, Chart, Graphs & More. [online] Available at: <https://www.simplilearn.com/tutorials/python-tutorial/data-visualization-in-python#:~:text=Matplotlib%20and%20Seaborn%20are%20python,primarily%20used%20for%20statistical%20graphs.> [Accessed April 2022].

Singh, D., 2019. Interpreting Data Using Descriptive Statistics with Python | Pluralsight. [online] Pluralsight.com. Available at: <https://www.pluralsight.com/guides/interpreting-data-using-descriptive-statistics-python> [Accessed April 2022].

Solomon, B., 2020. Pandas GroupBy: Your Guide to Grouping Data in Python – Real Python. [online] Realpython.com. Available at: <https://realpython.com/pandas-groupby/> [Accessed April 2022].

Stack Overflow. n.d. How do I expand the output display to see more columns of a Pandas DataFrame?. [online] Available at: <https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe> [Accessed April 2022].

Stack Overflow. n.d. How to show all columns' names on a large pandas dataframe?. [online] Available at: <https://stackoverflow.com/questions/49188960/how-to-show-all-columns-names-on-a-large-pandas-dataframe> [Accessed April 2022].

Stojiljković, 2020. The Pandas DataFrame: Make Working With Data Delightful – Real Python. [online] Realpython.com. Available at: <https://realpython.com/pandas-dataframe/#retrieving-labels-and-data> [Accessed April 2022].

W3schools.com. n.d. Pandas Tutorial. [online] Available at: <https://www.w3schools.com/python/pandas/default.asp> [Accessed April 2022].