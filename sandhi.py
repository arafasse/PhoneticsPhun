
import phonemicInventory

sequence = []
sequence.append(phonemicInventory.phonemeInv["b"])
sequence.append(phonemicInventory.phonemeInv["i"])
sequence.append(phonemicInventory.phonemeInv["i"])


print(sequence[1].orth)
print(sequence[2].equalsDifferentVowel(sequence[1]))

# have a separate function that computes \"different vowel\" etc\n",

phonemeInv = phonemicInventory.phonemeInv


# this needs to act on a specific sequence...
# Vowel rules (excerpted) 

# Actually, I want this to apply to the entire sequence... so maybe I should define a helper function? 


# ooooh it applied it before M... is that right??

def D1(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if (seq[i].equals(phonemeInv["i"]) or seq[i].equals(phonemeInv["ii"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["y"]
        return        
    
def D2(i):
    if i >= len(sequence) - 1 or i < 0:
        return
    if (sequence[i].equals(phonemeInv["u"]) or sequence[i].equals(phonemeInv["uu"])) and sequence[i+1].equalsDifferentVowel(sequence[i]):
        sequence[i] = phonemeInv["v"]
        return
    
#D1(1)
#print(sequence[1].orth)

# Consonant rules: 



