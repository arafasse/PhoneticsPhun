
import phonemicInventory

sequence = []
sequence.append(phonemicInventory.phonemeInv["b"])
sequence.append(phonemicInventory.phonemeInv["i"])
sequence.append(phonemicInventory.phonemeInv["i"])


print(sequence[1].orth)
print(sequence[2].equalsDifferentVowel(sequence[1]))

# have a separate function that computes \"different vowel\" etc\n",

phonemeInv = phonemicInventory.phonemeInv

# no I actually don't want a class because I don't need any instances of rules...
# I just need a probability dictionary, like I was thinking before... 
# but I would like to have the data structures coincide somehow... 

    
    #def printPhoneme(self):
    #    print(self._orth)



# ****** Test Rules ******
def T1(seq, i):
    if i >= len(seq)  or i < 0:
        return
    if not seq[i].vowel: #or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["i"]): #or seq[i].equals(phonemeInv["b"])) and seq[i+1].equals(phonemeInv["e"]):
        seq[i] = phonemeInv["*"]
        return 

def T2(seq, i):
    if i >= len(seq) or i < 0:
        return
    if not seq[i].vowel: #or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["a"]): #or seq[i].equals(phonemeInv["b"])) and seq[i+1].equals(phonemeInv["e"]):
        seq[i] = phonemeInv["*"]
        return 

# Vowel Sandhi Rules

def C1(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel: 
        return
    if seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["e"]):
        seq[i] = phonemeInv["ai"]
        return 

def C2(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["o"]):
        seq[i] = phonemeInv["au"]
        return 

def C3(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["ai"]):
        seq[i] = phonemeInv["ai"]
        return 

def C4(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["au"]):
        seq[i] = phonemeInv["au"]
        return 

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

def D3(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if (seq[i].equals(phonemeInv["r2"]) or seq[i].equals(phonemeInv["R"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["r"]
        return

def D4(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return
    if not seq[i].vowel or not seq[i+1].vowel:
        return
    if seq[i].equals(phonemeInv["l2"]) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["l"]
        return





# Define the probability dictionary
RULES = {}
RULES['T1'] = (1.0, T1) # lower because of potential word boundaries 
RULES['T2'] = (1.0, T2)
#RULES['D2'] = (0.5, D2)

# for testing purposes, we can set all probabilities to 1



