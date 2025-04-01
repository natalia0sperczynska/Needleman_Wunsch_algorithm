class InvalidRNASequence(Exception):

    def __init__(self, sequence, message="RNA sequence must have only ACTG characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"

class InvalidDNASequence(Exception):

    def __init__(self, sequence, message="DNA sequence must have only ATGC characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"


