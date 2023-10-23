## Predicting Databel Customer Churn using Machine Learning Models

[fullfilechurn]: https://drive.google.com/file/d/1wQ37a4mK6Oa1XssYXgb-bmaUX8z_T1ip/view?usp=sharing

>[!NOTE]
**For a comprehensive analysis, please refer to this [Full Report][fullfilechurn] document**

### 1. Introduction

In today’s high business competition, customer retention is more importance than ever. The loss of customers, commonly referred to as “Customer Churn”, becomes significant challenges for businesses, both in terms of lost revenue and increased marketing costs associated with acquiring new customers. Predicting and understanding the reasons behind churn can help implementing targeted strategies that increase customer satisfaction and loyalty.

In this way, machine learning becomes an invaluable tool with the ability to process large amounts of data and identify complex patterns. Machine learning models can predict potential churners with a level of accuracy. This project delves deep into the customer churn prediction based on Databel’s dataset, employing various machine learning models including Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), and XGBoost for the classification.

### 2. Definition of "Churn"

According to Investopedia, the Churn Rate, also known as the rate of attrition or customer churn, is the rate at which customer stop doing business with an entity. It is commonly expressed as the percentage of service subscribers who discontinue their subscriptions within a given period.

The churn rate formula is the number of customers lost during the period divided by total number of customers. Churn rate is commonly expressed as a percentage used to evaluate the retention success and potential growth or decline of a business’s customer base. A high churn rate may indicate customer dissatisfaction, while a low rate suggests customers are satisfied and remain loyal to the product or service. Minimizing the churn rate is crucial for sustained growth and profitability.

Churn Analysis is the process of evaluating and understanding the reasons and patterns behind customer choosing to end their relationship with a company or service over a specific period. Churn analysis is including:

  - Descriptive analytics: It is used to understand the current churn rate and profile of churned customers.
  - Predictive analytics: It is used to apply machine learning models to predict potential churn based on customer behavior and characteristics.
  - Prescriptive analytics: It is used to recommend specific actions to prevent or reduce churn.

### 3. Objective

The objective of conducting customer churn prediction is to proactively identify customers who are most likely to discontinue using company’s products or services in the near future, enabling businesses to implement targeted retention strategies. This predictive approach allows business to maximize customer lifetime value, optimize resource allocation, and increase overall profitability by focusing on maintaining existing customer relationships rather than solely investing in acquiring new ones. Through understanding and addressing specific reasons leading customer churn, business aims to improve customer satisfaction, loyalty, and long-term revenue generation.

### 4. Setting the Environment

### 5. Data Exploration (Exploratory Data Analysis)

#### 5.1 Overview of dataset

The dataset used in this project is a fictional churn dataset from a Telecom provider named Databel, the dataset consists of 29 columns or variables and 6687 rows of customer records with no time dimension. 

#### 5.2 Duplicate row

This dataset has no duplicate rows, ensuring that the subsequent prediction is based on unique customer records.

#### 5.3 Missing values

Missing values were identified specifically in “Churn Category” and “Churn Reason” columns. Both columns show the same count of 4918 missing entries. Recognizing missing values in dataset is an important step to ensure the precision of subsequent analysis and prediction, as missing information can potentially skew results.

#### 5.4 Remove redundant variables

The column “Customer ID”, “Phone Number”, and “Churn Reason” were excluded from the original dataset to enhance the efficacy of the modeling process. “Churn Reason” column comprises of unique textual reasons, which can introduce unnecessary complexity to the model. By omitting these columns, it aims to focus on features that directly contribute to a more efficient predictive analysis.

#### 5.5 Outlier detection

The highest percentage of outliers are in “Number of Customers in Group”, “Extra International Charges”, “Intl Calls”, and “Intl Mins”, all with percentages exceeding 15% considering high percentage of outliers that outright removal can lead to a substantial loss of data. For churn prediction, understanding the behavior of outliers can be crucial. Sometimes, outliers might represent high-value customers or those with specific needs. Instead of deleting the outliers, considering applying scaling and using algorithms that are less sensitive to outliers might be the better option for this project.

#### 5.6 Univariate analysis (Descriptive statistics)

Univariate analysis focuses on examining a single data variable. Since it's a single variable, it doesn’t deal with causes or relationships. The main purpose of univariate analysis is to describe the data and find patterns that exist within it.

#### 5.7 Bivariate analysis (Correlation analysis)

Bivariate analysis is a statistical method that used to determine the relationship between two variables such as correlation or scatter plot, studying whether a relationship exist and how strong it may be for a pair of data. 

### 6. Data Preprocessing

#### 6.1 Encoding categorical variables

Encoding is the process of converting categorical variables into a unique numeric format that can be provided to machine learning algorithms to improve predictions. 

#### 6.2 Feature scaling (Standardization)

Feature scaling is used to standardize the range of independent variables in the dataset. 

#### 6.3 Feature Selection

Feature selection is the process of selecting the most important features from the original set of features in a dataset to improve model performance, overfitting, and simplify models for better interpretation. This project applied feature importance using Random Forest classifier. 

“Churn Category” has the most important feature value close to 0.6. However, churn category is directly related to the target variable “Churn Label” as it provides the cause for the churn, then it is not appropriate to include in the model training process, it would leak information about the target into the model. In the practice, it would not have access to the reason for churn before predicting whether a customer will churn or not. Therefore, it is recommended to remove it from the feature used to train the model.

