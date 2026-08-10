from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

record=SeqIO.read(
    "Module_3/BRCA1_protein.fasta",
    "fasta"
)

protein=str(record.seq)
print(protein[:50])

print("-"*50)

analysis=ProteinAnalysis(protein)

mw=analysis.molecular_weight()
print("Molecular weight:", mw)

print("-"*50)

composition=analysis.count_amino_acids()


most_common = max(
    composition,
    key=composition.get
)

print(
    "Most common amino acid:",
    most_common
)

print(
    "Count:",
    composition[most_common]
)
print("Amino acid composition:", composition)

print("-"*50)

percentage=analysis.get_amino_acids_percent()
print("Amino acid percentage:", percentage)
print("-"*50)

pi = analysis.isoelectric_point()

print(
    "Isoelectric point:",
    pi
)

aromaticity = analysis.aromaticity()

print(
    "Aromaticity:",
    aromaticity
)

instability = analysis.instability_index()

print(
    "Instability Index:",
    instability
)

structure = analysis.secondary_structure_fraction()

print(
    "Helix:",
    structure[0]
)

print(
    "Turn:",
    structure[1]
)

print(
    "Sheet:",
    structure[2]
)
