# Establish an inventory of phonemes (maybe this should be input as a text file... could be language specific, na?)

# Places of articulation
GUTTURAL = 1
PALATAL = 2
RETROFLEX = 3
DENTAL = 4
LABIAL = 5
PALATOGUTTURAL = 6
LABIOGUTTURAL = 7
CONSONANTAL_ALLOPHONES = 8
OTHER = 9

# Manners of articulation
PLOSIVE = 1
NASAL = 2
APPROXIMANT = 3
FRICATIVE = 4

# Voicing
UNVOICED = False
VOICED = True

# Aspiration
UNASPIRATED = False
ASPIRATED = True

# Define the phoneme class, which contains both an orthographic string and a boolean (is it a vowel?)
class Phoneme:
    def __init__(self, orth, vowel, PoA):
        self._orth = orth
        self._vowel = vowel
        self._PoA = PoA
    
    def get_orth(self):
        return self._orth
     
    def set_orth(self, orth):
        self._orth = orth
    
    def get_vowel(self):
        return self._vowel
    
    def set_vowel(self, vowel):
        self._vowel = vowel

    def get_PoA(self):
        return self._PoA
    
    def set_PoA(self, PoA):
        self._PoA = PoA
        
    def equals(self, other):
        if self.vowel != other.get_vowel():
            return False
        return (self.orth == other.get_orth() and self.vowel == other.get_vowel() and 
                self.PoA == other.get_PoA())
    
    orth = property(get_orth, set_orth)
    vowel = property(get_vowel, set_vowel)
    PoA = property(get_PoA, set_PoA)
    
    #def printPhoneme(self):
    #    print(self._orth)

class Vowel(Phoneme):
    def __init__(self, orth, PoA):
        Phoneme.__init__(self, orth, True, PoA)
    
    def get_orth(self):
        return self._orth
     
    def set_orth(self, orth):
        self._orth = orth
    
    def get_vowel(self):
        return self._vowel
    
    def set_vowel(self, vowel):
        self._vowel = vowel

    def get_PoA(self):
        return self._PoA
    
    def set_PoA(self, PoA):
        self._PoA = PoA
        
    def equals(self, other):
        if self.vowel != other.get_vowel():
            return False
        return (self.orth == other.get_orth() and self.vowel == other.get_vowel() and 
                self.PoA == other.get_PoA())
    
    def equalsDifferentVowel(self, other):
        if self.vowel != other.get_vowel():
            return False
        return self.orth != other.get_orth() and other.get_vowel()

    orth = property(get_orth, set_orth)

class Consonant(Phoneme):
    def __init__(self, orth, PoA, MoA, voiced, aspirated):
        Phoneme.__init__(self, orth, False, PoA)
        self._MoA = MoA
        self._voiced = voiced
        self._aspirated = aspirated
        
    def get_MoA(self):
        return self._MoA
     
    def set_MoA(self, MoA):
        self._MoA = MoA
    
    def get_voiced(self):
        return self._voiced
    
    def set_voiced(self, voiced):
        self._voiced = voiced

    def get_aspirated(self):
        return self._aspirated
    
    def set_aspirated(self, aspirated):
        self._aspirated = aspirated
        
    MoA = property(get_MoA, set_MoA)
    voiced = property(get_voiced, set_voiced)
    aspirated = property(get_aspirated, set_aspirated)
    
    def equals(self, other):
        if self.vowel != other.get_vowel():
            return False
        return (self.equals(other) and self.MoA == other.get_MoA() and 
                self.voiced == other.get_voiced() and self.aspirated == other.get_aspirated())

# Define the phoneme inventory
phonemeInv = {}
# Define vowels
phonemeInv['a'] = Vowel("a",GUTTURAL)
phonemeInv['aa'] = Vowel("aa",GUTTURAL)
phonemeInv['i'] = Vowel("i",PALATAL)
phonemeInv['ii'] = Vowel("ii",PALATAL)
phonemeInv['u'] = Vowel("u",LABIAL)
phonemeInv['uu'] = Vowel("uu",LABIAL)
phonemeInv['e'] = Vowel("e",PALATOGUTTURAL)
phonemeInv['ai'] = Vowel("ai",PALATOGUTTURAL)
phonemeInv['o'] = Vowel("o",LABIOGUTTURAL)
phonemeInv['au'] = Vowel("au",LABIOGUTTURAL)
phonemeInv['r2'] = Vowel("r2",RETROFLEX)
phonemeInv['R'] = Vowel("R",RETROFLEX)
phonemeInv['l2'] = Vowel("l2",DENTAL)
phonemeInv['L'] = Vowel("L",DENTAL)
phonemeInv['M'] = Vowel("M",CONSONANTAL_ALLOPHONES)
phonemeInv['H'] = Vowel("H",CONSONANTAL_ALLOPHONES)

