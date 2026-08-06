from Bio import SeqIO
from Bio.Seq import Seq


record = SeqIO.read(
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

sequence = str(record.seq)

stop_codons = [
    "TAA",
    "TAG",
    "TGA"
]

orfs = []

for i in range(
    len(sequence)-2
):

    codon = sequence[i:i+3]

    if codon == "ATG":

        for j in range(
            i+3,
            len(sequence)-2,
            3
        ):

            stop = sequence[j:j+3]

            if stop in stop_codons:

                orf = sequence[i:j+3]

                orfs.append(orf)

                break


print("=" * 60)
print("ORF ANALYSIS")
print("=" * 60)

print(
    "Total ORFs:",
    len(orfs)
)

longest_orf = max(
    orfs,
    key=len
)

print(
    "Longest ORF Length:",
    len(longest_orf)
)

protein = Seq(
    longest_orf
).translate(
    to_stop=True
)

print(
    "Protein Length:",
    len(protein)
)

print("\nProtein Sequence:\n")
print(protein)

with open(
    "Module_4/Longest_ORF_Protein.fasta",
    "w"
) as file:

    file.write(
        ">Longest_ORF\n"
    )

    file.write(
        str(protein)
    )

print(
    "Protein saved successfully!"
)