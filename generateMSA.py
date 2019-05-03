import phonemicInventory
import sandhi
#import applyRules
import random
from datetime import datetime

logfile = open("logfile.txt","w")
outputfile = open("sequences.txt","w")

# Establish count array for analytics
stats = {}
statsControl = {} # If all the probs are 1
for key in sandhi.RULES.keys():
    stats[key] = 0
    statsControl[key] = 0

# Does this actually change the value?
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

def applyControl(ruleName, seq):
    count = 0
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        success = rule(seq, i)
        if success:
            count += 1
    return count

# This applies a different probability to every matching element in the sequence
# How will this scale??? I should do some BigOh notation...

with open('rigveda') as f:
    lines = f.readlines()

phonemeInv = phonemicInventory.phonemeInv

MSA = []
numReplicates = 10000 # This will eventually be 1500, but for the sake of testing, much less

# Generate the replicates
for i in range(0,numReplicates):
	sequence = []
	for l in lines:
		sequence.append(phonemicInventory.phonemeInv[l.strip()])
	MSA.append(sequence)

# Check to make sure it worked
#for a in MSA:
#    for b in a:
#    	print(b.orth,end='') # This end parameter only works with Python 3
#    print("\n")

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

for key in sandhi.RULES.keys():
    ratio = stats[key]/statsControl[key]
    outputfile.write(key + ": " + str(ratio) + "\n")

logfile.close()
outputfile.close()