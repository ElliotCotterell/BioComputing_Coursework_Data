# data: database, and test sequence - complete Database_creator.py

The `dog_breeds.fa` file contains the sequence in our database, to compare against.
The `mystery.fa` sequence contains a sequence from an uknown dog type, and we want to identify what is the closest breed to it in our database.


# Phylogeny

If you want to make a phylogeny, the simplest way to do it is to feed the file to an online webservice, such as https://www.ebi.ac.uk/Tools/phylogeny/simple_phylogeny/
export a file, then read it in using the Phylo submodule.

You can also compute a phylogenetic tree via the following two steps:
- construct a distance matrix
- construct a tree using a construction algorithm
See the following page for examples: https://biopython.org/docs/1.75/api/Bio.Phylo.TreeConstruction.html


Identifying the Closest Breed - COMPLETE

Read in the dog_breeds.fa file and the mystery.fa sequence. COMPLETE

Use a sequence alignment tool, such as BLAST, to compare the mystery.fa sequence to the sequences in the dog_breeds.fa file. - used a pairwise analisis - unalbe to make a python script write this to a new fasta file. 

Identify the breed in the dog_breeds.fa file with the closest match to the mystery.fa sequence. - COMPLETED closest_to_best.py prints to screen

Creating a Phylogenetic Tree - utterly failed here - unable to create code to create an alignment file SEE multiple_sequence_alignment.py 

Read in the dog_breeds.fa file.

Use a multiple sequence alignment tool, to align the sequences in the dog_breeds.fa file.

Calculate a distance matrix using the aligned sequences. - unalbe to do so

Use a tree construction algorithm, such as neighbor joining, to construct a phylogenetic tree based on the distance matrix.

Visualize the tree using a tree visualization tool, 

SEE

top_level_script.txt for run commands at command line

unable to create a top level bash script

undelivered, writing code into functions an no implementation of tests. 

project/
├── data/
│   ├── dob_breeds.fa
│   └── mystery.fa
├── doc/
│   ├── function_docs.md
│   └── test_docs.md
├── results/
└── bin/
    ├── create_database.py
    ├── pairwise_alignment.py
    ├── phylogeny_construction.py
    └── main.py
└── tests/
    ├── test_create_database.py
    ├── test_pairwise_alignment.py
    └── test_phylogeny_construction.py

