from Bio import Entrez

Entrez.email = "juyalanshika6@gmail.com"



search_handle = Entrez.esearch(
    db="nucleotide",
    term="BRCA1[Gene Name] AND Homo sapiens[Organism]"
)

search_record = Entrez.read(
    search_handle
)

search_handle.close()


ids = search_record["IdList"]


print(
    "Total records found:",
    len(ids)
)



batch_size = 50



with open(
    "Module_4/BRCA1_batch_sequences.fasta",
    "w"
) as output:

    for i in range(
        0,
        len(ids),
        batch_size
    ):

        batch = ids[
            i:i + batch_size
        ]

        print(
            "Fetching batch:",
            i,
            "to",
            i + len(batch) - 1
        )

        handle = Entrez.efetch(
            db="nucleotide",
            id=batch,
            rettype="fasta",
            retmode="text"
        )

        data = handle.read()

        handle.close()

        output.write(data)


print(
    "Batch retrieval completed!"
)