import sandhi
import random

# Does this actually change the value
def apply(rule, seq, prob):
	for i in range(0,len(seq)):
		randNum = random.random()
		if randNum < prob:
			rule(seq, i)
# This applies a different probability to every matching element in the sequence
# How will this scale??? I should do some BigOh notation...