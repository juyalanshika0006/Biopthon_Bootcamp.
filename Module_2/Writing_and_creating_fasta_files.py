from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
sequence=Seq("ATGGCTAACGCT")
record1=SeqRecord(
    sequence,
    id="Gene_1",
    description="Example DNA Sequence"
)
record2 = SeqRecord(
    Seq("ATGCGTTTAGCA"),
    id="Gene_2",
    description="Second gene"
)

record3 = SeqRecord(
    Seq("ATGTTCCGGAAA"),
    id="Gene_3",
    description="Third gene"
)
records=[record1,record2,record3]

SeqIO.write(records,"output.fasta" , "fasta")