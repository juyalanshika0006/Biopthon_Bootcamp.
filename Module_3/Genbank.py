from Bio import Entrez
from Bio import SeqIO

Entrez.email = "juyalanshika6@gmail.com"

accession = "NM_000546"

handle = Entrez.efetch(
    db="nucleotide",
    id=accession,
    rettype="gb",
    retmode="text"
)

with open("tp53_record.gb", "w") as file:
    file.write(handle.read())

handle.close()

print("GenBank file created successfully!")



record = SeqIO.read(
    "tp53_record.gb",
    "genbank"
)

print("ID:", record.id)

print("Description:")
print(record.description)

print("\nSequence length:")
print(len(record.seq))

print("\nAnnotations:")
print(record.annotations)

print("\nAnnotations with keys:")
print(record.annotations.keys())

print("\nFeatures:")

for feature in record.features:
    print(feature.type, feature.location)
    print("-" * 30)

for feature in record.features:

    if feature.type == "CDS":

        cds_sequence = feature.extract(record.seq)

        print("CDS location:", feature.location)
        print("CDS sequence:", cds_sequence)

        print("-" * 30)