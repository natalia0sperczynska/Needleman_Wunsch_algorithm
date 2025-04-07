from logging import exception
import numpy as np
from Exceptions.Exceptions import InvalidRNASequence, InvalidDNASequence, InvalidProteinSequence
#import biopython as biopython
from Sequences import *
#data.frame visualise
#ACTG valid for rna

def convert_user_input_Protein(user_sequence:str)->ProteinSequenceUser:
    user_sequence_upper=user_sequence.upper()
    user_sequence_upper_set = set(user_sequence)
    if user_sequence_upper_set.issubset({"A", "C", "D", "E","F","G","H","I","J","K","L","M","N","Q","R","S","T","V","W","Y"}):
        return ProteinSequenceUser(user_sequence_upper)
    else:
        exception(InvalidProteinSequence(user_sequence))

def convert_user_input_RNA(user_sequence:str)->RNASequenceUser:
    user_sequence_upper = user_sequence.upper()
    user_sequence_upper_set = set(user_sequence)
    if user_sequence_upper_set.issubset({"A", "C", "G", "T"}):
        return RNASequenceUser(user_sequence_upper)
    else:
        exception(InvalidRNASequence(user_sequence))

def convert_user_input_DNA(user_sequence:str)->DNASequenceUser:
    user_sequence_upper=user_sequence.upper()
    user_sequence_upper_set = set(user_sequence)
    if user_sequence_upper_set.issubset({"A", "C", "G", "U"}):
        return DNASequenceUser(user_sequence_upper)
    else:
        exception(InvalidDNASequence(user_sequence))

if __name__ == '__main__':
    choice = input(" 1.Enter DNA sequence \n 2.Enter RNA sequence \n 3.Enter Protein sequence \n 4.Enter FASTA file \n")
    match choice:
        case '1':
            user_protein_sequence1 = input('Enter a first DNA sequence: ')
            user_protein_sequence2 = input('Enter a second DNA sequence: ')
            try:
                sequence1 = convert_user_input_DNA(user_protein_sequence1)
                sequence2 = convert_user_input_DNA(user_protein_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidDNASequence as e:
                print(f"Error: {e}")
        case '2':
            user_RNA_sequence1 = input('Enter a first RNA sequence: ')
            user_RNA_sequence2 = input('Enter a second RNA sequence: ')
            try:
                sequence1 = convert_user_input_DNA(user_RNA_sequence1)
                sequence2 = convert_user_input_DNA(user_RNA_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidRNASequence as e:
                print(f"Error: {e}")
        case '3':
            user_protein_sequence1 = input('Enter a first protein sequence: ')
            user_protein_sequence2 = input('Enter a second protein sequence: ')
            try:
                sequence1 = convert_user_input_Protein(user_protein_sequence1)
                sequence2 = convert_user_input_Protein(user_protein_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidProteinSequence as e:
                print(f"Error: {e}")
        case '4':
            try:
                fasta_to_pro_seq(fasta_file="Tests/test_amylase.txt")
            except InvalidProteinSequence as e:
                print(f"Error: {e}")




