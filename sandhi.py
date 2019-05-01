
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

# VOWEL SANDHI RULES

# Dirgha Sandhi

def A1_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and (seq[i+1].equals(phonemeInv["a"]) or seq[i+1].equals(phonemeInv["aa"])):
        seq[i] = phonemeInv["aa"]
        seq[i+1] = phonemeInv["_"] # we're combining phonemes, so it results in a deletion...
        return True 
    else: 
        return False

def A2_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["i"]) or seq[i].equals(phonemeInv["ii"])) and (seq[i+1].equals(phonemeInv["i"]) or seq[i+1].equals(phonemeInv["ii"])):
        seq[i] = phonemeInv["ii"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def A3_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["u"]) or seq[i].equals(phonemeInv["uu"])) and (seq[i+1].equals(phonemeInv["u"]) or seq[i+1].equals(phonemeInv["uu"])):
        seq[i] = phonemeInv["uu"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def A4_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["r2"]) or seq[i].equals(phonemeInv["R"])) and (seq[i+1].equals(phonemeInv["r2"]) or seq[i+1].equals(phonemeInv["R"])):
        seq[i] = phonemeInv["R"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

# Guna Sandhi

def B1_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and (seq[i+1].equals(phonemeInv["i"]) or seq[i+1].equals(phonemeInv["ii"])):
        seq[i] = phonemeInv["e"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def B2_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and (seq[i+1].equals(phonemeInv["u"]) or seq[i+1].equals(phonemeInv["uu"])):
        seq[i] = phonemeInv["o"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def B3_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and (seq[i+1].equals(phonemeInv["r2"]) or seq[i+1].equals(phonemeInv["R"])):
        seq[i] = phonemeInv["a"]
        seq[i+1] = phonemeInv["r"] # This will be converted to a consonant now, yes?
        return True 
    else: 
        return False

def B4_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["l2"]):
        seq[i] = phonemeInv["a"]
        seq[i+1] = phonemeInv["l"]
        return True 
    else: 
        return False

# Vrddhi Sandhi

def C1_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel: 
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["e"]):
        seq[i] = phonemeInv["ai"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def C2_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["o"]):
        seq[i] = phonemeInv["au"]
        seq[i+1] = phonemeInv["_"]
        return True
    else: 
        return False

def C3_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["ai"]):
        seq[i] = phonemeInv["ai"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

def C4_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["a"]) or seq[i].equals(phonemeInv["aa"])) and seq[i+1].equals(phonemeInv["au"]):
        seq[i] = phonemeInv["au"]
        seq[i+1] = phonemeInv["_"]
        return True 
    else: 
        return False

# Yana Sandhi

# Describe - and justify - the probability that you'll apply to it
def D1_vow(seq, i):
    # I'd like to have the probability encoded into the function... but I think I might have to use global variables instead
    # Or a global probability dictionary
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["i"]) or seq[i].equals(phonemeInv["ii"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["y"]
        return True        
    else: 
        return False
    
def D2_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["u"]) or seq[i].equals(phonemeInv["uu"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["v"]
        return True
    else: 
        return False

def D3_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if (seq[i].equals(phonemeInv["r2"]) or seq[i].equals(phonemeInv["R"])) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["r"]
        return True
    else: 
        return False

def D4_vow(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if not seq[i].vowel or not seq[i+1].vowel:
        return False
    if seq[i].equals(phonemeInv["l2"]) and seq[i+1].equalsDifferentVowel(seq[i]):
        seq[i] = phonemeInv["l"]
        return True
    else: 
        return False

# Need the E's!!!




# Define the probability dictionary
RULES = {}
#RULES['T1'] = (1.0, T1) # lower because of potential word boundaries 
#RULES['T2'] = (1.0, T2)
RULES['A1_vow'] = (0.5, A1_vow)
RULES['A2_vow'] = (0.5, A2_vow)
RULES['A3_vow'] = (0.5, A3_vow)
RULES['A4_vow'] = (0.5, A4_vow)
RULES['B1_vow'] = (0.5, B1_vow)
RULES['B2_vow'] = (0.5, B2_vow)
RULES['B3_vow'] = (0.5, B3_vow)
RULES['B4_vow'] = (0.5, B4_vow)
RULES['C1_vow'] = (0.5, C1_vow)
RULES['C2_vow'] = (0.5, C2_vow)
RULES['C3_vow'] = (0.5, C3_vow)
RULES['C4_vow'] = (0.5, C4_vow)
RULES['D1_vow'] = (0.5, D1_vow)
RULES['D2_vow'] = (0.5, D2_vow)
RULES['D3_vow'] = (0.5, D3_vow)
RULES['D4_vow'] = (0.5, D4_vow)

#RULES['D2'] = (0.5, D2)

# for testing purposes, we can set all probabilities to 1



