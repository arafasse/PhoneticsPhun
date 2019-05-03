import phonemicInventory
import sandhi
#import applyRules
import random
from datetime import datetime

logfile = open("logfile.txt","w")

# Does this actually change the value?
def apply(ruleName, seq):
    rule = sandhi.RULES[ruleName][1]
    for i in range(0,len(seq)):
        randNum = random.random()
        if randNum < sandhi.RULES[ruleName][0]: # will this work? will it interpret it as a string??
            success = rule(seq, i)
            if success:
                logfile.write("Application of " + ruleName + " @ position " + str(i) + "\n")


# This applies a different probability to every matching element in the sequence
# How will this scale??? I should do some BigOh notation...

with open('rigveda') as f:
    lines = f.readlines()

phonemeInv = phonemicInventory.phonemeInv

MSA = []
numReplicates = 1500 # This will eventually be 1500, but for the sake of testing, much less

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

# Apply the function to each sequence
#for s in MSA:
# 	applyRules.apply(sandhi.D1,s)

# Apply ALL functions to ALL sequences

startTime = datetime.now()
count = 1
for s in MSA:
    logfile.write("Sequence #" + str(count) + "\n")
    for key in sandhi.RULES.keys():
        apply(key, s) 
    count += 1
logfile.write("Time: " + str(datetime.now() - startTime))
# Check to make sure there are changes
#for a in MSA:
#    for b in a:
#        print(b.orth,end='') # This end parameter only works with Python 3
#    print("\n")


logfile.close()