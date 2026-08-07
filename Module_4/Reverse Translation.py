from Bio import SeqIO

record = SeqIO.read(
    "Module_3/BRCA1_protein.fasta",
    "fasta"
)

protein = str(record.seq)

print(protein[:50])

codon_table = {

    "A":"GCT",

    "R":"CGT",

    "N":"AAT",

    "D":"GAT",

    "C":"TGT",

    "Q":"CAA",

    "E":"GAA",

    "G":"GGT",

    "H":"CAT",

    "I":"ATT",

    "L":"CTG",

    "K":"AAA",

    "M":"ATG",

    "F":"TTT",

    "P":"CCT",

    "S":"TCT",

    "T":"ACT",

    "W":"TGG",

    "Y":"TAT",

    "V":"GTT"

}

dna = ""

for amino_acid in protein:

    dna += codon_table[amino_acid]

print(dna[:90])

with open(
    "Module_4/Reverse_Translated_BRCA1.fasta",
    "w"
) as file:

    file.write(
        ">Reverse_Translated_BRCA1\n"
    )

    file.write(dna)

print(
    "DNA saved successfully!"
)