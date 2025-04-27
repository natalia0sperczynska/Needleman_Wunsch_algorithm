class InvalidRNASequence(Exception):
    """Exception raised for invalid RNA sequences.

        Attributes:
            sequence (str): The invalid sequence that was provided
            message (str): Explanation of the error (default RNA sequence requirements)
        """
    def __init__(self, sequence, message="RNA _sequence must have only ACTG characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"

class InvalidDNASequence(Exception):
    """Exception raised for invalid DNA sequences.

        Attributes:
            sequence (str): The invalid sequence that was provided
            message (str): Explanation of the error (default DNA sequence requirements)
        """
    def __init__(self, sequence, message="DNA _sequence must have only AUGC characters"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"

class InvalidProteinSequence(Exception):
    """Exception raised for invalid protein sequences.

        Attributes:
            sequence (str): The invalid sequence that was provided
            message (str): Explanation of the error (default amino acid requirements)
        """
    def __init__(self, sequence, message="Protein _sequence must contain only standard amino acid letters (ACDEFGHIKLMNPQRSTVWY)"):
        self.sequence = sequence
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. You provided: {self.sequence}"


