# ECG-Classification
ECG analysis to predict arrhythmia using the MIT-BIH arrhythmia data set.

This project, with the help of VMD reduces noise, and uses beat features(4): i. Mean ii. Standard Deviation iii. Skewness iv. Kurtosis

to classify the beats.

The Data set is very uneven as the number of anomalies is very less compared to the amount of normal heart beats. This project uses SMOTE Transformer to tranform the data to have all the different types of datas to be of the same numbers.

This project uses python to read multiple ecg data files which have its own labels on what sort of arrhythmia the beat has. Analysising each beat, The project will use 4 different machine learning algorithms: i. Decision Tree ii. Random Forest iii. Histogram Gradient Boosting Classifier iv. SVM

producing the F1 score, Precisoon, Recall and its Confusion MAtrix.
