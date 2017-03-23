#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

max_bonus = 0
name = ''

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]

    if bonus > max_bonus:
        max_bonus = bonus
        name = point[2]
    
    if (float(bonus) > 5000000.0) and (float(salary) > 1000000.0):
        print 'Name: %s - bonus: %s - salary: %s' % (point[2], bonus, salary)

    matplotlib.pyplot.scatter( salary, bonus )

print 'Max bonus name: %s' % name

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



