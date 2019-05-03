# Establish an inventory of phonemes

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

# Define the Phoneme class
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
    
# Define the Vowel class, a subtype of Phoneme
class Vowel(Phoneme):
    def __init__(self, orth, PoA):
        Phoneme.__init__(self, orth, True, PoA)
        
    def equals(self, other):
        if self.vowel != other.get_vowel():
            return False
        if self.orth != other.get_orth():
            return False
        if self.PoA != other.get_PoA():
            return False
        return True
    
    def equalsDifferentVowel(self, other):
        if self.vowel != other.get_vowel():
            return False
        return self.orth != other.get_orth() and other.get_vowel()

# Define the Consonant class, a subtype of Phoneme
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
        # Not pretty, but avoids infinite recursion error
        if self.vowel != other.get_vowel():
            return False
        if self.orth != other.get_orth():
            return False
        if self.PoA != other.get_PoA():
            return False
        if self.MoA != other.get_MoA():
            return False
        if self.voiced != other.get_voiced():
            return False
        if self.aspirated != other.get_aspirated():
            return False
        return True
        
    @staticmethod
    def dental2palatal(other):
        if other.get_PoA() != DENTAL:
            return other
        else:
            if other.get_orth() == "t":
                return phonemeInv['c']
            if other.get_orth() == "th":
                return phonemeInv['ch']
            if other.get_orth() == "d":
                return phonemeInv['j']
            if other.get_orth() == "dh":
                return phonemeInv['jh']
            if other.get_orth() == "n": 
                return phonemeInv['n2']
            if other.get_orth() == "l": 
                return phonemeInv['y']
            else:
                return other
    
    @staticmethod
    def dental2retroflex(other):
        if other.get_PoA() != DENTAL:
            return other
        else:
            if other.get_orth() == "t":
                return phonemeInv['T']
            if other.get_orth() == "th":
                return phonemeInv['Th']
            if other.get_orth() == "d":
                return phonemeInv['D']
            if other.get_orth() == "dh":
                return phonemeInv['Dh']
            if other.get_orth() == "n": 
                return phonemeInv['N']
            if other.get_orth() == "l": 
                return phonemeInv['r']
            else:
                return other

    @staticmethod
    def voiced2unvoiced(other):
        if other.get_voiced():
            return other
        else:
            if other.get_orth() == "k":
                return phonemeInv['g']
            if other.get_orth() == "kh":
                return phonemeInv['gh']
            if other.get_orth() == "c":
                return phonemeInv['j']
            if other.get_orth() == "ch":
                return phonemeInv['jh']
            if other.get_orth() == "T":
                return phonemeInv['D']
            if other.get_orth() == "Th":
                return phonemeInv['Dh']
            if other.get_orth() == "t":
                return phonemeInv['d']
            if other.get_orth() == "th":
                return phonemeInv['dh']
            if other.get_orth() == "p":
                return phonemeInv['b']
            if other.get_orth() == "ph":
                return phonemeInv['bh']
            else:
                return other
            
    @staticmethod
    def unvoiced2voiced(other):
        if not other.get_voiced():
            return other
        else:
            if other.get_orth() == "g":
                return phonemeInv['k']
            if other.get_orth() == "gh":
                return phonemeInv['kh']
            if other.get_orth() == "j":
                return phonemeInv['c']
            if other.get_orth() == "jh":
                return phonemeInv['ch']
            if other.get_orth() == "D":
                return phonemeInv['T']
            if other.get_orth() == "Dh":
                return phonemeInv['Th']
            if other.get_orth() == "d":
                return phonemeInv['t']
            if other.get_orth() == "dh":
                return phonemeInv['th']
            if other.get_orth() == "b":
                return phonemeInv['p']
            if other.get_orth() == "bh":
                return phonemeInv['ph']
            else:
                return other
        
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
phonemeInv[''] = Phoneme("",True,OTHER)

# Text
phonemeInv['*'] = Phoneme("*",True,OTHER) # Temporarily make it a vowel, for testing purposes

# Deletion
phonemeInv['_'] = Phoneme("_",True,OTHER)
