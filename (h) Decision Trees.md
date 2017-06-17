## Decision Trees

- Decision tree is a type of supervised learning algorithm (having a pre-defined target variable) that is mostly used in classification problems. 

- It works for both categorical and continuous input and output variables. 

- In this technique, we split the population or sample into two or more homogeneous sets (or sub-populations) based on most significant splitter / differentiator in input variables.

- It is a decision support tool that uses a tree-like graph or model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility.


## Types of Decision Trees

Types of decision tree is based on the type of target variable we have. It can be of two types:

- Categorical Variable Decision Tree: Decision Tree which has categorical target variable then it called as categorical variable decision tree. Example: YES or NO.

- Continuous Variable Decision Tree: Decision Tree has continuous target variable then it is called as Continuous Variable Decision Tree.


## Terminology related to Decision Trees

- Root Node: It represents entire population or sample and this further gets divided into two or more homogeneous sets.

- Splitting: It is a process of dividing a node into two or more sub-nodes.

- Decision Node: When a sub-node splits into further sub-nodes, then it is called decision node.

- Leaf / Terminal Node: Nodes do not split is called Leaf or Terminal node.

- Pruning: When we remove sub-nodes of a decision node, this process is called pruning. We can say it as opposite process of splitting.

- Branch / Sub-Tree: A sub section of entire tree is called branch or sub-tree.

- Parent and Child Node: A node, which is divided into sub-nodes is called parent node of sub-nodes where as sub-nodes are the child of parent node.


## How does decision tree decide where to split?

- Decision trees use multiple algorithms to decide to split a node in two or more sub-nodes. 

- The creation of sub-nodes increases the homogeneity of resultant sub-nodes. In other words, we can say that purity of the node increases with respect to the target variable. 

- Decision tree splits the nodes on all available variables and then selects the split which results in most homogeneous sub-nodes.


## Advantages

- Easy to Understand: Decision tree output is very easy to understand even for people from non-analytical background. It does not require any statistical knowledge to read and interpret them. Its graphical representation is very intuitive and users can easily relate their hypothesis.

- Useful in Data exploration: Decision tree is one of the fastest way to identify most significant variables and relation between two or more variables. With the help of decision trees, we can create new variables / features that has better power to predict target variable. It can also be used in data exploration stage. For example, if we are working on a problem where we have information available in hundreds of variables, there decision tree will help to identify most significant variable.

- Less data cleaning required: It requires less data cleaning compared to some other modeling techniques. It is not influenced by outliers and missing values to a fair degree.

- Data type is not a constraint: It can handle both numerical and categorical variables.

- Non Parametric Method: Decision tree is considered to be a non-parametric method. This means that decision trees have no assumptions about the space distribution and the classifier structure.

## Disadvantages

- Over fitting: Over fitting is one of the most practical difficulty for decision tree models. This problem gets solved by setting constraints on model parameters and pruning.

- Not fit for continuous variables: While working with continuous numerical variables, decision tree looses information when it categorizes variables in different categories.
