from Bio import SeqIO
import matplotlib.pyplot as plt

record=SeqIO.read(
    "Module_3/BRCA1_record.gb",
    "genbank"
)
SeqIO.write(
    record,
    "Module_3/BRCA1_record.fasta",
    "fasta"                     
)

def gc_skew(sequence):
    g=sequence.count("G")
    c=sequence.count("C")

    if (g+c)==0:
        return 0
    return((g-c)/(g+c))

record=SeqIO.read(
    "Module_3/BRCA1_record.gb",
    "genbank"
)
sequence=str(record.seq)
windows_size=100
positions=[]
skews=[]

for i in range(0, len(sequence),windows_size+1):
    window=sequence[i:i+windows_size]
    positions.append(i)
    skews.append(gc_skew(window)) 

for positions,skews in zip(positions,skews):
    print(f"Position: {positions}, GC Skew: {skews}")