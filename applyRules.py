import sandhi
import random

# Does this actually change the value?
def apply(rule, seq):
	for i in range(0,len(seq)):
		randNum = random.random()
		if randNum < sandhi.RULES[rule]: # will this work? will it interpret it as a string??
			rule(seq, i)

# This applies a different probability to every matching element in the sequence
# How will this scale??? I should do some BigOh notation...

