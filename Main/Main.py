from Converters import *
if __name__ == '__main__':
    choice = input(" 1.Enter DNA _sequence \n 2.Enter RNA _sequence \n 3.Enter Protein _sequence \n 4.Enter FASTA file \n")
    match choice:
        case '1':
            user_protein_sequence1 = input('Enter a first DNA _sequence: ')
            user_protein_sequence2 = input('Enter a second DNA _sequence: ')
            try:
                sequence1 = convert_user_input_DNA(user_protein_sequence1)
                sequence2 = convert_user_input_DNA(user_protein_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidDNASequence as e:
                print(f"Error: {e}")
        case '2':
            user_RNA_sequence1 = input('Enter a first RNA _sequence: ')
            user_RNA_sequence2 = input('Enter a second RNA _sequence: ')
            try:
                sequence1 = convert_user_input_DNA(user_RNA_sequence1)
                sequence2 = convert_user_input_DNA(user_RNA_sequence2)
                print(sequence1)
                print(sequence2)
            except InvalidRNASequence as e:
                print(f"Error: {e}")
        case '3':
            user_protein_sequence1 = input('Enter a first protein _sequence: ')
            user_protein_sequence2 = input('Enter a second protein _sequence: ')
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




