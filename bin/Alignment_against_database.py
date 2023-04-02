# Print Database

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sqlite3
import os
from Bio import Align

mystery_file_path = os.path.join("data", "mystery.fa")

# Load the query sequence
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

# Loop over the sequences and align each one to the query
for row in c.fetchall():
    name = row[1]
    seq = str(row[2])
    
    # Perform the alignment
    alignment = aligner.align(seq, query_seq)

    # Print the results
    print(f"Alignment of {name} to query:")
    print(alignment)

# Close the connection
conn.close()
