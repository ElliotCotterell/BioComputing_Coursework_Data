from Bio import SeqIO, Align
from Bio.SeqRecord import SeqRecord
import sqlite3
import os


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

# Initialize variables to keep track of the best alignment
best_score = None
best_id = None
best_seq = None

# Loop over the sequences and align each one to the query
i = 0
for row in c.fetchall():
    seq_id = row[0]
    name = row[1]
    seq = str(row[2])
    i += 1 # just to show something happening on the screen
    # Perform the alignment
    alignment = aligner.align(seq, query_seq)
    print(i, ": 99")
    # Check if this alignment is the best one so far
    if best_score is None or alignment.score > best_score:
        best_score = alignment.score
        best_id = seq_id
        best_seq = seq

# Print the details of the best alignment found
print(f"Best alignment: record {best_id}, score {best_score}")
print(f"Sequence: {best_seq}")

