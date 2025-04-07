class InvalidRNASequence(Exception):

    def __init__(self, sequence, message="RNA _sequence must have only ACTG characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"

class InvalidDNASequence(Exception):

    def __init__(self, sequence, message="DNA _sequence must have only AUGC characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"

class InvalidProteinSequence(Exception):

    def __init__(self, sequence, message="Protein _sequence must contain only standard amino acid letters (ACDEFGHIKLMNPQRSTVWY)"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"


