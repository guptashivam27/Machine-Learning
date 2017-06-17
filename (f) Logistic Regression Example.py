'''
Problem Statement:

In this example we are interested to find how variables such as GRE (Graduate Record Exam scores), GPA (grade point average) and prestige of the undergraduate institution, effect admission into graduate school. The response variable, admit/don’t admit, is a binary variable.

I am going to solve this problem using logistic regression. Let's see how well our model performs!
'''

## Importing required packages
''' First of all let us import all the packages which we would require for this task '''
import pandas as pd
import matplotlib.pyplot as pl
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import metrics

## Loading the datasets
''' Here I am importing the datasets directly from its URL address. We can also import datasets from our local file 
    directory on our system '''
df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/binary.csv")

''' Let us see what all different features are present in our dataset by printing the top 5 rows or head of the dataset '''
print("\nHead of the dataset is:\n")
print df.head()

'''
Here, GRE score, GPA obtained during undergraduation, and rank (prestige of undergraduate college) are predictor variables or input variables for our model. Institutions with a rank of 1 have the highest prestige, while those with a rank of 4 have the lowest.

While admit is binary target variable or output vaiable. It indicates whether or not a candidate was admitted our not.
'''

''' Now let us have a look at the description of the dataset, i.e. minimum value, maximum value, standard deviation and 
    other values for each field of the dataset '''
print ("\nDescription of dataset is as follows:\n")
print df.describe()

## Performing various data cleaning operations
''' First let us find our how may rows and columns are present in the dataset initially by printing its shape '''
print ("\nInitially, Shape of dataset is (rows, columns): " + str(df.shape))

''' Now, let us check if there are any blank tuples or records present in dataset by finding out total null fields '''
print df.isnull().sum()

''' Further we drop duplicate records (if any) present in dataset to remove data redundency '''
data = df.drop_duplicates()
print ("Shape of dataset after dropping duplicate records is (rows, columns): " + str(data.shape))

## Data represntation using histograms
data.gre.hist()
pl.title("Histogram of GRE (Graduate Record Exam) Scores")
pl.xlabel("GRE Score")
pl.ylabel("Frequency")
pl.show()

data.gpa.hist()
pl.title("Histogram of GPA (Grade Point Average)")
pl.xlabel("GPA")
pl.ylabel("Frequency")
pl.show()

''' Here, I am renaming field rank to prestige as rank is an inbuilt function and there are some conflicts while plotting 
    histogram using field name as rank '''
data.columns = ['admit', 'gre', 'gpa', 'prestige']
data.prestige.hist()
pl.title("Histogram of prestige of the undergraduate institution")
pl.xlabel("Prestige")
pl.ylabel("Frequency")
pl.show()

data.admit.hist()
pl.title("Histogram of Admitted")
pl.xlabel("Admitted")
pl.ylabel("Frequency")
pl.show()

## Splitting dataset into train data and test data
predictor_cols = ['gre', 'gpa', 'prestige']
target_cols = ['admit']

x_train, x_test, y_train, y_test = cross_validation.train_test_split(data[predictor_cols], data[target_cols], test_size=0.40)

## Training our algorithm
logClassifier = linear_model.LogisticRegression()
logClassifier.fit(x_train, y_train)

## Predicting outcome using our model
predicted = logClassifier.predict(x_test)

## Finding accuracy
print ("Accuracy of model is: ")
print metrics.accuracy_score(y_test, predicted)
