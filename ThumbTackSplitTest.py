#!/usr/bin/env python

'''
########################################################################################
ThumbTackSplitTest.py

   Python code to read ThumbTackSplitTestResults.csv and compute the success of a Split Test

__author__ = "Drew Smith"
__version__ = "0.7"
__status__ = "Demonstration"
__copyright__ = Copyright 2013, Andrew J Smith. All Rights Reserved."

Created on: Oct 29, 2013
 
########################################################################################
'''
import sys
import csv
import datetime
from scipy import stats
import numpy as np

########################################################################################
VERSION = "2013.10.29"

def main():
    # Read results of the Split Test from csv file
    with open('ThumbTackSplitTest.csv', 'rb') as file:
        results = csv.reader(file, delimiter=",")
        rows = list(results)
        data = np.zeros(shape=[5,2])
        i = 0
        skipFirstLine = True
        for row in rows:
            if skipFirstLine:   #skip header line
                skipFirstLine = False
                continue
            data[i] = [float(row[1]), float(row[2])]
            i += 1
    print data
    
    # Compute the significance of the results using Chi-squared
    observed = []
    expected = []
    chi2 = []
    baseline = 0
    for test in range(1,len(data)):
        print "Test #" + str(test)
        # Compute Chi-squared for each pair of baseline and test
        observed = np.array([data[baseline][0], data[test][0]])
        expected = np.array([0.5, 0.5]) * np.sum(observed)
        chi2 = stats.chisquare(observed, expected)
        
        print observed
        print expected
        print chi2
    
########################################################################################
# Main
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print "[*] Usage: python ThumbTackSplitTest.py"
    print "Starting ThumbTack Split Test Analysis on: " + datetime.datetime.now().ctime() + "\n"
    print "ThumbTackSplitTest Version: " + VERSION
    print "NumPy Version: " + np.version.version
    print "SciPy Version: " + scipy.version.version + "\n"
    main()
