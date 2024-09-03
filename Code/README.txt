Final Project Code Description, AIT 726
Author: Japneet Kohli

****************************************************************************************************
Problem : Translator Writer Classification for Shri Guru Granth Sahib Ji
Solutions Implemented: Naive Bayes, Logistic Regression, bi-LSTM Recurrent Neural Network
****************************************************************************************************

****************************************************************************************************
Data : Shri Guru Granth Sahib Ji Corpus obtained from Shabad OS API. 
Dataset Size: 121,020 rows
Labels: Dr. Sant Singh Khalsa	60,510
	Bhai Manmohan Singh	60,510
****************************************************************************************************

****************************************************************************************************
Please execute files in the following order: 
****************************************************************************************************

1. JSONtoCSVConversion.py [Converts JSON files to CSV]
2. ReadCSVToDF [Converts Multiple CSV files to singular CSV file with only required attributes]
3. FinalProjectNaiveBayes.ipynb [Naive Bayes Model]
4. FinalProjectLogisticRegression.ipynb [Logistic Regression Model]
5. FinalProjectNeuralNetwork.ipynb [bi-LSTM RNN Model]

****************************************************************************************************
Model							F1 Score
****************************************************************************************************
Naïve Bayes						91.98%
Logistic Regression					91.96%
Bi- LSTM						91.75%

****************************************************************************************************
Order of Model Implementation for Naive bayes and Logistic Regression Models
****************************************************************************************************

1.   Load data.
2.   Select only translation writer and line translations data from the list of attributes.
3.   Assign labels of translation writer attribute binary numeric values (0,1).
4.   Preprocess text using regex.
5.   Split data into train, validation, and test.
6.   Create pipeline with functions including (Multinomial Naive Bayes OR Logistic Regression), Count Vectorizer, and TF-IDF Transformer, and assign range of hyerparameters to be tuned.
7.   Perform 10 fold cross validation using GridSearchCV to find best values for hyperparameters. 
8.   Fit the model with the tuned parameters on training data.
9.   Predict values for validation and test data and compute accuracy using classfication report and confusion matrix.

****************************************************************************************************
Order of Model Implementation for Bi-LSTM Recurrent Neural Network Model
****************************************************************************************************

1.   Load data.
2.   Select only translation writer and line translations data from the list of attributes.
3.   Preprocess text using regex.
5.   Use label encoder to assign numeric values to the categeorical labels of the translator writer.
6.   Split data into train and test.
7.   Toeknize words and pad sentences to convert words into vectors.
7.   Use GloVe pretrained word embeddings to create embedding matrix.
8.   Define bi-lstm  model with embedding layer, lstm layer and output layer.
9.   Compile and fit model.
10.  Predict values for test data and compute accuracy.
