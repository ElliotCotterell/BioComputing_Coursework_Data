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
        print(record.seq)

mystery_file_path = os.path.join("data", "mystery.fa")

# Open the file using Biopython's SeqIO module
with open(mystery_file_path, "r") as file:
    # Parse the sequences in the file
    for record in SeqIO.parse(file, "fasta"):
        # Print the header and sequence data for each sequence
        print(record.description)
        print("This is the mystery record")
        
# Deliverable 1 complete. Files are being read into python and are iterable. 

# Deliverable 2 - create a sequence data base from the dog_breeds fasta file


# first convert fasta file to a csv file

import csv

# define path to output file

csv_file = os.path.join("results", "dog_breeds.csv")


## Open the input fasta file and read the contents
#with open(reference_file_path, "r") as f:
 #   fasta_lines = f.readlines()

## Initialize empty lists for headers and sequences
#headers = []
#sequences = []

# Loop through the fasta_lines variable object to extract headers and sequences
#current_header = "" # create empty string
#current_sequence = "" # create empty sting
#for line in fasta_lines:
    #if line.startswith(">"):  # this is a header line in a fasta file
     #   # Save the previous header and sequence
    #    if current_header != "" and current_sequence != "":
   #         headers.append(current_header)
  #          sequences.append(current_sequence)
#
 #       # Reset the current header and sequence
#        current_header = line.strip()[1:]
#        current_sequence = ""
#    else:  # this is a sequence line
#        current_sequence += line.strip()

# Save the last header and sequence
#headers.append(current_header)
#sequences.append(current_sequence)

# Write the headers and sequences to a csv file
# with open(csv_file, "w", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["header", "sequence"])
#    for i in range(len(headers)):
#        writer.writerow([headers[i], sequences[i]])

# Import the csv file and read it as a panda

import matplotlib.pyplot as plt
import pandas as pd


# df = pd.read_csv(csv_file)
# df = pd.read_table(csv_file)
# df
# please work
# make sure that you have actually installed mathplotlib
# sudo apt-get install python3-matplotlib
# make sure you have also installed pandas
# sudo apt-get install python3-pandas

# print(df)

# does not work, as it doens't slipt the header information correctly. 

# 

#import sqlite3

# Open connection to database
#conn = sqlite3.connect('mydatabase.db')
#c = conn.cursor()

# Open fasta file and read sequences
#with open(reference_file_path, "r") as f:
 #   data = f.read().splitlines()
    
# Parse fasta file and insert sequences into database
#seq_id = 1
#for i in range(0, len(data), 2):
  #  header = data[i]
  #  sequence = data[i+1]
  #  c.execute('INSERT INTO sequences (id, header, sequence) VALUES (?, ?, ?)',
  #            (seq_id, header, sequence))
  #  seq_id += 1

# Commit changes and close connection
#conn.commit()
#conn.close()

# Unable to complete deliverable 2. MOving forward to deliverable 3

# Deliverable 3 - You are an idiot Deliverable 2 was a waste of time - stop trying to reinvent the wheel 

# Deliverable 3  - Use a sequence alignment tool, such as BLAST, to compare the mystery.fa sequence to the sequences in the dog_breeds.fa file.

from Bio import SeqIO
# Open the file using Biopython's SeqIO module
#with open(reference_file_path, "r") as file:
    # Parse the sequences in the file
#    for seq_record in list(SeqIO.parse(file, "fasta")):
        # Print the header and sequence data for each sequence
#        print(seq_record.id)
#        print(repr(seq_record.seq))
#        print(len(seq_record))
  
# isnt't it amazing how easy this stuff is when you actually read the documentation. 

from Bio.Blast import NCBIWWW
from Bio import SeqIO

# Load the reference database
ref_db = SeqIO.to_dict(SeqIO.parse("reference.fasta", "fasta"))

# Load the unknown sequence
unknown_seq = SeqIO.read("unknown.fasta", "fasta")

# Run a BLAST search
result_handle = NCBIWWW.qblast("blastn", "nt", unknown_seq.seq)

# Parse the BLAST results
from Bio.Blast import NCBIXML
blast_records = NCBIXML.parse(result_handle)

# Identify the closest match
best_score = 0
best_match = None
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        breed_name = alignment.title.split("|")[3] # Extract the breed name from the reference sequence header
        if breed_name in ref_db:
            ref_seq = ref_db[breed_name]
            score = alignment.hsps[0].score
            if score > best_score:
                best_score = score
                best_match = breed_name

# Print the closest match
print("Closest match:", best_match)

