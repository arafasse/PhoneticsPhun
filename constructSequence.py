import phonemicInventory

with open('rigveda') as f:
    lines = f.readlines()

sequence = []
for l in lines:
	sequence.append(phonemicInventory.phonemeInv[l.strip()])

for s in sequence:
	#s.printPhoneme()
	print(s.vowel)