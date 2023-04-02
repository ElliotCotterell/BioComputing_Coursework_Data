# Try again



from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sqlite3
import os

# Set filepath

reference_file_path = os.path.join("data", "dog_breeds.fa")


# Open the file using Biopython's SeqIO module
# Print the header and sequence data for each sequence
with open(reference_file_path, "r") as file:
    # Parse the sequences in the file
    for record in SeqIO.parse(file, "fasta"):
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

# Open the FASTA file and parse the sequences
fasta_file = reference_file_path
records = list(SeqIO.parse(fasta_file, "fasta"))

# Connect to the database
conn = sqlite3.connect('sequences.db')
c = conn.cursor()

# Create a table to store the sequences
c.execute('''CREATE TABLE sequences
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              sequence TEXT)''')

# Insert each sequence into the database
for record in records:
    sequence = str(record.seq)
    name = record.name
    c.execute("INSERT INTO sequences (name, sequence) VALUES (?, ?)", (name, sequence))

# Save changes and close the connection
conn.commit()
conn.close()


