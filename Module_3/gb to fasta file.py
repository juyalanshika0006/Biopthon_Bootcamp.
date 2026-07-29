from Bio import SeqIO

SeqIO.convert(
    "Module_3/BRCA1_record.gb",
    "genbank",
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

print("Conversion completed!")