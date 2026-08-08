from Bio import Entrez

Entrez.email = "juyalanshika6@gmail.com"

search_handle = Entrez.esearch(
    db="nucleotide",
    term="BRCA1 AND Homo sapiens"
)

search_record = Entrez.read(
    search_handle
)

search_handle.close()

ids = search_record["IdList"]

if ids:

    first_id = ids[0]

    fetch_handle = Entrez.efetch(
        db="nucleotide",
        id=first_id,
        rettype="fasta",
        retmode="text"
    )

    sequence = fetch_handle.read()

    fetch_handle.close()

    with open(
        "Module_4/BRCA1_search_result.fasta",
        "w"
    ) as file:

        file.write(sequence)

    print(
        "Sequence saved successfully!"
    )

else:

    print(
        "No records found."
    )