## Steps For Creating A Machine Learning Program (in Python)
			
### (i) Importing Required Packages: 
First of all we would need to import packages as and when required in our program. These packages are similar to header files in programming languages such as C/C++. They contain a bunch of functions developed by various developers to perform certain tasks and can be used easily. We need not write their logic from scratch and they are very well optimised to save our time and memory space both. If you face any type of import errors then make sure that the package which you are trying to use is already installed.

### (ii) Loading Data: 
Next we would have to determine a particular dataset using which we are interested to prepare a Machine Learning model and then load them into our program or we can import some of the famous or very popularly used datasets (like Iris dataset) which are available readily as packages. For importing data from CSV (Comma Separated Values) file or text files we can use either NumPy or Pandas. I recommend using pandas data frames as they provide lot of flexibilities such as including header rows or not and various other.

### (iii) Data Cleaning: 
We need to perform data cleaning if required. It involves removing tuples or records which are redundant or if have missing values. Another way to deal with missing values is to fill them by using various measures of central tendencies such as mean/median depending on the situation. Generally if a record has multiple fields missing we prefer to remove that record and if it has lesser number of fields or features missing we can use mean/median to fill those missing values.

### (iv) Finding Appropriate Algorithm: 
After performing data cleaning we need to find which algorithm is most appropriate for solving our problem. We can explore sklearn/scikit-learn package in python for ML functions. It contains almost any required ML algorithm. It is basic scientific kit/library of ML. We can also design our own algorithm either by using combinations of multiple algorithms or design our own algorithm from scratch depending on the situations and if required.

After we have identified the most appropriate algorithm and its associated function we need to explore its usage and various parameters which are associated with that function and try to improve its efficiency by tuning different parameters.

### (v) Data Representation: 
We can pictorially represent our datasets by using matplotlib, seaborn and various other libraries. It can be very useful to represent our data using graphs, histograms, plots or heat maps. It should always be used to present or explain our point to some else and it helps in better visualization of data. 

Feature engineering is also performed after this if we have many variables or parameters in our dataset and we need to keep only essential features. Remember that removing less important variables or unessential variables from our dataset improves the accuracy of our algorithm.

### (vi) Splitting dataset into train data and test data
After this comes the most essential step. Splitting our dataset into two partitions. One for training purpose and another for testing purpose. This can be done using inbuilt train_test_split function available to us. If we are working in some other programming language and if we do not have this train_test_split function then we divide the dataset ourselves into 60:40 ratio where 60% is used for training and 40% is used for testing (A rule that is followed generally).

### (vii) Training our Algorithm
Then feed our chosen algorithm with train data to learn patterns and identity which type of data points belong to which classes. This can also be done easily by using fit function which basically fits the train dataset into the algorithm.

After we are done with this, we have basically trained our model. Remember the larger the train dataset the better it would be enable our algorithm to distinguish between various classes.

### (viii) Predicting outcome using our model
Now we are ready to test our model. We can use our trained model to predict the outcome of test datasets. And to check how well it performed we can compare our results with actual classes of these test datasets.

### (ix) Finding accuracy
Lastly, we can find accuracy of the model using various functions of "metrics" sub package available in python. We can also use other techniques such can confusion matrix, Receiver Operating Curve (ROC), Precision Recall Curve, etc. to see how well our model has performed.

##### Note: These steps can be performed in any order in our program as per our convenience and a few other things can always be added or removed as per our requirements and necessity.
