from logging import exception

from Exceptions.Exceptions import *
from Sequences import *

def is_correct(user_sequence : str, allowed_symbols : set) -> bool:
    user_sequence_upper = user_sequence.upper()
    user_sequence_upper_set = set(user_sequence_upper)
    return user_sequence_upper_set.issubset(allowed_symbols)


def convert_user_input_Protein(user_sequence:str)->ProteinSequenceUser:
    if is_correct(user_sequence, {"A", "C", "D", "E","F","G","H","I","J","K","L","M","N","Q","R","S","T","V","W","Y"}):
        return ProteinSequenceUser(user_sequence)
    else:
        exception(InvalidProteinSequence(user_sequence))

def convert_user_input_RNA(user_sequence:str)->RNASequenceUser:
    user_sequence_upper = user_sequence.upper()
    user_sequence_upper_set = set(user_sequence_upper)
    if user_sequence_upper_set.issubset({"A", "C", "G", "T"}):
        return RNASequenceUser(user_sequence_upper)
    else:
        exception(InvalidRNASequence(user_sequence))

def convert_user_input_DNA(user_sequence:str)->DNASequenceUser:
    user_sequence_upper=user_sequence.upper()
    user_sequence_upper_set = set(user_sequence_upper)
    if user_sequence_upper_set.issubset({"A", "C", "G", "U"}):
        return DNASequenceUser(user_sequence_upper)
    else:
        exception(InvalidDNASequence(user_sequence))