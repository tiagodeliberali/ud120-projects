#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

feature_names = vectorizer.get_feature_names()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

print 'training score: %s: ' % clf.score(features_train, labels_train)
print 'test score: %s: ' % clf.score(features_test, labels_test)

importanceList = clf.feature_importances_

outliers_features = list()
max_val = 0
max_i = 0

for i, val in enumerate(importanceList):
    if (max_val < val):
        max_val = val
        max_i = i
    if (float(val) > 0.2):
        outliers_features.append((i, val))

print 'Max val: %s - max i: %s - feature name: %s' % (max_val, max_i, feature_names[max_i])

for outlier in outliers_features:
    print 'Value: %s - Position: %s - Feature: %s' % (outlier[1], outlier[0], feature_names[outlier[0]])