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
phonemeInv.append(Phoneme("l",DENTAL))
phonemeInv.append(Phoneme("L",DENTAL))

# Define consonants
phonemeInv.append(Phoneme("k",GUTTURAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Phoneme("kh",GUTTURAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("c",PALATAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Phoneme("ch",PALATAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("T",RETROFLEX,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Phoneme("Th",RETROFLEX,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("t",DENTAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Phoneme("th",DENTAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("p",LABIAL,PLOSIVE,UNVOICED,UNASPIRATED))
phonemeInv.append(Phoneme("ph",LABIAL,PLOSIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("g",GUTTURAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("gh",GUTTURAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Phoneme("j",PALATAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("jh",PALATAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Phoneme("D",RETROFLEX,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("Dh",RETROFLEX,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Phoneme("d",DENTAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("dh",DENTAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Phoneme("b",LABIAL,PLOSIVE,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("bh",LABIAL,PLOSIVE,VOICED,ASPIRATED))
phonemeInv.append(Phoneme("N",RETROFLEX,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("n",DENTAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("m",LABIAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("N2",GUTTURAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("n2",PALATAL,NASAL,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("h",GUTTURAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("y",PALATAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("r",RETROFLEX,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("l",DENTAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("v",LABIAL,APPROXIMANT,VOICED,UNASPIRATED))
phonemeInv.append(Phoneme("sh",PALATAL,FRICATIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("Sh",RETROFLEX,FRICATIVE,UNVOICED,ASPIRATED))
phonemeInv.append(Phoneme("s",DENTAL,FRICATIVE,UNVOICED,ASPIRATED))


