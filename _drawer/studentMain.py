#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
import Classifiers as cl

import numpy as np
import pylab as pl

def printData(name, clf):
    ### draw the decision boundary with the text points overlaid
    prettyPicture(clf, features_test, labels_test, name)
    #output_image(name, "png", open(name, "rb").read())

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#printData("GaussianNB.png", cl.classifyGaussianNB(features_train, labels_train))

#printData("classifySVC_rbf_1.png", cl.classifySVC(features_train, labels_train, 'rbf', 1.0))
#printData("classifySVC_rbf_1000.png", cl.classifySVC(features_train, labels_train, 'rbf', 1000.0))

#printData("classifySVC_linear_1.png", cl.classifySVC(features_train, labels_train, 'linear', 1.0))
#printData("classifySVC_linear_1000.png", cl.classifySVC(features_train, labels_train, 'linear', 1000.0))

#printData("classifyDecisionTree_40.png", cl.classifyDecisionTree(features_train, labels_train, 40))

#printData("classifyKNeighborsClassifier_3.png", cl.classifyKNeighborsClassifier(features_train, labels_train, 3))
#printData("classifyKNeighborsClassifier_10.png", cl.classifyKNeighborsClassifier(features_train, labels_train, 10))
#printData("classifyKNeighborsClassifier_50.png", cl.classifyKNeighborsClassifier(features_train, labels_train, 50))

#printData("classifyAdaBoostClassifier_50.png", cl.classifyAdaBoostClassifier(features_train, labels_train, 50))
#printData("classifyAdaBoostClassifier_250.png", cl.classifyAdaBoostClassifier(features_train, labels_train, 250))
#printData("classifyAdaBoostClassifier_500.png", cl.classifyAdaBoostClassifier(features_train, labels_train, 500))

printData("classifyKNeighborsClassifier_1.png", cl.classifyKNeighborsClassifier(features_train, labels_train, 1))

