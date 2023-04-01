# Python scipt for data manipluation 
# deliverable 1
#Read in the dog_breeds.fa file and the mystery.fa sequence.
# utilise the os liberary
import os

# import SeqIO from Biopython

from Bio import SeqIO


# Set filepath

reference_file_path = os.path.join("data", "dog_breeds.fa")


# Open the file using Biopython's SeqIO module
with open(reference_file_path, "r") as file:
    # Parse the sequences in the file
    for record in SeqIO.parse(file, "fasta"):
        # Print the header and sequence data for each sequence
        print(record.description)
print("These are the reference records")
        # print(record.seq)

mystery_file_path = os.path.join("data", "mystery.fa")

# Open the file using Biopython's SeqIO module
with open(mystery_file_path, "r") as file:
    # Parse the sequences in the file
    for record in SeqIO.parse(file, "fasta"):
        # Print the header and sequence data for each sequence
        print(record.description)
        print("Theis is the mystery record")
