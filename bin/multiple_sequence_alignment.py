# multiple sequence alignment
# another dead end
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
import os

# Load input sequences from a FASTA file
reference_file_path = os.path.join("data", "dog_breeds.fa")
input_sequences = list(AlignIO.read(reference_file_path, "fasta"))

# Perform a multiple sequence alignment using ClustalW
aligned_sequences = AlignIO.MultipleSeqAlignment(input_sequences)
aligned_sequences = aligned_sequences.sort()

# Save the aligned sequences in a new FASTA file
output_file = "aligned.fasta"
with open(output_file, "w") as handle:
    AlignIO.write(aligned_sequences, handle, "fasta")

