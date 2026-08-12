from Bio import SeqIO
import re



record = SeqIO.read(
    "BRCA1_protein.fasta",
    "fasta"
)

protein = str(
    record.seq
).upper()


print("=" * 60)
print("BRCA1 PROTEIN MOTIF ANALYSIS")
print("=" * 60)

print(
    "Protein ID:",
    record.id
)

print(
    "Protein length:",
    len(protein)
)



pattern = r"N[^P][ST]"

matches = re.finditer(
    pattern,
    protein
)


print(
    "\nPotential N-X-S/T motifs:"
)

count = 0


for match in matches:

    count += 1

    print(
        "Motif:",
        match.group()
    )

    print(
        "Position:",
        match.start()
    )

    print("-" * 30)


print(
    "Total motifs found:",
    count
)