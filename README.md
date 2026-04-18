Dataset 2 - Dry Beans -- Dry_Bean_Dataset.csv
Dataset Description: The dataset for this assignment is adapted from the paper Multiclass classification of dry beans using computer vision and machine learning techniquesLinks to an external site. by Koklu et. al. in which the authors evaluate the capabilities of several machine learning models in classifying the varieties of beans based on the output of an image segmentation algorithm that receives images of dry beans and produces a segmentation mask. Features were then extracted from the segmented images that pertain to the size, shape, and structure of each bean. The dataset contains 13,611 instances belonging to 7 different varieties, which are listed below.

Dataset Preprocessing: The dataset remains identical to the original, only with class labels encoded as numerical values in the Class column rather than the original string format. The original class column is left for reference as Class_String. Additionally, the four Shape Factor columns are dropped.

Attributes

The dataset contains:

[Class_String]:: Original text-based class labels
[Class]: Class labels for each bean
Barbunya: 0
Bombay: 1
Cali: 2
Dermosan: 3
Horoz: 4
Seker: 5
Sira: 6
12 feature columns:
Area: The area of a bean zone and the number of pixels within its boundaries.
Perimeter: Bean circumference; the length of its border.
MajorAxisLength: The distance between the ends of the longest line that can be drawn from a bean.
MinorAxisLength: The longest line that can be drawn from the bean while standing perpendicular to the main axis.
AspectRation: Defines the relationship between the Major and Minor Axis Lengths.
Eccentricity: Eccentricity of the ellipse having the same moments as the region.
ConvexArea: Number of pixels in the smallest convex polygon that can contain the area of a bean seed.
EquivDiameter: The diameter of a circle having the same area as a bean seed area.
Extent: The ratio of the pixels in the bounding box to the bean area.
Solidity: Also known as convexity. The ratio of the pixels in the convex shell to those found in beans.
roundness: Calculated with the following formula: (4piA)/(P^2)
Compactness: Measures the roundness of an object: (Equivalent Diameter / Major Axis Length).

Assignment Tasks

Task 1

A. Using all attributes, build a Decision Tree model to predict bean varieties: Train the Decision Tree model using the given maximum depths (3, 7, 11, 15). 10 points

B. Perform 5-fold cross-validation for each of the 4 max depths and compute accuracy (mean of validation scores), precision and recall. Generate a table, as given below, for the obtained results. 5 points

Decision Tree Experiments

Max Depths	Accuracy	Precision	Recall
3			
7			
11			
15			
C. Explain how the tree size/depth affects model performance in the context of overfitting/underfitting. 3 points

D. Explain the meaning of the difference in accuracy, precision and recall scores in relation to the task; only if there is a significant difference. 2 points

Task 2

A. Using all attributes, build a k-nn classifier to predict bean varieties: Train the k-nn using the given neighbors (3, 9, 17, 25). 10 points

B. Perform 5-fold cross-validation for each of the 4 neighbor size and compute accuracy (mean of validation scores), precision and recall. Generate a table, as given below, for the obtained results. 5 points

K-NN Experiments

Neighbors	Accuracy	Precision	Recall
3			
9			
17			
25			
C. Explain how the number of neighbors affects model performance in the context of overfitting/underfitting. 3 points

D. Explain the meaning of the difference in accuracy, precision and recall scores in relation to the task; only if there is a significant difference. 2 points

Task 3

A. Using all attributes, build an SVM Model to predict bean varieties: Train the SVM model using the given kernel functions (linear, polynomial, rbf, sigmoid). 10 points

B. Perform 5-fold cross-validation for each of the 4 kernel functions and compute accuracy (mean of validation scores), precision and recall. Generate a table, as given below, for the obtained results. 5 points

SVM Experiments

Kernel Function	Accuracy	Precision	Recall
Linear			
Polynomial			
RBF			
Sigmoid			
C. Discuss the impact of different kernels on model performance. 3 points

D. Explain the meaning of the difference in accuracy, precision and recall scores in relation to the task. 2 points

Task 4 Interpretation 5 points

Interpret the tables you generated in tasks 1B, 2B, 3B; compare the performance of the Decision Tree, K-NN and SVM models.
Which model performs better? Why do you think that is the case?
What would you recommend to further improve each model’s performance?