#OH NO your r's and l's will overwrite each other

# Define consonants
phonemeInv['k'] = Consonant("k",GUTTURAL,PLOSIVE,UNVOICED,UNASPIRATED)
phonemeInv['kh'] = Consonant("kh",GUTTURAL,PLOSIVE,UNVOICED,ASPIRATED)
phonemeInv['c'] = Consonant("c",PALATAL,PLOSIVE,UNVOICED,UNASPIRATED)
phonemeInv['ch'] = Consonant("ch",PALATAL,PLOSIVE,UNVOICED,ASPIRATED)
phonemeInv['T'] = Consonant("T",RETROFLEX,PLOSIVE,UNVOICED,UNASPIRATED)
phonemeInv['Th'] = Consonant("Th",RETROFLEX,PLOSIVE,UNVOICED,ASPIRATED)
phonemeInv['t'] = Consonant("t",DENTAL,PLOSIVE,UNVOICED,UNASPIRATED)
phonemeInv['th'] = Consonant("th",DENTAL,PLOSIVE,UNVOICED,ASPIRATED)
phonemeInv['p'] = Consonant("p",LABIAL,PLOSIVE,UNVOICED,UNASPIRATED)
phonemeInv['ph'] = Consonant("ph",LABIAL,PLOSIVE,UNVOICED,ASPIRATED)
phonemeInv['g'] = Consonant("g",GUTTURAL,PLOSIVE,VOICED,UNASPIRATED)
phonemeInv['gh'] = Consonant("gh",GUTTURAL,PLOSIVE,VOICED,ASPIRATED)
phonemeInv['j'] = Consonant("j",PALATAL,PLOSIVE,VOICED,UNASPIRATED)
phonemeInv['jh'] = Consonant("jh",PALATAL,PLOSIVE,VOICED,ASPIRATED)
phonemeInv['D'] = Consonant("D",RETROFLEX,PLOSIVE,VOICED,UNASPIRATED)
phonemeInv['Dh'] = Consonant("Dh",RETROFLEX,PLOSIVE,VOICED,ASPIRATED)
phonemeInv['d'] = Consonant("d",DENTAL,PLOSIVE,VOICED,UNASPIRATED)
phonemeInv['dh'] = Consonant("dh",DENTAL,PLOSIVE,VOICED,ASPIRATED)
phonemeInv['b'] = Consonant("b",LABIAL,PLOSIVE,VOICED,UNASPIRATED)
phonemeInv['bh'] = Consonant("bh",LABIAL,PLOSIVE,VOICED,ASPIRATED)
phonemeInv['N'] = Consonant("N",RETROFLEX,NASAL,VOICED,UNASPIRATED)
phonemeInv['n'] = Consonant("n",DENTAL,NASAL,VOICED,UNASPIRATED)
phonemeInv['m'] = Consonant("m",LABIAL,NASAL,VOICED,UNASPIRATED)
phonemeInv['N2'] = Consonant("N2",GUTTURAL,NASAL,VOICED,UNASPIRATED)
phonemeInv['n2'] = Consonant("n2",PALATAL,NASAL,VOICED,UNASPIRATED)
phonemeInv['h'] = Consonant("h",GUTTURAL,APPROXIMANT,VOICED,UNASPIRATED)
phonemeInv['y'] = Consonant("y",PALATAL,APPROXIMANT,VOICED,UNASPIRATED)
phonemeInv['r'] = Consonant("r",RETROFLEX,APPROXIMANT,VOICED,UNASPIRATED)
phonemeInv['l'] = Consonant("l",DENTAL,APPROXIMANT,VOICED,UNASPIRATED)
phonemeInv['v'] = Consonant("v",LABIAL,APPROXIMANT,VOICED,UNASPIRATED)
phonemeInv['sh'] = Consonant("sh",PALATAL,FRICATIVE,UNVOICED,ASPIRATED)
phonemeInv['Sh'] = Consonant("Sh",RETROFLEX,FRICATIVE,UNVOICED,ASPIRATED)
phonemeInv['s'] = Consonant("s",DENTAL,FRICATIVE,UNVOICED,ASPIRATED)

# Space
phonemeInv[''] = Phoneme("",False,OTHER)

# Text
phonemeInv['*'] = Phoneme("*",True,OTHER) # Temporarily make it a vowel, for testing purposes

# Deletion
phonemeInv['_'] = Phoneme("_",False,OTHER)

#for p in phonemeInv:
#phonemeInv[p].printPhoneme()