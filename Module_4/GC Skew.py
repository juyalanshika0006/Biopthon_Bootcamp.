from Bio import SeqIO
import matplotlib.pyplot as plt

record = SeqIO.read(
    "Module_3/BRCA1_record.gb",
    "genbank"
)

SeqIO.write(
    record,
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

print("BRCA1_record.fasta created successfully!")



def gc_skew(sequence):

    g = sequence.count("G")

    c = sequence.count("C")

    if (g + c) == 0:

        return 0

    return (
        (g - c)
        /
        (g + c)
    )


record = SeqIO.read(
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

sequence = str(record.seq)

window_size = 100

positions = []

skews = []

for i in range(
    0,
    len(sequence),
    window_size
):

    window = sequence[
        i:i+window_size
    ]

    positions.append(i)

    skews.append(
        gc_skew(window)
    )

print("GC Skew Values")

for position, skew in zip(
    positions,
    skews
):

    print(
        position,
        ":",
        round(skew, 3)
    )

plt.figure(figsize=(10,5))

plt.plot(
    positions,
    skews
)

plt.title(
    "GC Skew Analysis"
)

plt.xlabel(
    "Genome Position"
)

plt.ylabel(
    "GC Skew"
)

plt.grid(True)

plt.show()
