import phonemicInventory
import sandhi
import random

with open('rigveda') as f:
    lines = f.readlines()

phonemeInv = phonemicInventory.phonemeInv

sequence = []
for l in lines:
	sequence.append(phonemicInventory.phonemeInv[l.strip()])

for s in sequence:
	#s.printPhoneme()
	print(s.vowel)

def D1(i):
    if i >= len(sequence) - 1 or i < 0:
        return
    if not sequence[i].vowel or not sequence[i+1].vowel:
    	return
    if (sequence[i].equals(phonemeInv["i"]) or sequence[i].equals(phonemeInv["ii"])) and sequence[i+1].equalsDifferentVowel(sequence[i]):
        sequence[i] = phonemeInv["y"]
        return 

def apply(rule, prob):
	for i in range(0,len(sequence)):
		randNum = random.random()
		if randNum < prob:
			rule(i)

apply(D1,0.5)


for s in sequence:
	print(s.orth)
