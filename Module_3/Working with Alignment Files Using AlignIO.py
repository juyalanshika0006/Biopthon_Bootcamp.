from Bio import AlignIO



alignment = AlignIO.read(
    "Module_3/brca1_alignment.fasta",
    "fasta"
)


print("=" * 50)
print("ALIGNMENT INFORMATION")
print("=" * 50)



print("\nComplete Alignment:")
print(alignment)



number_of_sequences = len(
    alignment
)

print(
    "\nNumber of sequences:",
    number_of_sequences
)



alignment_length = (
    alignment.get_alignment_length()
)

print(
    "Alignment length:",
    alignment_length
)



print("\nSequences in Alignment:")
print("-" * 50)


for record in alignment:

    print(
        "ID:",
        record.id
    )

    print(
        "Sequence:",
        record.seq
    )

    print("-" * 50)



first_sequence = alignment[0]

print(
    "\nFirst Sequence ID:",
    first_sequence.id
)

print(
    "First Sequence:",
    first_sequence.seq
)



if len(alignment) > 1:

    second_sequence = alignment[1]

    print(
        "\nSecond Sequence ID:",
        second_sequence.id
    )

    print(
        "Second Sequence:",
        second_sequence.seq
    )



first_column = alignment[:, 0]

print(
    "\nFirst Alignment Column:"
)

print(
    first_column
)



if alignment_length > 1:

    second_column = alignment[:, 1]

    print(
        "\nSecond Alignment Column:"
    )

    print(
        second_column
    )



if alignment_length >= 5:

    fifth_column = alignment[:, 4]

    print(
        "\nFifth Alignment Column:"
    )

    print(
        fifth_column
    )



AlignIO.write(
    alignment,
    "Module_3/brca1_alignment_copy.fasta",
    "fasta"
)


print(
    "\nAlignment saved successfully!"
)

print(
    "Output file:",
    "brca1_alignment_copy.fasta"
)


