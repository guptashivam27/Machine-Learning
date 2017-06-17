#Importing datasets
from sklearn.datasets import load_iris
iris = load_iris()

#Create an instance of the classifier
from sklearn import linear_model

##Let us try and run our classifier with different values of its parameters to see what type of results it produce

'''For more details of its input parameters here is a link to its documentation page: 
http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html '''

##logClassifier = linear_model.LogisticRegression(C=1, random_state=111)
logClassifier = linear_model.LogisticRegression(C=150, random_state=111)

#Splitting datasets into train and test datasets
from sklearn import cross_validation
x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.10, random_state=111)

#Using the instance of logistic regression classifier created above and calling the fit method to train the model with the 
#training dataset.
logClassifier.fit(x_train, y_train)
''' Output: LogisticRegression(C=150, class_weight=None, dual=False, fit_intercept=True,
            intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
            penalty='l2', random_state=111, solver='liblinear', tol=0.0001,
            verbose=0, warm_start=False) '''

#Feeding the test data to model
predicted = logClassifier.predict(x_test)
print predicted
''' Output: [0, 0, 2, 2, 1, 0, 0, 2, 2, 1, 2, 0, 2, 2, 2] '''

print y_test
''' Output: [0 0 2 2 1 0 0 2 2 1 2 0 2 2 2] '''

#Evalutaing the model and finding out how accurate it is
from sklearn import metrics
metrics.accuracy_score(y_test, predicted)
''' Output: 0.93333333333333335 '''

print predicted == y_test
''' Output: [ True  True  True  True  True  True  True  True  True  True  True  True
            False  True  True] '''
