## The Use of Amazon S3 and EC2 for Deploying Machine Learning Web Application to Predict Software Developer Salaries

[fullfiledeploy]: https://drive.google.com/file/d/1akC871lgTeqZpXq1UQMCrGDx_1okJ1Wm/view?usp=sharing

>[!NOTE]
**For a comprehensive analysis, please refer to this [Full Report][fullfiledeploy] document.**

### 1. Introduction

The propose of this experiment is to outline the steps involved in uploading the files into Amazon S3 bucket and deploying a machine learning web application using Streamlit on an Amazon EC2 (Elastic Compute Cloud) instance. Specifically, the web application focuses on predicting annual salaries for software developers and is hosted on an AWS server through an EC2 instance, making it accessible online via the internet.

Streamlit is a Python library that simplifies the process of building interactive web applications for machine learning and data science projects. 

Amazon S3, or Simple Storage Service, is a highly scalable and durable cloud storage service. It offers developers and businesses a secure and reliable way to store and retrieve any amount of data from anywhere on the web. 

Amazon EC2 instance provides the computational power and resources to support machine learning algorithms and web application. It offers customizable configurations, including instance types, storage options, and networking capabilities. 

### 2. Objective

To provide comprehensive detail methodology for efficiently storing files in Amazon S3 bucket and to explain the deployment process of a machine learning web application, developed using Streamlit on an Amazon EC2 instance. The primary focus of this web application is to predict annual salaries for software developers using machine learning model based on relevant factors. By leveraging the scalable storage capabilities of Amazon S3 and the processing power of EC2, the objective is to deliver a seamless and globally accessible online platform that assists to make informed compensation decisions.

### 3. Requirements

Requirements for deploying the machine learning web application on an Amazon EC2 instance includes as follows:

  - ‘app.py’, ‘explore_page.py’, and ‘predict_page.py’ files are the script that created the user interface for web application to handle user’s inputs and display the results or visualizations.
  - requirements.txt’ file is listed the specific libraries required by machine learning application to install across different environments.
  - ‘Salary_Prediction_Model.ipynb’ file is machine learning model for prediction.
  - ‘save_steps.pkl’ file refers to a serialized machine learning model saved using Python’s pickle library, which is used to store trained machine learning models in a compact manner.
  - survey_results_public.csv’ file is the dataset.

 ### 4. Data Source

 The dataset used in this experiment, is software developer annual survey in 2022 dataset that is publicly available online on Stackoverflow website for further analysis (https://insights.stackoverflow.com/survey). The dataset consists of 73268 rows and 79 columns in total.

 ### 5. Machine Learning Model

The machine learning model process for predicting software developer salaries.

 #### 5.1 Setting the environment

 #### 5.2 Data exploration
 
 To analyze the distribution of salary. In the dataset comprising 79 variables, the variables “Country”, “Edlevel” (education level), “YearCodePro” (years of experiences), and “ConvertedCompYearly” renamed to “Salary” have been chosen to focus for the analysis and training the machine learning models. 

 #### 5.3 Data preprocessing 
 
 The step of cleaning the dataset including removing missing values, outliers, and irrelevant variables from the dataset, and encode categorical variables.

 #### 5.4 Data splitting

   -	Feature or independent variables (X) is the feature used to train the predictive models based on the following feature “Country”, “EdLevel”, “YearsCodePro” and drop “Salary” from the dataset.
  -	Target or dependent variable (y) is set “Salary” column as the outcome for prediction.

#### 5.5 Model selection

To choose the most appropriate machine learning algorithm that is best fit and interpret the given data for salary prediction. Linear regression and Decision tree are considered to train for predictive models.

  - Linear Regression: It is the linear relationship between dependent variable (salary) and one or more independent variables. In salary prediction, it leverages features such as years of experiences, education level, and country to provide straightforward estimates.
  - Decision Tree: It is tree-like model that makes decision based on feature tests. For salary prediction, it can identify non-linear relationships, such as how specific combinations of country and education level impact salary, making it effective in situation with clear decision-making paths affecting wages.

#### 5.6 Model Evaluation

Root Mean Square Error (RMSE) provides a measure of the magnitude of the model’s prediction errors. It is used to measure the difference between values predicted by a model and the values observed. RMSE represents the sample standard deviation of the differences between predicted and observed values. A lower RMSE indicates a better fit of the model to the data, while a higher RMSE indicates a poorer fit. Additionally, RMSE has the same units as the dependent variable. The evaluation of models is provided as follows:

  -	Logistic Regression: RMSE value of $49370.57 suggests that on average, the model’s predictions deviate from the actual salaries by approximately $49370. Since logistic regression is typically used for classification tasks rather than regression. Therefore, using it for salary prediction might not be the most appropriate choice.
  -	Decision Tree: This model performs better than logistic regression with an RMSE of $38375.22. The prediction from decision tree model, on average, off by around $37375 from the actual salaries. This suggests that the decision tree has captured the underlying patterns in the data more accurately than logistic regression.

### 6. Save and Test the Model using Sample Set

The decision tree algorithm was selected as machine learning model for predicting the salary since the evaluation of performance using mean square error was the lowest compared to logistic regression algorithm. The prediction model was saved into ‘save_steps.pkl’ file using Pickle library that is used to save as a binary file that can be easily loaded and reused later.

### 7. Streamlit Web Application Development

Streamlit is used to develop the web application for predicting software developer salaries. The files ‘app.py’, ‘explore_page.py’, and ‘predict_page.py’ were created to define the layout of the web application to process user inputs and provide the prediction result based on trained machined learning model. 

### 8. Amazon S3 Bucket

All the requirement files (or objects) were uploaded on Amazon S3 bucket.

### 9. Amazon EC2 Instance

Aftr uploaded all the files in S3 bucket, created an EC2 instance to deploy a web application through EC2 instance. 


