from Bio import Entrez
Entrez.email="juyalanshika6@gmail.com"

handle=Entrez.esearch(
    db="nucleotide",
    term="Homo sapiens TP53",
    retmax=5
)
record=Entrez.read(handle)

handle.close()
print("Total results:", record["Count"])

print("First few IDs:")

for record_id in record["IdList"]:
    print(record_id)

