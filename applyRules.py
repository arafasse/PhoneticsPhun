import sandhi
import random

logfile = open("logfile.txt","w+")

# Does this actually change the value?
def apply(ruleName, seq):
	rule = sandhi.RULES[ruleName][1]
	for i in range(0,len(seq)):
		randNum = random.random()
		if randNum < sandhi.RULES[ruleName][0]: # will this work? will it interpret it as a string??
			logfile.write("Application of " + ruleName + " @ position " + i + "\n")
			rule(seq, i)

logfile.close()

# This applies a different probability to every matching element in the sequence
# How will this scale??? I should do some BigOh notation...

