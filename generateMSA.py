import phonemicInventory
import sandhi
import random
from datetime import datetime
import copy 
import pandas as pd
import numpy
import collections
import sys


# How will this scale??? I should do some BigOh notation..

# Probabilisticly apply a rule
def apply(ruleName, seq):#, index):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        randNum = random.random()
        if randNum < sandhi.RULES[ruleName][0]: # The probability of rule application
            success = rule(seq, i)
            if success:
                ruleFile.write("Application of " + ruleName + " @ position " + str(i) + "\n")
                count += 1
    return count

# Apply a rule with 100% probability (for control purposes)
def applyControl(ruleName, seq):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        success = rule(seq, i)
        if success:
            count += 1
    return count

# Open files for logging
ruleFile = open("rulefile.txt","w") # For logging rule application
statFile = open("stats.txt","w") # For logging run stats
seqFile = open("sequences.txt","w")
entropyFile = open("shannonEntropies.txt","w")
binaryFile = open("binaryRep.txt", "w")
inputFile = open("rigveda_short", "r")

# Read in the input data file
lines = inputFile.readlines()

# Define the phonemic inventory
phonemeInv = phonemicInventory.phonemeInv

# Define the multiple sequence alignment structure
MSA = []

# Generate the replicates
#numReplicates = 15 # This will eventually be 1500, but for the sake of testing, far fewer
numReplicates = int(sys.argv[1])
for i in range(0,numReplicates):
    sequence = []
    for l in lines:
        sequence.append(phonemicInventory.phonemeInv[l.strip()])
    MSA.append(sequence)
sequenceLength = len(sequence)

# Define additional data strutcures, including the MSA to be altered 
MSAControl = copy.deepcopy(MSA)
MSABinary = []

# Establish count arrays for analytics
stats = {}
statsControl = {} # If all the rule application probabilities are 1
for key in sandhi.RULES.keys():
    stats[key] = 0
    statsControl[key] = 0

startTime = datetime.now()
refSequence = MSA[0] # The first sequence in the MSA is the reference sequence

# Apply rules to every element in the MSA (except the reference sequence)
for s in MSAControl[1:]: 
    for key in sandhi.RULES.keys():
        appliedControl = applyControl(key, s)
        statsControl[key] += appliedControl

# Apply rules probabilistically to each sequence in the MSA, except the reference;
# Print rule application results to rule file, and runtime stats to stat file
count = 1
for s in MSA[1:]: 
    ruleFile.write("Sequence #" + str(count) + "\n")
    for key in sandhi.RULES.keys():
        applied = apply(key, s)
        stats[key] += applied
    count += 1
statFile.write("Time: " + str(datetime.now() - startTime) + "\n")

# Write final sequences to sequence file, for later perusal and populate the binary matrix
i = 0 # Because we're starting with the reference sequence here
for s in MSA:
    j = 0
    MSABinary.append([])
    #seqFile.write("Sequence #" + str(count) + "\n")
    for b in s:
        seqFile.write(b.orth + " ")
        if (b.orth) == (refSequence[j].orth):
            MSABinary[i].append(0)
        else:
            MSABinary[i].append(1)
        j += 1
    seqFile.write("\n")
    i += 1

# Output binary MSA to binary file
for s in MSABinary:
    for b in s:
        binaryFile.write(str(b) + " ")
    binaryFile.write("\n")

# Compute and print application ratios
for key in sandhi.RULES.keys():
    if statsControl[key] == 0:
        ratio = 0
    else:
        ratio = stats[key]/statsControl[key]
    statFile.write(key + ": " + str(ratio) + "\n")

#Close logging files
ruleFile.close()
statFile.close()
seqFile.close()
binaryFile.close()
inputFile.close()

# Calculate positional Shannon entropy for the MSA 
#MSA_analyze = pd.read_csv("sample.txt", sep=' ', header=None)
MSA_analyze = pd.read_csv("sequences.txt", sep=' ', header=None)
# There's sure to be a more elegant way to do this, without the intermediate output file...
# It should be an "in-house" data structure of sorts.
cols = list(MSA_analyze) # This gives me the indices of the columns
denom = numReplicates
shannonEntropy = []

# Calculate the shannon entropy of each column
for c in cols:
    v = MSA_analyze.iloc[:,c].value_counts()
    entropy = 0
    for p in v:
        entropy += (p / denom) * numpy.log(p)
    entropy *= -1
    shannonEntropy.append(entropy)
    # The end of the file always has a trailing NaN: dispose of it
    if str(MSA_analyze.iloc[0,c]) != "nan":
        entropyFile.write(str(MSA_analyze.iloc[0,c]) + ": " + str(entropy) + "\n")

entropyFile.close()

# I have to do some sort of analysis for this... some visualization I guess... not sure what though. Maybe Sid can help me with R?
# So, for this analysis, we have the following values: 
# N is the length of the string (53, for the short rigveda... I should probably make it smaller)
# q is the number of possible alphabets
# 

# Generate .p file for analysis
aceFile = open("ace.p", "w")
q = phonemicInventory.alphabetSize
alphabet = phonemicInventory.allPhonemes
#alphabet = ['n','m','aa','ai','s','q','v']
B = numReplicates
N = sequenceLength
# Okay I already have the shannon entropy, so, that's good

probs = [] # This is the overall data set
for c in cols:
    probs_oneLetter = {} # This is going to be a dictionary of probabilities by letter
    alph_subset = copy.deepcopy(alphabet)
    #print(alph_subset)
    valueCounts = MSA_analyze.iloc[:,c].value_counts()
    #print(valueCounts)
    for i in range(0,valueCounts.size): 
        orth = valueCounts.index[i]
        alph_subset.remove(orth)
        probs_oneLetter[orth] = valueCounts[i]/B # This is where we calculate the probability that a given spot in the sequence takes on specific alphabet values
    for alph in alph_subset:
        probs_oneLetter[alph] = 0.0
    probs_sorted = collections.OrderedDict(sorted(probs_oneLetter.items()))
    probs.append(probs_sorted)

# Okay I've supes gotta check this...

# Now, print out these values:
for probs_oneLetter in probs:
    for alphabetOption in probs_oneLetter:
        #aceFile.write(alphabetOption + ": " + str(probs_oneLetter[alphabetOption]) + '\t')
        aceFile.write(str(probs_oneLetter[alphabetOption]) + '\t')
    aceFile.write('\n')

aceFile.close()


# probs = [] 
# for c in cols:
#     p_1letter = {}
#     for alph in alphabet:
#         p_1letter[alph] = []
#     valueCounts = MSA_analyze.iloc[:,c].value_counts()
#     #print(valueCounts)
#     for alph in alphabet:
#         #print(alph)
#         if alph in valueCounts:
#             orth = valueCounts.index[0]
#             p_1letter[orth].append(valueCounts[0]/B) # This is where we calculate the probability that a given spot in the sequence takes on specific alphabet values
#         else:
#             p_1letter[alph].append(0)
#     probs.append(p_1letter)

# # Okay I've supes gotta check this...

# # Now, print out these values:
# for p in probs:
#     for q in p:
#         aceFile.write(str(p[q]) + '\t')
#     aceFile.write('\n')

# aceFile.close()
