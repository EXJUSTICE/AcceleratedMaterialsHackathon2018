
# -*- coding: utf-8 -*-
"""
Code for AMDNUSWorkshop
Datanames is the same as the standard dataset given

For our approach The inputs are voltage, temperature
output/labels are current

Three methods used here. Suppor vector machine regression
Bayesian Ridge,
And traditional linear regression in 3D.

No SGD or other methods used due to lack of time to tune methods

@author: Adrian Yijie Xu
"""

import numpy as np
import pandas as pd

import time  
from sklearn.metrics import accuracy_score
import numpy as np  
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.signal import savgol_filter
from scipy.signal import find_peaks_cwt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import warnings
from sklearn import linear_model
from sklearn import svm

warnings.filterwarnings('ignore')


"""
Define some classifiers, we will use regressors here for continuous prediction
"""

classifiers = [
    svm.SVR(),
    linear_model.BayesianRidge(),
    linear_model.LinearRegression()]

#import into datafRame
data_df = pd.read_csv("C:/Users/Adrian/datanames.csv")

#Print to make sure we are all good
#print(data_df)

# Select only data where current value is bigger than 0.1 mA
# df_new = data_df[data_df.J >= 0.0001]
# print(df_new)

#Select only V & T for input dataset

inputs =data_df[['V','T']].copy()

inputsshuf= inputs
inputsshuf = inputsshuf.drop (inputsshuf.index[0])

outputs =data_df[['J']].copy()

outputsshuf=outputs
outputsshuf = outputsshuf.drop (outputsshuf.index[0])

predictData = ([[2.4,400]])


for item in classifiers:
    print(item)
    clf = item
    clf.fit(inputsshuf, outputsshuf)
    print(clf.predict(predictData),'\n')
    
print ("Finished")
    
