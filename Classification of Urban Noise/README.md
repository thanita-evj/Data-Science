## Classification of Urban Environmental Noise on Sound Characteristics using KNN, Decision Tree, and CNN Algorithms

[noisereport]: https://drive.google.com/file/d/1WmVBzGJ6nfmYshNn3TXATC0wZpfun846/view?usp=sharing

[noisepresent]: https://drive.google.com/file/d/1GjOCgHzMxerWW4zwjl6Ugwe1y0KmPok8/view?usp=sharing

>[!NOTE]
**For a comprehensive analysis, please refer to the [Full Report][noisereport] and [Presentation][noisepresent] Documents**

### 1. Introduction

The rapid expansion of urban areas has given rise to an increase in environmental noise levels, which has significant implications for the well-being of individuals. As a result, urban sound classification has emerged as a crucial area of research. The goal of this project is to develop a sound classification system using the UrbanSound8K dataset, which was obtained from Kaggle. To achieve this objective, we will utilize the librosa library to extract relevant sound features. Furthermore, we will employ various classification algorithms, including the K-Nearest Neighbors (KNN) algorithm with different distance metrics such as Cosine, Chebyshev, and Euclidean distances, as well as the Random Forest algorithm and Convolutional Neural Network (CNN). Our main aim is to evaluate the accuracy and effectiveness of these algorithms in accurately classifying urban sounds. By doing so, we aim to make valuable contributions to the field of urban sound classification, enhance our understanding of the acoustic characteristics of urban environments, and improve the quality of urban sound analysis and management.

### 2. Shortcoming of Work Implementation

1) Choise of classifier
2) Parameter tuning
3) Evaluation metrics
4) Lack of cross-validation

### 3. Project Contribution

1) KNN when n = 5.
2) Using different classifiers inclusing Random Forest and CNN.

### 4. Methodology

#### 4.1 Dataset

The dataset used in this study is the UrbanSound8K dataset, which was publicly accessed from Kaggle website (https://www.kaggle.com/code/prabhavsingh/urbansound8k-classification/notebook). Dataset consists of 8732 observations (rows) and 8 variables (columns).

#### 4.2 Feature Extraction

Feature extraction is the process of extracting relevant information from raw data to use as inputs to machine learning algorithms. For sound classification, it involves the process of converting raw audio data into a set of identifiers that used to distinguish between different types of sounds. 

#### 4.3 Data Transformation

Data transformation refers to the process of modifying the format, structure, or values within a dataset to prepare it for machine learning. In this experiment, we used the LabelEncoder from scikit-learn to convert categorical variables into numerical values. 

#### 4.4 Preparation of Training and Testing Datasets

The training and testing datasets are prepared as follows: the independent variable (X) consists of the feature vectors extracted from the audio files, and the dependent variable (y) represents the labeled class for each feature vector. The data is split into an 80% training set and a 20% testing set, ensuring an adequate amount of data for model training and evaluation.

#### 4.5 Machine Learning for Classification

- K-Nearest Neighbors (KNN): a type of instance-based learning that assumes that similar data points are in proximity to each other. The algorithm classifies a data point based on the majority class of its k nearest neighbors. In this experiment, we set k = 5, which means that the class label of a data point is determined by the majority vote of its 5 nearest neighbors.
- Random Forest: is an ensemble learning method that constructs multiple decision trees and outputs the class that is the mode of the classes predicted by individual trees. In this experiment, we set the number of trees to 100 based on our trials.
- Convolutional Neural Network (CNN): is a type of neural network designed to work with data that has a grid-like topology, such as images or time-series data. The network consists of multiple layers, including Convolutional, MaxPooling, Flatten, Dense, and Dropout layers. The model is trained on the extracted features and can learn to identify patterns that are useful for classification. In this project, we apply the CNN algorithm to classify the audio data.

### 5. Results

#### 5.1 Accuracy

The results shown in Figure 1 indicates that the models produced different prediction accuracy. The results of the existing research study perform in KNN with n = 1, 2, 3 and the new study on KNN with n = 5 and new model of CNN and Random Forest. 

•	KNN with Euclidean distance, the prediction accuracy is 78.13% for n=1, 76.88% for n=2, 74.38% for n=3, and 81.34% for n=5.

•	KNN with Cosine distance, the prediction accuracy is 85% for n=1, 81.88% for n=2, 83.13% for n=3, and 84.43% for n=5.

•	KNN with Chebyshev distance, the prediction accuracy is 85% for n=1, 81.88% for n=2, 83.13% for n=3, and 84.43% for n=5.

•	CNN and Random Forest (RF) achieved prediction accuracy of 75.56% and 73.78%, respectively.


#### 5.2 Confusion Matrix

A confusion matrix for a multi-class classification is used to provide an idea of the distribution of prediction accuracy for each sound or class. In confusion matrix, each row corresponds to a true class and each column corresponds to a predicted class. The diagonal elements of the matrix represent instances where the model’s predictions match the actual classes meaning that where the model’s predictions are correct. The off-diagonal elements represent instances where the model’s predictions are incorrect. By examining the values in each row of the confusion matrix, it shows the true instances of each class were distributed across the predicted classes.

To analyze the results of confusion matrix, if a particular row of the confusion matrix has a high value on the diagonal indicating correct predictions for that class and low values elsewhere, this suggests that the model is accurately predicting that class. In contrast, if a row has low values on the diagonal and high values elsewhere, this suggests that the model is often incorrectly predicting that class.

### 6. Conclusion

In a study comparing machine learning models for sound classification, KNN using the Cosine distance metric outperformed other models, with KNN (n = 1) from a previous study achieving 85% accuracy and our KNN (n = 5) reaching 84.43% accuracy, while more complex models like CNN and Random Forest yielded lower accuracies of 75.56% and 73.78%, respectively. Despite the implementation of more complex models like CNN and Random Forest, the simpler KNN with n = 1 and 5 outperformed our proposed models. This suggests that for this specific task, KNN model using Cosine distance metric may be the most effective model for this urban sound dataset, possibly due to its ability to capture the small differences in the data that are important for accuracy classification.


