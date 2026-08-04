from Bio.Blast import NCBIXML


with open(
    "Module_3/BRCA1_blast_result.xml"
) as result_handle:

    blast_record = NCBIXML.read(
        result_handle
    )



query_length = (
    blast_record.query_letters
)



for alignment in blast_record.alignments:

    print(
        "\nHit:",
        alignment.title
    )

    for hsp in alignment.hsps:

        
        identity_percentage = (
            hsp.identities
            / hsp.align_length
        ) * 100

        
        coverage = (
            hsp.align_length
            / query_length
        ) * 100

        print(
            "E-value:",
            hsp.expect
        )

        print(
            "Identity:",
            identity_percentage,
            "%"
        )

        print(
            "Alignment length:",
            hsp.align_length
        )

        print(
            "Query coverage:",
            coverage,
            "%"
        )

        print(
            "Query:",
            hsp.query
        )

        print(
            "Subject:",
            hsp.sbjct
        )

        print("-" * 60)
