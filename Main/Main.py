from logging import exception
import numpy as np
from Exceptions.Exceptions import InvalidRNASequence
#import biopython as biopython
from Sequences import *
#data.frame visualise
#ACTG valid for rna
def convert_user_input(user_sequence)->ProteinSequenceUser:
    user_sequence_upper=user_sequence.upper()
    if check_user_input_RNA(user_sequence_upper):
        return ProteinSequenceUser(user_sequence)
    else:
        exception(InvalidRNASequence(user_sequence))

def check_user_input_RNA(user_sequence)->bool:
    user_sequence=set(user_sequence)
    if user_sequence.issubset({"A","C","G","T"}):
        return True
    else:
        return False

if __name__ == '__main__':
    choice = input(" 1.Enter RNA sequence \n 2.Enter Protein sequence \n 3.Enter FASTA file \n")
    match choice:
        case '1':
            user_sequence1 = input('Enter a first sequence: ')
            user_sequence2 = input('Enter a second sequence: ')
            try:
                sequence1 = convert_user_input(user_sequence1)
                sequence2 = convert_user_input(user_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidRNASequence as e:
                print(f"Error: {e}")
        case '2':
            user_protein_sequence1 = input('Enter a first sequence: ')
            user_protein_sequence2 = input('Enter a second sequence: ')
        case '3':
            pass




