from Bio import SeqIO
from pathlib import Path

fasta_file_path = Path(__file__).parent / "sample.fasta"

for record in SeqIO.parse(fasta_file_path, "fasta"):
    
    sequence = record.seq

    gc_count = sequence.count("G") + sequence.count("C")

    gc_content = (gc_count / len(sequence)) * 100

    if len(sequence) > 10 and gc_content > 30:

        print("ID:", record.id)

        print("Length:", len(sequence))

        print("GC Content:", gc_content)

        print()    
