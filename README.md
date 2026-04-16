Task 1: Imputing and Encoding [35 points]

Goal of this task is to learn how to do some minor clean up and processing of data, specifically using encoding to deal with categorical variables. 
For this task, we will use the Titanic dataset. This data comes from a Kaggle competition (https://www.kaggle.com/competitions/titanic/overview)
Links to an external site. Dataset -- train.csv

Variable    	Definition    	                                         Key
survival    	Survival    	                                      0 = No, 1 = Yes
pclass        Ticket class    	                                  1 = 1st, 2 = 2nd, 3 = 3rd
sex        	  Sex    	 
Age        	  Age in years  	 
sibsp        	# of siblings / spouses aboard the Titanic    	 
parch        	# of parents / children aboard the Titanic    	 
ticket        Ticket number    	 
fare        	Passenger fare    	 
cabin        	Cabin number    	 
embarked    	Port of Embarkation    	                             C = Cherbourg, Q = Queenstown, S = Southampton

Variable Notes pclass: A proxy for socio-economic status (SES) 1st = Upper 2nd = Middle 3rd = Lower
age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
sibsp: The dataset defines family relations in this way… Sibling = brother, sister, stepbrother, stepsister Spouse = husband, wife (mistresses and fiancés were ignored)
parch: The dataset defines family relations in this way… Parent = mother, father Child = daughter, son, stepdaughter, stepson Some children travelled only with a nanny, therefore parch=0 for them.

Your tasks

1. Use the features ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"] for training with "Survival" as the label that you are trying to predict. There are some missing values in these features (see code stub), your first task is to choose how to handle them. I have shown two methods. Explain the pros and cons of choosing each method [ 10 points]
2. Use One Hot Encoding to change categorical variables to numerical values. I have done this for imputed data. Complete the exercise for imputed data and repeat for data with missing values removed. What are the other options available for encoding? Explain why OHE is good or not good for this exercise [ 10 points]
3. Divide data into training and test datasets. Use Random Forest algorithm to obtain a classifier (you can use sklearn methods). What are the hyper parameters you can use for Random Forest? Which ones did you choose to use, why? Plot the confusion matrix for your results on the test dataset. Explain your results [15 points]

If you are keen, you can try to apply your model to the test.csv data from the Kaggle competition (this does not contain the labels). Upload it and see how your model does in the leaderboard.  

Task 2: Naive Bayes and Logistic Regression [30 points]

For this task, let's use the Iris dataset. You can get it from sklearn.datasets (see notebook)

1. Use Gaussian Naive Bayes to build a classifier for the Iris dataset.  Don't forget to split data into train and test methods. Create a confusion matrix to check the accuracy of your classifier. Analyse the results and give your opinion of whether we have a good classifier or not [8 points]
2. There is code provided in the given notebook that shows how to extract the mean and variance values for each attribute and plot the Gaussian distribution associated with each class. Use it (may need to modify) to plot the Gaussian distributions for each class. Interpret the plots? [7 points]
3. Build a classifier using scikit learn's logistic regression for the same dataset. Create a confusion matrix for the logistic regression classifier and analyze the results. [8 points]
4. sklearn logistic regression has a predict_proba method that gives the probability of each sample belonging to each class. Use the plotting code provided (may need to modify). Interpret the plot [7 points]

Task 3: Neural Networks [35 points]

We will use the digits data for this exercise. You can download from Scikit Learn (see notebook). 

1. Write a MLP classifier to predice the digits. Remember to split into test and train datasets. Fix the activation function to ReLU. Use cross validation to determine the best number of layers and number of neurons per layers. There are infinitely many combinations possible, try increasing from 1 to 5 layers, and try between 32 to 256 neurons per layer. Each layer can have a different set of neurons. Print the accuracies [15 points]
2. Fix the architecture (number of layers and number of neurons) at what you determined was best in step 1. Choose 4 different activation functions and use cross validation to determine the best activation function [10 points]
3. Comment on your strategy in handling the large number of combinations of hyper parameters possible [10 points]
4. Extra credit: Build a convolutional neural network for this classification. Does it improve the accuracy? Why might a CNN be better suited for this problem? [10 points]

Code stub: COSC3337HW3Classification2_stub.ipynb
