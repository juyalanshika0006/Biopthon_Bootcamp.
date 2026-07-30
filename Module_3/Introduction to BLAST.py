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

with open(
    "BRCA1_blast_result.xml",
    "w"
) as file:

    file.write(
        result_handle.read()
    )
result_handle.close()

print("BLAST results saved Succesfully!")
