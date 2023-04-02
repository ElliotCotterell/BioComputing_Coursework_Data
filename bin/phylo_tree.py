# phylo tree
# doesn't work
from Bio import Phylo
import requests
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO, Phylo, SeqIO
from Bio.Align.Applications import ClustalOmegaCommandline
import os
import sqlite3

#reference_file_path = os.path.join("data", "dog_breeds.fa")

# Connect to the database
conn = sqlite3.connect('sequences.db')
c = conn.cursor()

# Prepare the data to send to the web service
# Select all sequences from the table
seqs = []
c.execute("SELECT * FROM sequences")
for row in c.fetchall():
    seq_id = row[0]
    name = row[1]
    seq = str(row[2])
    seqs.append(f">{name}\n{seq}")
data = {'tool': 'simple_phylogeny', 'sequences': "\n".join(seqs)}

# Call the web service to construct the tree
response = requests.post('https://www.ebi.ac.uk/Tools/services/rest/embnet.simple_phylogeny/run', data=data)
job_id = response.text.strip()

# Wait for the job to complete and retrieve the results
status_url = f'https://www.ebi.ac.uk/Tools/services/rest/embnet.simple_phylogeny/status/{job_id}'
result_url = f'https://www.ebi.ac.uk/Tools/services/rest/embnet.simple_phylogeny/result/{job_id}/newick'
status = requests.get(status_url).text.strip()
while status != "FINISHED":
    time.sleep(5)
    status = requests.get(status_url).text.strip()
newick = requests.get(result_url).text.strip()

# Parse the tree and print it
tree = Phylo.read(io.StringIO(newick), 'newick')
Phylo.draw_ascii(tree)

# Read in the FASTA file
# reference_file_path = os.path.join("data", "dog_breeds.fa")
# alignment = AlignIO.read(reference_file_path, "fasta")

# Perform the multiple sequence alignment using Clustal Omega
# clustalomega_cline = ClustalOmegaCommandline(profile1="slow", input="sequences.fasta", # outfmt="clustal", verbose=True)
# stdout, stderr = clustalomega_cline()

# Parse the output file
# aligned_sequences = AlignIO.read("sequences.aln", "clustal")
# print(aligned_sequences)




# Load the sequences into a MultipleSeqAlignment object
# records = list(SeqIO.parse(reference_file_path, "fasta"))
# alignment = MultipleSeqAlignment(records)

# Calculate the distance matrix using a Jukes-Cantor model
# calculator = DistanceCalculator('identity')
# dm = calculator.get_distance(alignment)

# Construct the tree using the UPGMA method
# constructor = DistanceTreeConstructor()
# tree = constructor.upgma(dm)

# Draw the tree
# Phylo.draw_ascii(tree)

