from Bio import SeqIO
from pathlib import Path

fasta_file_path = Path(__file__).parent / "sample.fasta"

for record in SeqIO.parse(fasta_file_path, "fasta"):
   
    print("ID:", record.id)

    print("Description:", record.description)

    print("Sequence:", record.seq)

    print("Length:", len(record.seq))

    print("-" * 40)
