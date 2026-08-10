from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

record=SeqIO.read(
    "Module_3/BRCA1_protein.fasta",
    "fasta"
)

protein=str(record.seq)
print(protein[:50])