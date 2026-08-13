from Bio import AlignIO
import matplotlib.pyplot as plt


alignment = AlignIO.read(
    "Module_3/BRCA1_MSA.aln-clustal_num",
    "clustal"
)



print("=" * 50)
print("BRCA1 MULTIPLE SEQUENCE ALIGNMENT")
print("=" * 50)

print("Number of sequences:", len(alignment))

print(
    "Alignment length:",
    alignment.get_alignment_length()
)



print("\nSequence IDs:")

for record in alignment:
    print(record.id)


#Calculating conserved positions in the alignment   

print("\nConserved positions in the alignment:")
for position in range(alignment.get_alignment_length()):
    column=alignment[:,position]
    if len(set(column))==1:
        print(f"Position {position+1}: {column[0]}")

#calculation of the percentage of conserved positions in the alignment

total_positions = alignment.get_alignment_length()

conserved_positions = 0

for position in range(total_positions):

    column = alignment[:, position]

    if len(set(column)) == 1:
        conserved_positions += 1


conservation_percentage = (
    conserved_positions / total_positions
) * 100


print("\n" + "=" * 50)

print(
    "Conserved positions:",
    conserved_positions
)

print(
    "Total positions:",
    total_positions
)

print(
    f"Conservation: "
    f"{conservation_percentage:.2f}%"
)

variable_positions = total_positions - conserved_positions

print(
    "Variable positions:",
    variable_positions
)


#Visualization of the conservation profile of the alignment

positions = []
conservation_values = []


for position in range(
    alignment.get_alignment_length()
):

    column = alignment[:, position]

    positions.append(position + 1)

    if len(set(column)) == 1:
        conservation_values.append(100)
    else:
        conservation_values.append(0)


plt.figure(figsize=(10, 5))

plt.bar(
    positions,
    conservation_values
)

plt.xlabel("Alignment Position")
plt.ylabel("Strict Conservation (%)")

plt.title(
    "BRCA1 Alignment Conservation Profile"
)

plt.ylim(0, 110)

plt.xticks(positions)

plt.tight_layout()

plt.savefig(
    "Module_3/BRCA1_conservation_profile.png"
)

plt.show()