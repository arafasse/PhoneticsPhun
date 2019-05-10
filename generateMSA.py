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
outputfile4 = open("binaryRep.txt", "w")

# Read in the input data file
with open('rigveda_short') as f:
    lines = f.readlines()

# Define the phonemic inventory
phonemeInv = phonemicInventory.phonemeInv

MSA = []
numReplicates = 15 # This will eventually be 1500, but for the sake of testing, much less

# Generate the replicates
for i in range(0,numReplicates):
    sequence = []
    for l in lines:
        sequence.append(phonemicInventory.phonemeInv[l.strip()])
    MSA.append(sequence)

#sequenceLength = len(sequence)
#print(sequenceLength)

MSAControl = copy.deepcopy(MSA)
MSABinary = []

# Establish count arrays for analytics
stats = {}
statsControl = {} # If all the rule application probabilities are 1

for key in sandhi.RULES.keys():
    stats[key] = 0
    statsControl[key] = 0

# Probabilistic apply a rule
def apply(ruleName, seq):#, index):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    #binaryRep = []
    for i in range(0,len(seq)):
        randNum = random.random()
        if randNum < sandhi.RULES[ruleName][0]: # will this work? will it interpret it as a string??
            success = rule(seq, i)
            if success:
                logfile.write("Application of " + ruleName + " @ position " + str(i) + "\n")
                #binaryRep.append(1)
                count += 1
            #else:
                #binaryRep.append(0)
    #MSABinary.append(binaryRep)
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
baseSequence = MSA[0]
for b in baseSequence:
    print(b.orth, end="")

for s in MSAControl[1:]: # apply to all but the first
    for key in sandhi.RULES.keys():
        appliedControl = applyControl(key, s)
        statsControl[key] += appliedControl

count = 1
#index = 1 #maybe this should be 1... this requires a rather massive clean-up
#MSABinary.append([0] * sequenceLength)
for s in MSA[1:]: # apply to all but the first
    MSAControl.append([])
    logfile.write("Sequence #" + str(count) + "\n")
    for key in sandhi.RULES.keys():
        applied = apply(key, s)#, index) 
        stats[key] += applied
    count += 1
#    index += 1
logfile.write("Time: " + str(datetime.now() - startTime))

# Write sequences to output file
count = 0 # because we're starting with the ref sequence here
for s in MSA:
    index = 0
    MSABinary.append([])
    outputfile1.write("Sequence #" + str(count) + "\n")
    for b in s:
        outputfile1.write(b.orth) 
        outputfile2.write(b.orth + " ")
        print(b.orth)
        print(baseSequence[index].orth)
        if (b.orth) == (baseSequence[index].orth):
            MSABinary[count].append(0)
        else:
            MSABinary[count].append(1)
        index += 1
    outputfile1.write("\n")
    outputfile2.write("\n")
    count += 1

for s in MSABinary:
    for b in s:
        outputfile4.write(str(b) + " ")
    outputfile4.write("\n")

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
outputfile4.close()


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

outputfile3.close()

#MSA.T.squeeze()
#counts = MSA.value_counts()
#MSA.count()
#series1=MSA.iloc[0,:]
#counts = series1.value_counts()

#This is all getting quite messy... I need to go back and fix it eventually.



