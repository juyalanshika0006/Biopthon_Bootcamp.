from Bio import SeqIO
from Bio.Blast import NCBIWWW

protein_record = SeqIO.read(
    "Module_3/BRCA1_protein.fasta",
    "fasta"
)

protein_sequence = str(
    protein_record.seq
)

result_handle = NCBIWWW.qblast(
    "blastp",
    "nr",
    protein_sequence
)

print("BLAST search submitted!")