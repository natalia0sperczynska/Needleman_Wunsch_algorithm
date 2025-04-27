
from tkinter import messagebox
from Exceptions.Exceptions import *
from Sequences.Sequences import ProteinSequenceUser, RNASequenceUser, DNASequenceUser


def is_correct(user_sequence : str, allowed_symbols : set) -> bool:
    user_sequence_upper = user_sequence.upper()
    user_sequence_upper_set = set(user_sequence_upper)
    return user_sequence_upper_set.issubset(allowed_symbols)

def convert_user_input_Protein(user_sequence:str)->ProteinSequenceUser:
    if is_correct(user_sequence, {"A", "C", "D", "E","F","G","H","I","J","K","L","M","N","Q","R","S","T","V","W","Y","P"}):
        return ProteinSequenceUser(user_sequence)
    else:
        messagebox.showerror("DNA Sequence Error", f" {InvalidProteinSequence(user_sequence).message}")
        return None


def convert_user_input_RNA(user_sequence:str)->RNASequenceUser:
    if is_correct(user_sequence,{"A", "C", "G", "U"}):
        return RNASequenceUser(user_sequence)
    else:
        messagebox.showerror("DNA Sequence Error", f" {InvalidRNASequence(user_sequence).message}")
        return None


def convert_user_input_DNA(user_sequence:str)->DNASequenceUser:
    if is_correct(user_sequence,{"A", "C", "G", "T"}):
        return DNASequenceUser(user_sequence)
    else:
        messagebox.showerror("DNA Sequence Error", f" {InvalidDNASequence(user_sequence).message}")
        return None

