# Establish an inventory of phonemes (maybe this should be input as a text file... could be language specific, na?)

# Places of articulation
GUTTURAL = 1
PALATAL = 2
RETROFLEX = 3
DENTAL = 4
LABIAL = 5
PALATOGUTTURAL = 6
LABIOGUTTURAL = 7

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
        print self.orth 

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
phonemeInv = []
# Define vowels
phonemeInv.append(Vowel("a",GUTTURAL))
phonemeInv.append(Vowel("aa",GUTTURAL))
phonemeInv.append(Vowel("i",PALATAL))
phonemeInv.append(Vowel("ii",PALATAL))
phonemeInv.append(Vowel("u",LABIAL))
phonemeInv.append(Vowel("uu",LABIAL))
phonemeInv.append(Vowel("e",PALATOGUTTURAL))
phonemeInv.append(Vowel("ai",PALATOGUTTURAL))
phonemeInv.append(Vowel("o",LABIOGUTTURAL))
phonemeInv.append(Vowel("au",LABIOGUTTURAL))
phonemeInv.append(Vowel("r",RETROFLEX))
phonemeInv.append(Vowel("R",RETROFLEX))
phonemeInv.append(Vowel("l",DENTAL))
phonemeInv.append(Vowel("L",DENTAL))

# Define consonants
phonemeInv.append(Consonant("k",GUTTURAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Consonant("kh",GUTTURAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("c",PALATAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Consonant("ch",PALATAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("T",RETROFLEX,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Consonant("Th",RETROFLEX,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("t",DENTAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Consonant("th",DENTAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("p",LABIAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Consonant("ph",LABIAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("g",GUTTURAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("gh",GUTTURAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Consonant("j",PALATAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("jh",PALATAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Consonant("D",RETROFLEX,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("Dh",RETROFLEX,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Consonant("d",DENTAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("dh",DENTAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Consonant("b",LABIAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("bh",LABIAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Consonant("N",RETROFLEX,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("n",DENTAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("m",LABIAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("N2",GUTTURAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("n2",PALATAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("h",GUTTURAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("y",PALATAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("r",RETROFLEX,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("l",DENTAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("v",LABIAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Consonant("sh",PALATAL,FRICATIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("Sh",RETROFLEX,FRICATIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Consonant("s",DENTAL,FRICATIVE,UNVOICED,ASPIRATED))


for p in phonemeInv:
    p.printPhoneme()