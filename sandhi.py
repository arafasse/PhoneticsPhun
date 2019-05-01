
import phonemicInventory

sequence = []
sequence.append(phonemicInventory.phonemeInv["b"])
sequence.append(phonemicInventory.phonemeInv["i"])
sequence.append(phonemicInventory.phonemeInv["i"])


print(sequence[1].orth)
print(sequence[2].equalsDifferentVowel(sequence[1]))

# have a separate function that computes \"different vowel\" etc\n",

phonemeInv = phonemicInventory.phonemeInv

# Define the probability dictionary
RULES = {}
RULES['C1'] = 0.2 # lower because of potential word boundaries 
RULES['D1'] = 0.5
RULES['D2'] = 0.5


# Vowel rules (excerpted) 

def C1(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["e"]):
        seq[i] = phonemeInv["ai"]
        return 

# ooooh it applied it before M... is that right??
# Describe what this does
# Describe - and justify - the probability that you'll apply to it
def D1(seq, i):
    # I'd like to have the probability encoded into the function... but I think I might have to use global variables instead
    # Or a global probability dictionary
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if (seq[i].equals(phonemeInv["i"]) or seq[i].equals(phonemeInv["ii"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["y"]
        return        
    
def D2(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if (seq[i].equals(phonemeInv["u"]) or seq[i].equals(phonemeInv["uu"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["v"]
        return



    
#D1(1)
#print(sequence[1].orth)

# Consonant rules: 



