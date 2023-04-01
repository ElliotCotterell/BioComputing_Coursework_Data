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
