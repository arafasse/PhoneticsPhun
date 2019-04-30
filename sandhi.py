
import phonemicInventory

sequence = []
sequence.append(phonemicInventory.phonemeInv["b"])
sequence.append(phonemicInventory.phonemeInv["i"])
sequence.append(phonemicInventory.phonemeInv["o"])

print(sequence[1].orth)

# have a separate function that computes \"different vowel\" etc\n",

phonemeInv = phonemicInventory.phonemeInv

# take care of corner cases!\n",
def D1(i):
    if sequence[i].equals(phonemeInv["i"]) or sequence[i].equals(phonemeInv["ii"]) and sequence[i+1].equals(phonemeInv["o"]):
            sequence[i] = phonemeInv["y"]

D1(1)

print(sequence[1].orth)