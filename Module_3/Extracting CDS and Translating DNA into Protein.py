from Bio import SeqIO
from Bio import Entrez

accession="NM_007294"
Entrez.email="juyalanshika6@gmail.com"

handle=Entrez.efetch(
    db="nucleotide",
    id=accession,
    rettype="gb",
    retmode="text"
)

with open("BRCA1_record.gb","w") as file:
    file.write(handle.read())
handle.close()    

print("Genebank file created successfully!!")

# Read GenBank file
record = SeqIO.read(
    "BRCA1_record.gb",
    "genbank"
)


# Loop through features
for feature in record.features:

    # Find CDS
    if feature.type == "CDS":

        # Extract CDS DNA
        cds_sequence = feature.extract(
            record.seq
        )

        # Translate CDS
        protein_sequence = (
            cds_sequence.translate()
        )

        # Get gene name
        gene_name = feature.qualifiers.get(
            "gene",
            ["Unknown"]
        )[0]

        # Get protein product
        product = feature.qualifiers.get(
            "product",
            ["Unknown"]
        )[0]

        # Print results
        print("Gene:", gene_name)

        print(
            "Protein product:",
            product
        )

        print(
            "CDS length:",
            len(cds_sequence)
        )

        print(
            "Protein length:",
            len(protein_sequence)
        )

        print(
            "Protein sequence:",
            protein_sequence
        )

        print("-" * 50)