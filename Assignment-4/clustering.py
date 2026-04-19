"""clustering.py: Starter file for assignment on Clustering """

__author__ = "Put your full name here"


# Data Manipulation and Visualization
import pandas as pd #creating and manipulating dataframes
import matplotlib.pyplot as plt #visuals
import seaborn as sns #visuals
from sklearn.cluster import KMeans #K-Means
from sklearn.cluster import DBSCAN #DBSCAN
import numpy as np
from sklearn.metrics import confusion_matrix
'''
Github Username: 
PSID:
'''

# Reading the data
data = pd.read_csv('data/clinical_records_dataset.csv')
class_labels = data['DEATH_EVENT']
data = data.drop('DEATH_EVENT', axis=1)
data = data.drop('time', axis=1)

''' Modify this method '''
def purity(y_true,y_pred):

    """
    Compute the purity score for clustering.

    Parameters:
    y_true (array-like): True class labels.
    y_pred (array-like): Predicted cluster labels.

    Returns:
    float: Purity score, a single number
    """
    contingency_matrix = confusion_matrix(y_true, y_pred)

    # Using amax to compute the number of data points assigned to the correct label, based on the contingency matrix
    correct = 

    # Find the total number of data points
    ndata =
      

    return correct/ndata

''' Write your code here '''
