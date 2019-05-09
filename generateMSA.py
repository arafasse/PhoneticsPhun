import phonemicInventory
import sandhi
import random
from datetime import datetime
import copy 
import pandas as pd
import numpy

# How will this scale??? I should do some BigOh notation..

# Open files for logging
logfile = open("logfile.txt","w")
outputfile1 = open("sequences.txt","w")
outputfile2 = open("sequences4analysis.txt","w")
outputfile3 = open("shannonEntropies.txt","w")

# Read in the input data file
with open('rigveda') as f:
    lines = f.readlines()

# Define the phonemic inventory
phonemeInv = phonemicInventory.phonemeInv

MSA = []
numReplicates = 1500 # This will eventually be 1500, but for the sake of testing, much less

# Generate the replicates
for i in range(0,numReplicates):
    sequence = []
    for l in lines:
        sequence.append(phonemicInventory.phonemeInv[l.strip()])
    MSA.append(sequence)

MSAControl = copy.deepcopy(MSA)
MSABinary = []

# Establish count arrays for analytics
stats = {}
statsControl = {} # If all the rule application probabilities are 1

for key in sandhi.RULES.keys():
    stats[key] = 0
    statsControl[key] = 0

# Probabilistic apply a rule
def apply(ruleName, seq, index):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        randNum = random.random()
        if randNum < sandhi.RULES[ruleName][0]: # will this work? will it interpret it as a string??
            success = rule(seq, i)
            if success:
                logfile.write("Application of " + ruleName + " @ position " + str(i) + "\n")
                MSAControl[index].append(1)
                count += 1
            else:
                MSAControl[index].append(0)
    return count

# Apply a rule with 100% probability
def applyControl(ruleName, seq):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        success = rule(seq, i)
        if success:
            count += 1
    return count

# Apply ALL functions to ALL sequences
# shouldn't I save one at the beginning, to be the reference sequence?
startTime = datetime.now()

for s in MSAControl[1:]: # apply to all but the first
    for key in sandhi.RULES.keys():
        appliedControl = applyControl(key, s)
        statsControl[key] += appliedControl

count = 1
index = 0
for s in MSA[1:]: # apply to all but the first
    MSAControl.append([])
    logfile.write("Sequence #" + str(count) + "\n")
    for key in sandhi.RULES.keys():
        applied = apply(key, s, index) 
        stats[key] += applied
    count += 1
logfile.write("Time: " + str(datetime.now() - startTime))

# Write sequences to output file
count = 0 # because we're starting with the ref sequence here
for s in MSA:
    outputfile1.write("Sequence #" + str(count) + "\n")
    for b in s:
        outputfile1.write(b.orth) 
        outputfile2.write(b.orth + " ")
    outputfile1.write("\n")
    outputfile2.write("\n")
    count += 1

# Compute and print application rations
for key in sandhi.RULES.keys():
    if statsControl[key] == 0:
        ratio = 0
    else:
        ratio = stats[key]/statsControl[key]
    outputfile1.write(key + ": " + str(ratio) + "\n")

#Close logging files
logfile.close()
outputfile1.close()
outputfile2.close()


# Calculate positional Shannon entropy for the MSA 
MSA = pd.read_csv("sequences4analysis.txt", sep=' ', header=None)
# There's sure to be a more elegant way to do this, without the intermediate output file...
# we'll keep this in an "in-house" data structure of sorts.
cols = list(MSA)
denom = numReplicates
shannonEntropy = []

# Calculate the shannon entropy of each column
for c in cols:
    q = MSA.iloc[:,c].value_counts()
    entropy = 0
    for p in q:
        entropy += (p / denom) * numpy.log(p)
    entropy *= -1
    shannonEntropy.append(entropy)
    # The end of the file always has a trailing NaN: dispose of it
    if str(MSA.iloc[0,c]) != "nan":
        outputfile3.write(str(MSA.iloc[0,c]) + ": " + str(entropy) + "\n")

#MSA.T.squeeze()
#counts = MSA.value_counts()
#MSA.count()
#series1=MSA.iloc[0,:]
#counts = series1.value_counts()

#This is all getting quite messy... I need to go back and fix it eventually.



