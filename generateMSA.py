import phonemicInventory
import sandhi
import applyRules

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


# Apply the function to each 
for s in MSA:
 	applyRules.apply(sandhi.D1,s,0.5)

# Check to make sure there are changes
for a in MSA:
    for b in a:
    	print(b.orth,end='') # This end parameter only works with Python 3
    print("\n")


#apply(D1,0.5)


#for s in sequence:
#	print(s.orth)
