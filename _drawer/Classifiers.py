from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def classifyGaussianNB(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    clf = GaussianNB()
    clf_fit = clf.fit(features_train, labels_train)
    
    return clf_fit
	
def classifySVC(features_train, labels_train, kernel_name, c_value):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    clf = SVC(kernel=kernel_name, C=c_value)
    clf_fit = clf.fit(features_train, labels_train)
    
    return clf_fit
	
def classifyDecisionTree(features_train, labels_train, samples):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    clf = DecisionTreeClassifier(min_samples_split=samples)
    clf_fit = clf.fit(features_train, labels_train)
    
    return clf_fit