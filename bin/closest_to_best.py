

# Find the closest sequence and its difference from the best alignment,  
# store the best alignment and compare it to each sequence in the database. 

from Bio import SeqIO, Align
import numpy as np
import scipy.stats as stats
import os
import sqlite3


# Load the query sequence
mystery_file_path = os.path.join("data", "mystery.fa")
query_record = SeqIO.read(mystery_file_path, "fasta")
query_seq = str(query_record.seq)

# Connect to the database
conn = sqlite3.connect('sequences.db')
c = conn.cursor()

# Select all sequences from the table
c.execute("SELECT * FROM sequences")

# Set up the pairwise aligner
aligner = Align.PairwiseAligner()
aligner.mode = 'global'
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -0.5
aligner.extend_gap_score = -0.1

# Initialize variables to keep track of the best alignment and closest sequence
best_score = None
best_id = None
best_seq = None
closest_score = None
closest_id = None
closest_seq = None
differences = []

# Loop over the sequences and align each one to the query
i = 0
for row in c.fetchall():
    seq_id = row[0]
    name = row[1]
    seq = str(row[2])
    i += 1
    print(i, " : 99")
    # Perform the alignment
    alignment = aligner.align(seq, query_seq)

    # Check if this alignment is the best one so far
    if best_score is None or alignment.score > best_score:
        best_score = alignment.score
        best_id = seq_id
        best_seq = seq
        
    # Check if this alignment is the closest one so far
    if closest_score is None or abs(alignment.score - best_score) < abs(closest_score - best_score):
        closest_score = alignment.score
        closest_id = seq_id
        closest_seq = seq
        # differences = np.abs(np.array(list(best_seq)) - np.array(list(closest_seq)))
        # doesn't work
        
# Print the details of the best and closest alignments found
print(f"Best alignment: record {best_id}, score {best_score}")
# print(f"Sequence: {best_seq}")
print(f"Closest alignment: record {closest_id}, score {closest_score}")
# print(f"Sequence: {closest_seq}")
# print(f"Differences: {differences}")

