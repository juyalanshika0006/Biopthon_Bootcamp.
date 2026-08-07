from Bio import SeqIO
from collections import Counter


record = SeqIO.read(
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

sequence = str(record.seq)


codons = []

for i in range(
    0,
    len(sequence)-2,
    3
):

    codons.append(
        sequence[i:i+3]
    )


codon_counts = Counter(
    codons
)

print("="*60)

print("CODON USAGE ANALYSIS")

print("="*60)

print(
    "Total Codons:",
    len(codons)
)

print()

print(
    "Most Common Codons"
)

print("-"*40)

for codon, count in codon_counts.most_common(15):

    print(
        codon,
        ":",
        count
    )

print()

print(
    "Codon Frequencies"
)

print("-"*40)

total = sum(
    codon_counts.values()
)

for codon, count in codon_counts.items():

    frequency = (
        count /
        total
    ) * 100

    print(

        codon,

        ":",

        round(
            frequency,
            2
        ),

        "%"

    )