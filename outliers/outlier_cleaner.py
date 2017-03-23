#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    def calcError(pred, val): return (pred - val)**2 
    errors = map(calcError, predictions, net_worths)

    removeSize = int(len(predictions) * 0.9)

    topErrors = sorted(errors)[0:removeSize]

    for i in range(len(predictions)):
        if errors[i] in topErrors:
            cleaned_data.append((ages[i][0], net_worths[i][0], errors[i][0]))

    print 'test!!!'
    
    return cleaned_data

