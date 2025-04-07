class DNASequenceUser:
    def __init__(self,sequence):
        self.sequence = sequence

    def __str__(self):
        return f"{self.sequence}"

class RNASequenceUser:
    def __init__(self,sequence):
        self.sequence = sequence

    def __str__(self):
        return f"{self.sequence}"

class ProteinSequenceUser:
    def __init__(self,sequence):
        self.sequence = sequence

    def __str__(self):
     return f"{self.sequence}"

class ProteinSequence:
    """
        Represents a protein sequence with an identifier and sequence data.

          Attributes:
          identifier (str): the FASTA identifier for the protein.
          data (str) :The sequence data of the protein.

          Methods
          __init__():
          Initializes a ProteinSequence object with an identifier and sequence data.
          __str__():
              Returns the protein sequence in FASTA format.
    """
    def __init__(self, identifier: str, data: str):
        """
            Initializes a ProteinSequence object with an identifier and sequence data.

            Param:
            identifier (str) : The FASTA identifier for the protein.
            data (str) : The sequence data of the protein.
        """
        self.identifier = identifier
        self.data = data

    def __str__(self):
        """
            Returns the protein sequence in FASTA format.

            Returns:
                str :The protein sequence formatted as:
                        >identifier
                        data
        """
        return f"{self.identifier}\n{self.data}"

def fasta_to_pro_seq(fasta_file):
    """
       Reads a FASTA file and creates a ProteinSequence object.

       Param:
       fasta_file: Path to the FASTA file.

       Return:
       ProteinSequence object or None: A ProteinSequence object if the file is valid,containing the identifier and sequence, None otherwise.
       """
    try:
        with open(fasta_file, "r") as file:
            identifier = file.readline()
            content = file.read()
            if identifier and content:
                return ProteinSequence(identifier, content)
            else:
                print("missing identifier or sequence.")
                return None
    except FileNotFoundError:
        print("File Not Found")
        return None
    except PermissionError:
        print("Permission Denied")
        return None
