import phonemicInventory
import sandhi
import random
from datetime import datetime

# How will this scale??? I should do some BigOh notation..

# Open files for logging
logfile = open("logfile.txt","w")
outputfile = open("sequences.txt","w")


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

# Establish count arrays for analytics
stats = {}
statsControl = {} # If all the rule application probabilities are 1

for key in sandhi.RULES.keys():
    stats[key] = 0
    statsControl[key] = 0

# Probabilistic apply a rule
def apply(ruleName, seq):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        randNum = random.random()
        if randNum < sandhi.RULES[ruleName][0]: # will this work? will it interpret it as a string??
            success = rule(seq, i)
            if success:
                logfile.write("Application of " + ruleName + " @ position " + str(i) + "\n")
                count += 1
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
startTime = datetime.now()
count = 1
for s in MSA:
    logfile.write("Sequence #" + str(count) + "\n")
    for key in sandhi.RULES.keys():
        applied = apply(key, s) 
        appliedControl = applyControl(key, s)
        stats[key] += applied
        statsControl[key] += appliedControl
    count += 1
logfile.write("Time: " + str(datetime.now() - startTime))

# Write sequences to output file
count = 1
for s in MSA:
    outputfile.write("Sequence #" + str(count) + "\n")
    for b in s:
        outputfile.write(b.orth) 
    outputfile.write("\n")
    count += 1

# Compute and print application rations
for key in sandhi.RULES.keys():
    ratio = stats[key]/statsControl[key]
    outputfile.write(key + ": " + str(ratio) + "\n")

#Close logging files
logfile.close()
outputfile.close()