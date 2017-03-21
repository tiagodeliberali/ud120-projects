#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

total_payments = 0
total = 0

for key, v in enron_data.items():
    #if v['poi']:
    if v['total_payments'] == 'NaN':
        total_payments = total_payments + 1
    total = total + 1
        
print 'total_payments: %s / total: %s' % (total_payments + 10, total + 10)

