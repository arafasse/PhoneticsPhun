
import phonemicInventory as pinv
import random

phonemeInv = pinv.phonemeInv

# Test Rules 
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

def D1_vow(seq, i):
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

# CONSONANT SANDHI RULES

def A1_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].voiced and not seq[i+1].voiced:
        seq[i] = pinv.Consonant.voiced2unvoiced(seq[i])
        return True
    else:
        return False

def B1_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    # Will this throw a recursion error?
    if seq[i].vowel: #or not seq[i+1].consonant:  this is causing difficulties...
        return False
    if not seq[i].voiced and (seq[i+1].voiced or seq[i+1].vowel):
        seq[i] = pinv.unvoiced2voiced(seq[i])
        return True
    else:
        return False

def D1_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].PoA == pinv.DENTAL and seq[i+1].PoA == pinv.PALATAL:
        seq[i] = pinv.Consonant.dental2palatal(seq[i])
        return True
    else:
        return False

def E1_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].PoA == pinv.DENTAL and seq[i+1].PoA == pinv.RETROFLEX:
        seq[i] = pinv.Consonant.dental2retroflex(seq[i])
        return True
    else:
        return False    

def F1_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].PoA == pinv.DENTAL and seq[i+1].equals(phonemeInv["l"]):
        seq[i] = phonemeInv["l"]
        return True
    else:
        return False 

def L5_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].equals(phonemeInv["s"]) and seq[i+1].PoA == pinv.PALATAL:
        seq[i] = phonemeInv["sh"]
        return True
    else:
        return False 

def L6_con(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    if seq[i].vowel or seq[i+1].vowel:
        return False
    if seq[i].equals(phonemeInv["s"]) and seq[i+1].PoA == pinv.RETROFLEX:
        seq[i] = phonemeInv["Sh"]
        return True
    else:
        return False 

# We could make this more sophisticated by adjusting weights: more reasonable to go from cons --> cons, vowel --> vowel, etc
# there could be some sort of permutation function based on which linguistic features they have in common...
# for another day!
def noise(seq, i):
    if i >= len(seq) - 1 or i < 0:
        return False
    else: 
        newPhoneme = random.choice(list(phonemeInv.keys()))
        seq[i] = phonemeInv[newPhoneme]
        return True

# Define the probability dictionary
RULES = {}
#RULES['T1'] = (0.2, T1) # lower because of potential word boundaries 
#RULES['T2'] = (0.2, T2)
RULES['A1_vow'] = (0.2, A1_vow) 
#RULES['A2_vow'] = (0.2, A2_vow)
#RULES['A3_vow'] = (0.2, A3_vow)
#RULES['A4_vow'] = (0.2, A4_vow)
RULES['B1_vow'] = (0.2, B1_vow)
#RULES['B2_vow'] = (0.2, B2_vow)
#RULES['B3_vow'] = (0.2, B3_vow)
#RULES['B4_vow'] = (0.2, B4_vow)
#RULES['C1_vow'] = (0.2, C1_vow)
#RULES['C2_vow'] = (0.2, C2_vow)
#RULES['C3_vow'] = (0.2, C3_vow)
#RULES['C4_vow'] = (0.2, C4_vow)
RULES['D1_vow'] = (0.2, D1_vow)
RULES['D2_vow'] = (0.2, D2_vow)
#RULES['D3_vow'] = (0.2, D3_vow)
#RULES['D4_vow'] = (0.2, D4_vow)
RULES['A1_con'] = (0.2, A1_con)
# #RULES['B1_con'] = (0.2, B1_con)
RULES['D1_con'] = (0.2, D1_con)
RULES['E1_con'] = (0.2, E1_con)
#RULES['F1_con'] = (0.2, F1_con)
RULES['L5_con'] = (0.2, L5_con)
#RULES['L6_con'] = (0.2, L6_con)
RULES['noise'] = (0.0001, noise)


# for testing purposes, we should set all probabilities to 1 - for determinism! 

#When all probabilities are 1, for this specific input file, here are our counts:
# A1_vow: 16500
# A2_vow: 0
# A3_vow: 0
# A4_vow: 0
# B1_vow: 6000
# B2_vow: 0
# B3_vow: 0
# B4_vow: 0
# C1_vow: 0
# C2_vow: 0
# C3_vow: 0
# C4_vow: 0
# D1_vow: 9000
# D2_vow: 3000
# D3_vow: 0
# D4_vow: 0
# A1_con: 4500
# D1_con: 12000
# E1_con: 3000
# F1_con: 0
# L5_con: 4500
# L6_con: 0



