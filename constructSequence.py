import phonemicInventory
import sandhi
import random

with open('rigveda') as f:
    lines = f.readlines()

phonemeInv = phonemicInventory.phonemeInv


MSA = []
numReplicates = 5 # This will eventually be 1500, but for the sake of testing, much less

# Generate the replicates
for i in range(0,numReplicates):
	sequence = []
	for l in lines:
		sequence.append(phonemicInventory.phonemeInv[l.strip()])
	MSA.append(sequence)

# Check to make sure it worked
for a in MSA:
    for b in a:
    	print(b.orth,end='') # This end parameter only works with Python 3
    print("\n")

#for s in sequence:
	#s.printPhoneme()
#	print(s.vowel)

def apply(rule, prob):
	for i in range(0,len(sequence)):
		randNum = random.random()
		if randNum < prob:
			rule(i)

# Apply the function to each 
for s in MSA:
 	apply(sandhi.D1,0.5)

# Check to make sure there are changes
for a in MSA:
    for b in a:
    	print(b.orth,end='') # This end parameter only works with Python 3
    print("\n")


#apply(D1,0.5)


#for s in sequence:
#	print(s.orth)
