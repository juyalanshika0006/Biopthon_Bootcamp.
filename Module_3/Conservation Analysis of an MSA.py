from Bio import AlignIO
from collections import Counter



alignment = AlignIO.read(
    "Module_3/brca1_alignment.fasta",
    "fasta"
)


print("=" * 60)
print("BRCA1 CONSERVATION ANALYSIS")
print("=" * 60)



number_of_sequences = len(
    alignment
)

alignment_length = (
    alignment.get_alignment_length()
)


print(
    "\nNumber of sequences:",
    number_of_sequences
)

print(
    "Alignment length:",
    alignment_length
)



#  ANALYZE EVERY ALIGNMENT COLUMN


print(
    "\nCONSERVATION ANALYSIS"
)

print("-" * 60)


for i in range(
    alignment_length
):


    # Get one alignment column


    column = alignment[:, i]



    # Remove gaps


    residues = [
        residue
        for residue in column
        if residue != "-"
    ]



    # Skip column if it contains
    # no actual residues


    if len(residues) == 0:

        continue



    # Count each amino acid


    counts = Counter(
        residues
    )



    # Find the most common amino acid


    most_common_residue, count = (
        counts.most_common(1)[0]
    )



    # Calculate conservation percentage


    conservation = (
        count
        / len(residues)
    ) * 100



    # Print results


    print(
        "Position:",
        i + 1
    )

    print(
        "Column:",
        column
    )

    print(
        "Amino acid counts:",
        counts
    )

    print(
        "Most common residue:",
        most_common_residue
    )

    print(
        "Conservation:",
        round(
            conservation,
            2
        ),
        "%"
    )

    print("-" * 60)