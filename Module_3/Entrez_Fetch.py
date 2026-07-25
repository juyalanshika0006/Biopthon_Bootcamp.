from Bio import Entrez


Entrez.email = "your_actual_email@example.com"



search_handle = Entrez.esearch(
    db="nucleotide",
    term="Homo sapiens TP53",
    retmax=1
)



search_record = Entrez.read(search_handle)

search_handle.close()



record_id = search_record["IdList"][0]

print("NCBI ID:", record_id)



fetch_handle = Entrez.efetch(
    db="nucleotide",
    id=record_id,
    rettype="fasta",
    retmode="text"
)



fasta_data = fetch_handle.read()

fetch_handle.close()



with open("tp53_sequence.fasta", "w") as file:

    file.write(fasta_data)


print("Sequence saved successfully!")