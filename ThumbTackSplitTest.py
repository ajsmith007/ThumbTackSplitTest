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
import scipy
import scipy.stats.stats
import numpy as np

########################################################################################
VERSION = "2013.10.29 demo"

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
    print "Results of the A/B Split Test\n"
    print "Data: "
    print data
    print"\n"
    
    # Compute the significance of the results using Chi-squared
    baseline = 0
    for test in range(1,len(data)):
        print "Variation #" + str(test)
        # Compute Chi-squared for each pair of baseline and test
        trials = np.array([data[baseline][1],data[test][1]])
        observed = np.array([data[baseline][0], data[test][0]])
        expected = np.array([0.5, 0.5]) * np.sum(observed)    # only true if you assume number of trials were equal between A and B tests
        #expected = np.array([(observed[baseline]/trials[baseline])*trials[baseline], (observed[baseline]/trials[baseline])*trials[1]])
        chiSq = scipy.stats.stats.chisquare(observed, expected)
        print "Observed: " + str(observed)
        print "Expected: " + str(expected)
        print "Trials: " + str(trials)
        print "ChiSq = " + str(chiSq[0]) 
        print "p-value = " + str(chiSq[1])
        if (chiSq[0] > 3.841) & (chiSq[1] < 0.05) : # Test for significance with 1 DOF at 95% confidence level
            print "This test is statistically significant at the 95% confidence level"
        else:
            print "This test is not statistically significant"
        print "\n"
    
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
