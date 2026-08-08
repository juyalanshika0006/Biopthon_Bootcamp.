from Bio import Entrez


Entrez.email = "juyalanshika6@gmail.com"


search_handle = Entrez.esearch(
    db="nucleotide",
    term='BRCA1[Gene Name] AND Homo sapiens[Organism] AND RefSeq[Filter]'
)

search_record = Entrez.read(
    search_handle
)

search_handle.close()

ids = search_record["IdList"]

print(
    "Number of results:",
    search_record["Count"]
)

print(
    "IDs found:",
    ids
)


if ids:

    first_id = ids[0]

    print(
        "\nFirst ID:",
        first_id
    )


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



    summary_handle = Entrez.esummary(
        db="nucleotide",
        id=first_id
    )

    summary = Entrez.read(
        summary_handle
    )

    summary_handle.close()


    print(
        "\nNCBI Summary:"
    )

    print(summary)


else:

    print(
        "No records found."
    )
