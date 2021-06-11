# EMNIST Dataset Optical Character Recognition (OCR) with Classification Algorithms
Diego Wahl

# Abstract
This project sought to create a robust, functional multiclass classification model to interpret handwritten characters and classify them as their appropriate alphanumeric character. We sought to minimize the run time, while maintaining a high level of accuracy, requiring care in both model selection and careful consideration of feature 'engineering'.

# Design
In practice, a functional classification model to read writing must be able to provide predictions rapidly, and, to a lesser extent, be trained in a reasonable amount of time. To help satisfy both of those conditions, it was decided that the dataset would undergo some sort of feature selection or dimensionality reduction strategy to greatly speed up both prediction and training time. Two approaches were focused on; a mutual information (MI) feature selection approach (using SKLearn's native mutual info package), and a principle component analysis (PCA) dimensionality reduction approach. Both approaches provide a mechanism by which the most "important" predictive features of the data can be identified and ranked, allowing the modeling to go forward with just those limited features without entirely losing its predictive ability.

# Data
The data used in this project is the (relatively) well-know EMNIST dataset. EMNIST is an expanded version of the (perhaps more famous) MNIST dataset (both provided by, unsurprisingly, NIST). These data consist of 814,255 handwritten characters, belonging to 62 unbalanced classes. The classes themselves correspond to the alphanumeric characters; 0-9, a-z, and A-Z. Each digit comes as a 28x28 black-and-white image, with each pixel value being a measure of brightness of that pixel. 

# Algorithms
A variety of models were tested on both dimensionality reduction approaches (MI and PCA) with a varying amount of component features. Additionally, a baseline Random Forest model was trained with the entirety of the dataset and features in order to get a 'ballpark' accuracy score to aim for with the reduced dataset (82% mean accuracy with a 5-fold cross validation scheme). It was found that for both MI and PCA the most succesful model, in general, was a Random Forest model, outclassing Decision Trees and Logistic Regression in both accuracy and run time, and XGBoost in run time. Between the two reduction approaches additionally, it was found that PCA not only in general has a better accuracy per number of components, but also 'caps out' in accuracy at a much lower number of components (at around 20 features, in our analysis). Thus it was decided that a Random Forest PCA model with 20 features would be the final model to be used for hyperparameter tuning. In all, the final model was found to hit about 77% accuracy on the test set, though it should be noted that due to memory limitations the model could not be trained on the enetirety of the training set as intended (capping out at about 200,000 training images). 

# Relevant Tools
* SKLearn for variety of packages (including PCA, MI, and models)
* Matplotlib and Seaborn for visualization

# Communication
Findings of this project were presented to Metis cohort. 