from Bio import SeqIO
from pathlib import Path

fasta_file_path = Path(__file__).parent / "sample.fasta"

selected_records = []

for record in SeqIO.parse(fasta_file_path, "fasta"):

    if len(record.seq) > 10:

        selected_records.append(record)

SeqIO.write(
    selected_records,
    "filtered_sequences.fasta",
    "fasta"
)
print("Sequences saved:", len(selected_records))