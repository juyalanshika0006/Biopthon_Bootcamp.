from Bio.Blast import NCBIXML

with open(
    "Module_3/BRCA1_blast_result.xml"
) as result_handle:

    blast_record = NCBIXML.read(
        result_handle
    )
print("\n Queries:", blast_record.query)
print("\n Database:", blast_record.database)
print("\n Description:", blast_record.descriptions)
for alignment in blast_record.alignments:

    for hsp in alignment.hsps:

        print(
            hsp
        )
for alignment in blast_record.alignments:

    print(
        "Hit:",
        alignment.title
    )

    for hsp in alignment.hsps:

        print(
            "E-value:",
            hsp.expect
        )

        print(
            "Score:",
            hsp.score
        )

        print(
            "Identities:",
            hsp.identities
        )

        print(
            "Alignment length:",
            hsp.align_length
        )

        print(
            "Query:",
            hsp.query
        )

        print(
            "Subject:",
            hsp.sbjct
        )

        print("-" * 50)        