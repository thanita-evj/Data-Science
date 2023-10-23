## Master Thesis: Development of A Clustering Algorithm for Customer Segmentation (Hybrid DBK-Means Algorithm)

[thesisreport]: https://drive.google.com/file/d/1yJH8h5PZeIz7-jC3Ta8iq4yigI7dSwVr/view?usp=sharing

[thesispaper]: https://drive.google.com/file/d/1u-UkXu_BITWIKMxV18zjseE58xik60gH/view?usp=sharing

**(Note: For a comprehensive analysis, please refer to this [Full Master Thesis Report][thesisreport] or [Master Thesis Research Paper][thesispaper] Documents)**

[thesispresent]: https://drive.google.com/file/d/1VPMSSxNwDCyeA4Rj4DSJkFjhi91oRezi/view?usp=sharing

**Presentation:** [Master Thesis Presentation][thesispresent]

### 1. Abstract

This study used clustering algorithms to apply to customer segmentation to define groups of bank customer based on similar characteristics. There are two main contributions that aims to increase the clustering performance results while maintaining the insights of customers. First, a hybrid algorithm is proposed by combining DBSCAN and K-means called hybrid DBK-means.  Second, clustering algorithms for K-means, Hierarchical, Density-Based Spatial Clustering of Applications with Noise (DBSCAN) and novel hybrid DBK-means, are incorporated with two different dimensional reduction techniques: feature importance and Principal Component Analysis (PCA). Normalized dataset of credit card customers was applied and evaluated using Silhouette coefficient and Calinski-Harabasz index. Results showed that incorporating with feature importance specifically with K-means, Hierarchical, and hybrid DBK-means, led to more distinct clusters and improving performance. PCA also improved cluster cohesion but was less effective than feature importance. Hybrid DBK-means algorithm improved in term of lower dissimilarity within cluster and better isolation between clusters compared to other algorithms and maintained the strength of DBSCAN in detecting of anomaly and outliers.

### 2. Introduction

Clustering algorithms have become vital in many fields, including customer segmentation to identify relationships within data. Clustering algorithms are categorized into partitioning, hierarchical, density-based, grid-based, and model-based clustering algorithms. However, the conventional algorithms struggle with high-dimensional data common in online behavior tracking. To address this issue, dimensional reduction techniques are applied to reduce feature numbers while retaining critical information. There are various methods for dimensional reduction exist, such as feature selection, linear (e.g., PCA), and non-linear techniques. Therefore, this research aims to further develop the conventional clustering algorithm and explore and evaluate the use of dimensional reduction techniques with various clustering algorithms to achieve robust cluster results, leading to better customer understanding and segmentation.

### 3. Overview of Hybrid Clustering Algorithm

To overcome limitation of individual clustering algorithms and robust its performance results, these clustering algorithms are incorporated as multiple clustering techniques to maximize the strength of various approaches called hybrid algorithm. 

### 4. Overview of Clustering Algorithms with Dimensional Reduction

Combining clustering algorithms with dimensional reduction techniques provides an effective solution for managing high-dimensional data, boosting cluster quality, and simpler interpretation of cluster results. 

### 5. Methodology

The experiment makes two main contributions to develop the clustering algorithm for customer segmentation. 

- The first contribution involves proposing new hybrid clustering algorithm combining the strength of DBSCAN and K-means called hybrid DBK-means, to leverage its individual algorithm.
- The second contribution is integrating clustering algorithms consisting of K-means, hierarchical, DBSCAN, and proposed hybrid DBK-means with dimensional reduction techniques, specifically feature importance and principal component analysis (PCA).

The implementation of clustering algorithms and methodology proceeds as shown in Fig. 1. 


