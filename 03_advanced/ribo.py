class BioMolecule(object):
    """
    A generic molecule
    """
    def __init__(self, id, name, mass=None):
        self._id = id
        self.name = name
        self.mass = mass

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        # if self.mass and \
        #    not isinstance(value, float) or \
        #    not isinstance(value, int):
        #     raise Exception("mass must be numeric")
#        else:
        self._mass = value


class MRNA(BioMolecule):
    def __init__(self, id, name, sequence, mass=None):
        super(MRNA, self).__init__(id, name, mass)
        self.sequence = sequence

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if not isinstance(value, str):
            raise Exception("sequence must be a string")
        # TODO: check for valid nucleotides here
        self._sequence = value
        self.calculate_mass()

    def calculate_mass(self):
        self.mass = 0
        NA_mass = {'a': 1.0, 'u': 2.2, 'g':2.1, 'c':1.3}
        for na in self.sequence:
            self.mass += NA_mass[na]


    
class Protein(BioMolecule):
    number_of_proteins = 0

    def __init__(self, id, name, sequence, mass=None):
        super(Protein, self).__init__(id, name, mass)
        self.sequence = sequence
        self.number_of_proteins += 1

    def __add__(self, AS):
        self.sequence += AS 

    def calculate_mass(self):
        AA_mass = {'a': 1.0, 'v': 2.9, 'f':3.0}
        for aa in self.sequence:
            self.mass += AA_mass[aa]
   

class Ribosome(BioMolecule):
    def __init__(self, id, name):
        super(Ribosome, self).__init__(id, name)
        self.bound = False
        self.position = None


    def initiate(self, mrna):
        pass


    def elongate(self, mRNA):
        code = {'aug': 'a', 'ugg': 'v', 'ccc': 'f'}
        prot = Protein()
        na_seq = mRNA.sequence
        aa_seq = ''
        for codon_num in range(len(na_seq)/3):
            aa = code[na_seq[0:3]]
            aa_seq += aa
            na_seq = na_seq[3:] 

        prot.sequence = aa_seq
        return prot