### 7. Independent and Dependent Variables

X is the independent variables by dropping columns “Churn Label”, “Churn Category”, “Local Calls”, “Number of Customers in Group”, and “Intl Mins”, leaving the remaining columns as the features to be used for training and prediction.

y is set to “Churn Label” column, which represents the target (dependent variable) or outcome for prediction.

### 8. Imbalanced Data

#### 8.1 Imbalanced Data

Imbalanced data refers to a situation in classification where the number of observations for one class significantly exceeds the number of observations for the other classes, representing unequal classification. 

Here is the distribution of churn label in the dataset about 73% of the samples belong to “0” class (customer who did not churn) and remaining 27% of the samples belong to “1” class (customer who did churn). The ratio of 73:27 represents imbalanced data where the class label “0” is the majority class making up three-quarter of dataset, while the class label “1” is the minority class.

#### 8.2 Resampling Technique

Since the dataset is highly imbalanced and most of machine learning algorithms work best when the number of samples in each class are about equal. Synthetic Minority Over-sampling Technique (SMOTE) is used in this project for resampling method to balance dataset with uneven class distributions. SMOTE works by generating new, synthetic samples of the minority class. After applying SMOTE, the class is balanced with 50% or 4891 of samples belong to “0” class and another 50% belong to “1” class.

### 9. Data Splitting

Data splitting using “train_test_split” function, is to split the data into training and testing sets for assessing the performance of machine learning models accurately. Training set is used to train the machine learning models, it is the largest portion of the dataset where the model learns patterns and relationships in the data. Testing set is the smaller portion of the data used for evaluating the model’s performance after training. The dataset in this project is divided using ratio of 70:20 for training and testing sets.

### 10. Model Selection, Traning, and Evaluation

#### 10.1 Model Selection

This project applies five different machine learning algorithms for prediction as described below:

-	Logistic Regression: It is used for modeling the probability of a binary outcome based on one or more predictive variables. For churn prediction, it would model the probability of a customer churn or not.
-	Decision Tree: It breaks down a dataset into smaller subsets, making a decision at every level forming a tree-like model. For churn prediction, the tree would split customers based on the features.
-	Random Forest: It is an ensemble method that builds multiple decision trees or a forest of decision trees. Each tree is trained on a random subset of the data and makes its own predictions. The Random Forest aggregates these predictions to produce a final result, which makes it more robust and often has higher accuracy than a single decision tree.
-	Support Vector Machine (SVM): It tries to find a hyperplane that best divides a dataset into classes (churning or non-churning).
-	eXtreme Gradient Boosting (XGBoost): It is an ensemble method and implementation of gradient boosting trees algorithm, but instead of fitting multiple trees in parallel like Random Forest, it builds one tree at a time, where each tree corrects the errors of the previous one.

#### 10.2 Training the model

#### 10.3 Model evaluation

#### 10.3.1 Accuracy

Accuracy is the ratio of correctly predicted instances to the total instances to provide how well the model is performing. XGBoost (0.92) and Random Forest (0.91) have outperformed other models indicating their ability to capture complex relationships in the data. There is not a large gap between the highest (XGBoost) and lowest (SVM) accuracies, suggesting that the data is relatively good, and most models can capture its underlying patterns. 

#### 10.3.2 Confusion matrix

Confusion matrix is used to evaluate the performance of a classification model by presenting the actual and predicted classification. In churn prediction, minimizing False Negative (FN) is crucial due to the association with revenue implication. At the same time, False Positive (FP) should be focused to ensure that retention resources are utilized effectively. 

XGBoost and Random Forest stands out as the most efficient models showing strong True Positive (TP) and True Negative (TN) values, indicating the effectiveness of churners and non-churners. In term of minimizing misclassifications, Logistic Regression and Decision Tree have balanced results, but they do not outshine Random Forest and XGBoost.

A representation of precision and recall for the fived evaluated models. It shows that XGBoost has the highest precision at 0.92, meaning that the model is right about 92% of the time when it says a customer will churn. It suggests that XGBoost is the best among other models at making correct positive prediction. Furthermore, XGBoost and Decision Tree have almost the same recall at about 0.91, spotting 91% of the customers who churn correctly. They are better than other models at identifying all potential positive instances.

#### 10.3.3 ROC Curve

ROC curve is used to evaluate the performance of a binary classification model. The curve helps to show the model’s capability to distinguish between the positive and negative classes. 

A curve that is closer to the top-left corner (0,1) of the plot indicates a better performing model and a curve that is closer to the random guessing line indicates a less effective model.

Area Under Curve (AUC) is the overall ability of the model to differentiate between the positive and negative classes. The higher value of AUC is the better on classification with less random guessing.

The result shows that XGBoost and Random Forest are the standout performers with their ROC curves close to the top-left corner and high AUC values at about 0.98 and 0.97, respectively.

### 11. Conclusion

In an attempt to predict and understand customer churn, this project has gone through from data collection to analytics. This project has identified key variables influencing churn, addressed challenges such as imbalanced dataset, and employed a variety of machine learning models to evaluate prediction accuracy. Through the model evaluations, the models have provided both reliability and interpretability, especially XGBoost and Random Forest, which outperformed and more robust in term of accuracy (about 92%) and correctness compared to Logistic Regression, Decision Tree, and Support Vector Machine.





