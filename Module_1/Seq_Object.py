from Bio.Seq import Seq

dna = Seq("ATGCGTACCGTA")

print("Sequence:", dna)

print("Type:", type(dna))

print("Length:", len(dna))

print("First Base:", dna[0])

print("Last Base:", dna[-1])

print("First Three:", dna[:3])

print("Last Four:", dna[-4:])