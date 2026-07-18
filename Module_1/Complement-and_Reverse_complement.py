from Bio.Seq import Seq
dna=Seq("ATGCGT")
print("Orignal:", dna)
print("Complement:",dna.complement())
print("Reverse Complement:", dna.reverse_complement())