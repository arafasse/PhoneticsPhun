
import phonemicInventory

sequence = []
sequence.append(phonemicInventory.phonemeInv["b"])
sequence.append(phonemicInventory.phonemeInv["i"])
sequence.append(phonemicInventory.phonemeInv["i"])


print(sequence[1].orth)
print(sequence[2].equalsDifferentVowel(sequence[1]))

# have a separate function that computes \"different vowel\" etc\n",

phonemeInv = phonemicInventory.phonemeInv

def D1(i):
    if i >= len(sequence) - 1 or i < 0:
        return
    if (sequence[i].equals(phonemeInv["i"]) or sequence[i].equals(phonemeInv["ii"])) and sequence[i+1].equalsDifferentVowel(sequence[i]):
        sequence[i] = phonemeInv["y"]
        return        
    
def D2(i):
    if i >= len(sequence) - 1 or i < 0:
        return
    if (sequence[i].equals(phonemeInv["u"]) or sequence[i].equals(phonemeInv["uu"])) and sequence[i+1].equalsDifferentVowel(sequence[i]):
        sequence[i] = phonemeInv["v"]
        return
    
D1(1)
print(sequence[1].orth)


