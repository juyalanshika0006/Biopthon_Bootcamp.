from Bio.Seq import Seq
dna=Seq("ATGCGT")
rna=dna.transcribe()
print("DNA:",dna)
print("RNA:", rna)