from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


record = SeqIO.read(
    "Module_3/BRCA1_record.gb",
    "genbank"
)

for feature in record.features:

    if feature.type == "CDS":

        
        cds_sequence = feature.extract(record.seq)

        
        protein_sequence = cds_sequence.translate(
            to_stop=True
        )

        
        protein_record = SeqRecord(
            protein_sequence,
            id="BRCA1_protein",
            description="BRCA1 protein sequence"
        )

        
        SeqIO.write(
            protein_record,
            "Module_3/BRCA1_protein.fasta",
            "fasta"
        )

        print("Protein FASTA created successfully!")
