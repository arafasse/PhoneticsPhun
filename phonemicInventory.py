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
        self.orth = orth
        self.vowel = vowel
        self.PoA = PoA
        
    def isEqual(self, other):
        return (self.orth == other.orth and self.vowel == other.vowel and 
                self.PoA == other.PoA)
    
    def printPhoneme(self):
        print(self.orth)

class Vowel(Phoneme):
    def __init__(self, orth, PoA):
        Phoneme.__init__(self, orth, True, PoA)
    
    def isEqual(self, other):
        return self.isEqual(other) 

class Consonant(Phoneme):
    def __init__(self, orth, PoA, MoA, voiced, aspirated):
        Phoneme.__init__(self, orth, False, PoA)
        self.MoA = MoA
        self.voiced = voiced
        self.aspirated = aspirated
    
    def isEqual(self, other):
        return (self.isEqual(other) and self.MoA == other.MoA and 
                self.voiced == other.voiced and self.aspirated == other.aspirated)

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
phonemeInv['r'] = Vowel("r",RETROFLEX)
phonemeInv['R'] = Vowel("R",RETROFLEX)
phonemeInv['l'] = Vowel("l",DENTAL)
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
phonemeInv[''] = Phoneme("",False,OTHER)

#for p in phonemeInv:
#phonemeInv[p].printPhoneme()