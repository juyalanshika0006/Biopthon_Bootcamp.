from Bio import SeqIO

for record in SeqIO.parse(
    "Module_4/BRCA1_batch_sequences.fasta",
    "fasta"
):
  print("Record ID:", record.id)
  print("Sequence Length:", len(record.seq)) 
  print("-" * 20) 


longest=None

for record in SeqIO.parse("Module_4/BRCA1_batch_sequences.fasta", "fasta"):
    if longest is None or len(record.seq) > len(longest.seq):
        longest=record

print("Longest Record:", longest.id)
print("Length:", len(longest.seq))
print("-" * 20)

shortest=None

for record in SeqIO.parse("Module_4/BRCA1_batch_sequences.fasta", "fasta"):
    if shortest is None or len(record.seq) < len(shortest.seq):
        shortest=record

print("Shortest Record:", shortest.id)
print("Length:", len(shortest.seq))
print("-" * 20)