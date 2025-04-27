class SequenceUser:
    def __init__(self,sequence : str):
        self._sequence : str = sequence.upper()

    def __str__(self):
        return f"{self._sequence}"

    def seq(self):
        return self._sequence

class DNASequenceUser(SequenceUser):
    pass

class RNASequenceUser(SequenceUser):
    pass

class ProteinSequenceUser(SequenceUser):
    pass

class ProteinSequence(SequenceUser):
    def __init__(self, identifier: str, data: str):
        self.identifier = identifier
        self.data = data

    def __str__(self):
        return f"{self.identifier}\n{self.data}"

def fasta_to_pro_seq(fasta_file):
    try:
        with open(fasta_file, "r") as file:
            identifier = file.readline()
            content = file.read()
            if identifier and content:
                return ProteinSequence(identifier, content)
            else:
                print("missing identifier or _sequence.")
                return None
    except FileNotFoundError:
        print("File Not Found")
        return None
    except PermissionError:
        print("Permission Denied")
        return None
