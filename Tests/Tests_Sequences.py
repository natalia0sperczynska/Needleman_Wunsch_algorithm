import unittest

from Sequences.Sequences import *
class MyTestCase(unittest.TestCase):
    """
    Unit tests for the Sequences.

    Methods:
    setUpClass():
        Executes once before all test methods.
    setUp():
        Prepares test data for each test method.
    test_protein_sequence_initialization():
        Tests initialization of the ProteinSequence class.
    test_protein_sequence_str():
        Tests the __str__ method of the ProteinSequence class.
    test_fasta_to_prto_seq():
        Tests the fasta_to_prto_seq function with valid and invalid inputs.
    tearDownClass():
        Executes once after all test methods.
    """
    @classmethod
    def setUpClass(cls):
        """Executed once before all tests."""
        print("setUpClass method: Runs before all tests...")

    def setUp(self):
        """Sets up data for testing."""
        self.identifier = ">sp|P02768|ALBU_HUMAN"
        self.data = "MKWVTFISLLFLFSSAYS"
        self.test_file = "test_albumin.txt"

        with open(self.test_file, "w") as file:
            file.write(f"{self.identifier}\n{self.data}")

    def test_protein_sequence_initialization(self):
        """
        Test the initialization of the ProteinSequence class.
        """
        self.protein = ProteinSequence(self.identifier, self.data)
        self.assertEqual(self.protein.identifier.strip(), self.identifier.strip())
        self.assertEqual(self.protein.data, self.data)

    def test_protein_sequence_str(self):
        """
        Test the __str__ method of the ProteinSequence class.
        """
        self.assertEqual(str(ProteinSequence(self.identifier, self.data)),">sp|P02768|ALBU_HUMAN\nMKWVTFISLLFLFSSAYS")

    def test_fasta_to_prto_seq(self):
        """
        Test the fasta_to_prto_seq function with a valid and invalid FASTA file.
        """
        self.assertEqual(fasta_to_pro_seq(self.test_file).identifier.strip(), self.identifier.strip())
        self.assertEqual(fasta_to_pro_seq(self.test_file).data, self.data)
        self.assertIsNone(fasta_to_pro_seq("non_existent_file.txt"))

    @classmethod
    def tearDownClass(cls):
        """Executed once after all tests."""
        print("\nRunning tearDown method after all tests...")

if __name__ == '__main__':
    unittest.main()
