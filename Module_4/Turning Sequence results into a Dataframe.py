from Bio import SeqIO
import pandas as pd


results = []


for record in SeqIO.parse(
    "Module_4/BRCA1_batch_sequences.fasta",
    "fasta"
):

    sequence = str(
        record.seq
    ).upper()

    length = len(sequence)

    a_count = sequence.count("A")

    t_count = sequence.count("T")

    g_count = sequence.count("G")

    c_count = sequence.count("C")

    if length > 0:

        gc_content = (
            (
                g_count
                +
                c_count
            )
            /
            length
        ) * 100

    else:

        gc_content = 0


    results.append({

        "ID": record.id,

        "Length": length,

        "A": a_count,

        "T": t_count,

        "G": g_count,

        "C": c_count,

        "GC_Content": gc_content

    })


df = pd.DataFrame(
    results
)

print(df)
