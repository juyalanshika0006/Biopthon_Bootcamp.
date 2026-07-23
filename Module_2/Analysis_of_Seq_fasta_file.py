from Bio import SeqIO
from pathlib import Path

fasta_file_path = Path(__file__).parent / "sample.fasta"

for record in SeqIO.parse(fasta_file_path, "fasta"):
    sequence = record.seq

    length = len(sequence)

    a_count = sequence.count("A")

    t_count = sequence.count("T")

    g_count = sequence.count("G")

    c_count = sequence.count("C")

    gc_count = g_count + c_count

    at_count = a_count + t_count

    gc_content = (gc_count / length) * 100

    at_content = (at_count / length) * 100

    print("ID:", record.id)

    print("Sequence:", sequence)

    print("Length:", length)

    print("A:", a_count)

    print("T:", t_count)

    print("G:", g_count)

    print("C:", c_count)

    print("GC Content:", gc_content)

    print("AT Content:", at_content)

    print("-" * 50)
