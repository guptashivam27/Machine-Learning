## Support Vector Machine (SVM)

- Support Vector Machine (SVM) is a supervised machine learning algorithm which can be used for both classification or regression purpose. However,  it is mostly used in classification problems. 

- Support Vectors are simply the <b>co-ordinates of individual observation</b>.

- Support Vector Machine is a <b>frontier or hyper-plane</b> which best segregates the two classes (hyper-plane/ line).

- In this algorithm, we plot each data item as a point in n-dimensional space (where n is number of features we have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the <b>hyper-plane</b> that differentiate the two classes very well.

<p align="center">
  <img src="http://openclassroom.stanford.edu/MainFolder/courses/MachineLearning/exercises/ex7materials/twofeature_b.png" width="500"/>
</p>

## Working of SVM

The main task involved in this algorithm is identification of an ideal frontier / hyper-plane which segregates various datapoints into appropriate class labels. Let us consider various scenarios which may occur while finding correct hyper-plane:

- <b>Scenario 1:</b><br/> 
Here, we have three hyper-planes (A, B and C). Now we need to identify the right hyper-plane to classify star and circle. We need to remember that to identify the right hyper-plane we should select the hyper-plane which segregates the two classes better. In this scenario, hyper-plane “B” is the most appropriate one.

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_21.png" width="350"/>
</p>

- <b>Scenario 2:</b><br/> 
Here, we have three hyper-planes (A, B and C) and all are segregating the classes well. Now, How can we identify the right hyper-plane? Here, maximizing the distances between nearest data point (either class) and hyper-plane will help us to decide the right hyper-plane. This distance is called as Margin. <br/> <br/> We can see that the margin for hyper-plane C is high as compared to both A and B. Hence, we name the right hyper-plane as C. Another reason for selecting the hyper-plane with higher margin is robustness. If we select a hyper-plane having low margin then there is high chance of miss-classification.

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_4.png" width="350"/>
</p>

- <b>Scenario 3:</b><br/> 
Consider the scenario given below. Some of us may have selected the hyper-plane B as it has higher margin compared to A. But, SVM selects the hyper-plane which classifies the classes accurately prior to maximizing margin. Here, hyper-plane B has a classification error and A has classified all correctly. Therefore, the right hyper-plane is A.

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_5.png" width="350"/>
</p>

- <b>Scenario 4:</b> <br/>
Here we are unable to segregate the two classes using a straight line, as one of star lies in the territory of other(circle) class as an outlier. One star at other end is like an outlier for star class. SVM has a feature to ignore outliers and find the hyper-plane that has maximum margin. Hence, we can say, <b>SVM is robust to outliers</b>.

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_61.png" width="350"/>
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_71.png" width="350"/>
</p>

- <b>Scenario 5:</b> <br/>
In the scenario below, we can’t have linear hyper-plane between the two classes, so how does SVM classify these two classes? 

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_8.png" width="350"/>
</p>

SVM solves this problem by introducing additional feature. Here, we will add a new feature z=x^2+y^2. Now, let’s plot the data points on axis x and z:

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_9.png" width="350"/>
</p>

In SVM, it is easy to have a linear hyper-plane between these two classes. But, another question which arises is, should we need to add this feature manually to have a hyper-plane. No, SVM has a technique called the kernel trick. These are functions which takes low dimensional input space and transform it to a higher dimensional space i.e. it converts not separable problem to separable problem, these functions are called kernels. It is mostly useful in non-linear separation problem. Simply put, it does some extremely complex data transformations, then find out the process to separate the data based on the labels or outputs we have defined.

When we look at the hyper-plane in original input space it looks like a circle:

<p align="center">
  <img src="https://www.analyticsvidhya.com/wp-content/uploads/2015/10/SVM_10.png" width="350"/>
</p>

<h3>Some advantages and disadvantages associated with SVM are:</h3>

<h4>Advantages:</h4>
- It works really well with clear margin of separation
- It is effective in high dimensional spaces.
- It is effective in cases where number of dimensions is greater than the number of samples.
- It uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

<h4>Disadvantages:</h4>
- It doesn’t perform well, when we have large data set because the required training time is higher
- It also doesn’t perform very well, when the data set has more noise i.e. target classes are overlapping
- SVM doesn’t directly provide probability estimates.

<h4>References:</h4> 
(i) <href>https://www.analyticsvidhya.com/blog/2015/10/understaing-support-vector-machine-example-code/<href><br/>
(ii) <href>https://en.wikipedia.org/wiki/Support_vector_machine
